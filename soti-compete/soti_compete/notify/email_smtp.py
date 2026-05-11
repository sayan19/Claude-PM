"""SMTP email notifier. Supports a dry-run mode that writes .eml to disk."""

from __future__ import annotations

import logging
import smtplib
import ssl
import uuid
from collections.abc import Iterable
from datetime import UTC, datetime
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from pathlib import Path

from soti_compete.config import data_dir, env_optional, is_dry_run
from soti_compete.notify.base import Notifier, NotifyResult
from soti_compete.notify.render import RenderedEmail

log = logging.getLogger(__name__)


class SMTPNotifier(Notifier):
    def __init__(
        self,
        *,
        host: str | None = None,
        port: int | None = None,
        username: str | None = None,
        password: str | None = None,
        use_tls: bool | None = None,
        sender: str | None = None,
        dry_run: bool | None = None,
        outbox_dir: Path | None = None,
    ):
        self.host = host or env_optional("SMTP_HOST")
        self.port = int(port if port is not None else env_optional("SMTP_PORT", "587") or "587")
        self.username = username if username is not None else env_optional("SMTP_USERNAME")
        self.password = password if password is not None else env_optional("SMTP_PASSWORD")
        self.use_tls = (
            use_tls
            if use_tls is not None
            else env_optional("SMTP_USE_TLS", "true").lower() in {"1", "true", "yes"}
        )
        self.sender = sender or env_optional("SMTP_FROM", "compete-bot@soti.example")
        self.dry_run = is_dry_run() if dry_run is None else dry_run
        self.outbox_dir = outbox_dir or (data_dir() / "outbox")
        self.outbox_dir.mkdir(parents=True, exist_ok=True)

    def _build_message(
        self,
        *,
        to: Iterable[str],
        cc: Iterable[str],
        rendered: RenderedEmail,
    ) -> EmailMessage:
        msg = EmailMessage()
        msg["From"] = self.sender
        msg["To"] = ", ".join(to)
        if cc:
            msg["Cc"] = ", ".join(cc)
        msg["Subject"] = rendered.subject
        msg["Date"] = formatdate(localtime=True)
        msg["Message-ID"] = make_msgid(domain="soti.compete")
        msg.set_content(rendered.plaintext)
        msg.add_alternative(rendered.html, subtype="html")
        return msg

    def send(
        self,
        *,
        to: list[str],
        rendered: RenderedEmail,
        cc: list[str] | None = None,
    ) -> NotifyResult:
        cc = cc or []
        recipients = [*to, *cc]
        if not recipients:
            return NotifyResult(success=False, detail="no recipients")

        msg = self._build_message(to=to, cc=cc, rendered=rendered)

        if self.dry_run or not self.host:
            ts = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
            slug = uuid.uuid4().hex[:8]
            path = self.outbox_dir / f"{ts}-{slug}.eml"
            path.write_bytes(bytes(msg))
            reason = "dry-run" if self.dry_run else "no SMTP_HOST configured"
            log.info("email %s -> %s (subject=%r)", reason, path, rendered.subject)
            return NotifyResult(success=True, dry_run=True, detail=str(path), payload=rendered)

        try:
            if self.port == 465:
                ctx = ssl.create_default_context()
                with smtplib.SMTP_SSL(self.host, self.port, context=ctx, timeout=30) as s:
                    if self.username:
                        s.login(self.username, self.password)
                    s.send_message(msg, to_addrs=recipients)
            else:
                with smtplib.SMTP(self.host, self.port, timeout=30) as s:
                    s.ehlo()
                    if self.use_tls:
                        s.starttls(context=ssl.create_default_context())
                        s.ehlo()
                    if self.username:
                        s.login(self.username, self.password)
                    s.send_message(msg, to_addrs=recipients)
        except (smtplib.SMTPException, OSError) as e:
            log.error("smtp send failed: %s", e)
            return NotifyResult(success=False, detail=str(e))
        return NotifyResult(success=True, detail=f"sent to {len(recipients)} recipients")

    def ping(self) -> bool:
        if self.dry_run:
            return True
        if not self.host:
            return False
        try:
            if self.port == 465:
                with smtplib.SMTP_SSL(self.host, self.port, timeout=10) as s:
                    s.noop()
            else:
                with smtplib.SMTP(self.host, self.port, timeout=10) as s:
                    s.ehlo()
            return True
        except (smtplib.SMTPException, OSError) as e:
            log.warning("smtp ping failed: %s", e)
            return False


__all__ = ["SMTPNotifier"]
