from __future__ import annotations

import email
import email.policy
import json

from soti_compete.notify import SMTPNotifier, TeamsNotifier
from soti_compete.notify.render import RenderedEmail


def test_smtp_dry_run_writes_eml(tmp_path):
    outbox = tmp_path / "outbox"
    n = SMTPNotifier(host="", dry_run=True, outbox_dir=outbox, sender="bot@soti.example")
    rendered = RenderedEmail(
        subject="[P0 COMPETE] Test",
        plaintext="hello plain",
        html="<p>hello html</p>",
    )
    r = n.send(to=["pm@soti.example"], rendered=rendered, cc=["leadership@soti.example"])
    assert r.success and r.dry_run
    eml_files = list(outbox.glob("*.eml"))
    assert len(eml_files) == 1

    msg = email.message_from_bytes(eml_files[0].read_bytes(), policy=email.policy.default)
    assert msg["Subject"] == "[P0 COMPETE] Test"
    assert msg["To"] == "pm@soti.example"
    assert msg["Cc"] == "leadership@soti.example"
    assert msg["From"] == "bot@soti.example"

    parts = {p.get_content_type(): p.get_content() for p in msg.iter_parts()}
    assert "text/plain" in parts and "hello plain" in parts["text/plain"]
    assert "text/html" in parts and "hello html" in parts["text/html"]


def test_smtp_no_host_falls_back_to_outbox(tmp_path):
    n = SMTPNotifier(host="", dry_run=False, outbox_dir=tmp_path)
    rendered = RenderedEmail(subject="x", plaintext="x", html="<p>x</p>")
    r = n.send(to=["a@b.c"], rendered=rendered)
    assert r.success and r.dry_run is True


def test_smtp_no_recipients_fails(tmp_path):
    n = SMTPNotifier(host="", dry_run=True, outbox_dir=tmp_path)
    rendered = RenderedEmail(subject="x", plaintext="x", html="<p>x</p>")
    r = n.send(to=[], rendered=rendered)
    assert r.success is False


def test_smtp_ping_dry_run_true(tmp_path):
    n = SMTPNotifier(host="", dry_run=True, outbox_dir=tmp_path)
    assert n.ping() is True


def test_smtp_ping_unconfigured_false(tmp_path):
    n = SMTPNotifier(host="", dry_run=False, outbox_dir=tmp_path)
    assert n.ping() is False


def test_teams_dry_run_writes_json(tmp_path):
    n = TeamsNotifier(webhook_url="", dry_run=True, outbox_dir=tmp_path)
    payload = {"type": "message", "attachments": [{"foo": "bar"}]}
    r = n.send(payload=payload)
    assert r.success and r.dry_run
    files = list(tmp_path.glob("*.teams.json"))
    assert len(files) == 1
    data = json.loads(files[0].read_text())
    assert data["attachments"][0]["foo"] == "bar"


def test_teams_no_webhook_url_falls_back_to_outbox(tmp_path):
    n = TeamsNotifier(webhook_url="", dry_run=False, outbox_dir=tmp_path)
    r = n.send(payload={"x": 1})
    assert r.success and r.dry_run is True


def test_teams_ping_with_webhook(tmp_path):
    n = TeamsNotifier(webhook_url="https://outlook.office.com/webhook/abc", dry_run=False, outbox_dir=tmp_path)
    assert n.ping() is True


def test_teams_ping_without_webhook(tmp_path):
    n = TeamsNotifier(webhook_url="", dry_run=False, outbox_dir=tmp_path)
    assert n.ping() is False
