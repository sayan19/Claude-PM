"""Microsoft Teams notifier via incoming webhook.

Phase 1 uses raw HTTPS POST of an Adaptive Card payload, which works for both
Power Automate webhooks and legacy Office 365 connectors. Dry-run writes the
JSON payload to disk for inspection.
"""

from __future__ import annotations

import json
import logging
import urllib.error
import urllib.request
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from soti_compete.config import data_dir, env_optional, is_dry_run
from soti_compete.notify.base import Notifier, NotifyResult

log = logging.getLogger(__name__)


class TeamsNotifier(Notifier):
    def __init__(
        self,
        *,
        webhook_url: str | None = None,
        dry_run: bool | None = None,
        outbox_dir: Path | None = None,
    ):
        self.webhook_url = webhook_url if webhook_url is not None else env_optional("TEAMS_WEBHOOK_URL")
        self.dry_run = is_dry_run() if dry_run is None else dry_run
        self.outbox_dir = outbox_dir or (data_dir() / "outbox")
        self.outbox_dir.mkdir(parents=True, exist_ok=True)

    def send(self, *, payload: dict[str, Any]) -> NotifyResult:
        if self.dry_run or not self.webhook_url:
            ts = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
            slug = uuid.uuid4().hex[:8]
            path = self.outbox_dir / f"{ts}-{slug}.teams.json"
            path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
            reason = "dry-run" if self.dry_run else "no TEAMS_WEBHOOK_URL configured"
            log.info("teams %s -> %s", reason, path)
            return NotifyResult(success=True, dry_run=True, detail=str(path), payload=payload)

        try:
            req = urllib.request.Request(
                self.webhook_url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                status = resp.status
                body = resp.read().decode("utf-8", errors="replace")
        except urllib.error.URLError as e:
            log.error("teams webhook failed: %s", e)
            return NotifyResult(success=False, detail=str(e))
        if 200 <= status < 300:
            return NotifyResult(success=True, detail=f"http {status}")
        return NotifyResult(success=False, detail=f"http {status}: {body[:200]}")

    def ping(self) -> bool:
        if self.dry_run:
            return True
        return bool(self.webhook_url)


__all__ = ["TeamsNotifier"]
