"""Verify all integrations are reachable. Used by `soti-compete healthcheck`."""

from __future__ import annotations

import logging
import os
from collections.abc import Callable
from dataclasses import dataclass, field

from soti_compete.config import Config, data_dir, load_config
from soti_compete.notify.email_smtp import SMTPNotifier
from soti_compete.notify.teams import TeamsNotifier
from soti_compete.storage.sqlite import SQLiteStorage

log = logging.getLogger(__name__)


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str = ""


@dataclass
class HealthReport:
    results: list[CheckResult] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return all(r.ok for r in self.results)

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.results.append(CheckResult(name=name, ok=ok, detail=detail))

    def format(self) -> str:
        lines = []
        for r in self.results:
            status = "OK " if r.ok else "FAIL"
            lines.append(f"[{status}] {r.name}: {r.detail}" if r.detail else f"[{status}] {r.name}")
        lines.append("")
        lines.append("OVERALL: " + ("OK" if self.ok else "FAIL"))
        return "\n".join(lines)


def _check_config(config_dir_path: str | None = None) -> tuple[bool, str, Config | None]:
    try:
        cfg = load_config(config_dir_path)
    except Exception as e:
        return False, f"{type(e).__name__}: {e}", None
    return True, f"{len(cfg.competitors.competitors)} competitors loaded", cfg


def _check_anthropic_env() -> tuple[bool, str]:
    if os.environ.get("ANTHROPIC_API_KEY"):
        return True, "ANTHROPIC_API_KEY present"
    return False, "ANTHROPIC_API_KEY not set"


def _check_storage(cfg: Config) -> tuple[bool, str]:
    if cfg.runtime.storage.backend != "sqlite":
        return False, f"unsupported backend: {cfg.runtime.storage.backend}"
    try:
        store = SQLiteStorage(cfg.runtime.storage.sqlite_path)
        return (store.ping(), f"sqlite at {cfg.runtime.storage.sqlite_path}")
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def _check_smtp() -> tuple[bool, str]:
    n = SMTPNotifier()
    if n.dry_run:
        return True, "dry-run mode (no live SMTP check)"
    if not n.host:
        return False, "SMTP_HOST not configured"
    return n.ping(), f"smtp {n.host}:{n.port}"


def _check_teams() -> tuple[bool, str]:
    n = TeamsNotifier()
    if n.dry_run:
        return True, "dry-run mode (no live webhook check)"
    if not n.webhook_url:
        return False, "TEAMS_WEBHOOK_URL not configured"
    return True, "webhook URL configured"


def _check_outbox_writable() -> tuple[bool, str]:
    try:
        d = data_dir() / "outbox"
        d.mkdir(parents=True, exist_ok=True)
        probe = d / ".healthcheck"
        probe.write_text("ok")
        probe.unlink()
        return True, f"writable at {d}"
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def run_healthcheck(config_dir_path: str | None = None) -> HealthReport:
    report = HealthReport()

    ok, detail, cfg = _check_config(config_dir_path)
    report.add("config", ok, detail)
    if not ok or cfg is None:
        return report

    for name, fn in _build_check_list(cfg):
        ok, detail = fn()
        report.add(name, ok, detail)

    return report


def _build_check_list(cfg: Config) -> list[tuple[str, Callable[[], tuple[bool, str]]]]:
    return [
        ("anthropic_env", _check_anthropic_env),
        ("storage", lambda: _check_storage(cfg)),
        ("smtp", _check_smtp),
        ("teams", _check_teams),
        ("outbox", _check_outbox_writable),
    ]


__all__ = ["CheckResult", "HealthReport", "run_healthcheck"]
