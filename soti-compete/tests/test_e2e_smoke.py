"""End-to-end smoke test.

Drives the CLI via Click's CliRunner. The Anthropic SDK is never reached;
bootstrap() is monkey-patched to inject a FakeLLM that replays a captured
JSONL fixture. Asserts on storage state and the dry-run outbox so a human
can also inspect the rendered email/Teams payloads.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from click.testing import CliRunner

from soti_compete import bootstrap as bootstrap_mod
from soti_compete.bootstrap import Components
from soti_compete.cli import cli
from soti_compete.config import load_config
from soti_compete.notify import SMTPNotifier, TeamsNotifier
from soti_compete.storage import SQLiteStorage
from tests.conftest import FakeLLM, fake_response

FIXTURE = Path(__file__).parent / "fixtures" / "daily_response.jsonl"
CONFIG_DIR = Path(__file__).resolve().parents[1] / "config"


@pytest.fixture
def workdir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("SOTI_COMPETE_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("SOTI_COMPETE_DRY_RUN", "true")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test")
    return tmp_path


@pytest.fixture
def fixture_text() -> str:
    return FIXTURE.read_text(encoding="utf-8")


def _patched_bootstrap(monkeypatch, workdir: Path, fixture_text: str) -> FakeLLM:
    fake = FakeLLM([fake_response(fixture_text, search_count=6)])

    def _bootstrap(config_dir=None):
        cfg = load_config(str(CONFIG_DIR))
        cfg = cfg.model_copy(
            update={
                "runtime": cfg.runtime.model_copy(
                    update={
                        "storage": cfg.runtime.storage.model_copy(
                            update={"sqlite_path": str(workdir / "data" / "soti.db")}
                        )
                    }
                )
            }
        )
        storage = SQLiteStorage(cfg.runtime.storage.sqlite_path)
        outbox = workdir / "data" / "outbox"
        smtp = SMTPNotifier(host="", dry_run=True, outbox_dir=outbox, sender="bot@soti.example")
        teams = TeamsNotifier(webhook_url="", dry_run=True, outbox_dir=outbox)
        return Components(config=cfg, llm=fake, storage=storage, smtp=smtp, teams=teams)

    monkeypatch.setattr(bootstrap_mod, "bootstrap", _bootstrap)
    monkeypatch.setattr("soti_compete.cli.bootstrap", _bootstrap)
    return fake


def test_cli_help_lists_all_commands():
    runner = CliRunner()
    r = runner.invoke(cli, ["--help"])
    assert r.exit_code == 0
    for cmd in ("daily", "hourly", "pastein", "sentiment", "query", "healthcheck"):
        assert cmd in r.output


def test_cli_healthcheck_passes_in_dry_run(workdir, monkeypatch):
    monkeypatch.setenv("SMTP_HOST", "")
    monkeypatch.setenv("TEAMS_WEBHOOK_URL", "")
    runner = CliRunner()
    r = runner.invoke(cli, ["--config-dir", str(CONFIG_DIR), "healthcheck"])
    assert r.exit_code == 0, r.output
    assert "OVERALL: OK" in r.output


def test_cli_daily_end_to_end(workdir, monkeypatch, fixture_text):
    fake = _patched_bootstrap(monkeypatch, workdir, fixture_text)
    runner = CliRunner()
    r = runner.invoke(cli, ["--config-dir", str(CONFIG_DIR), "daily"])
    assert r.exit_code == 0, r.output

    assert len(fake.calls) == 1
    tool = fake.calls[0]["tools"][0]
    assert tool["type"] == "web_search_20250305"
    assert tool["max_uses"] >= 1

    outbox = workdir / "data" / "outbox"
    emls = list(outbox.glob("*.eml"))
    teams_files = list(outbox.glob("*.teams.json"))
    assert any("P0 COMPETE" in f.read_text(errors="ignore") for f in emls), "expected a P0 email"
    assert any("Compete Daily" in f.read_text(errors="ignore") for f in emls), "expected a P1 digest"
    assert len(teams_files) >= 1, "expected at least one Teams card"

    storage = SQLiteStorage(workdir / "data" / "soti.db")
    rows = storage.query_briefs(limit=100)
    assert len(rows) >= 3
    by_bucket = {b.bucket: 0 for b in rows}
    for b in rows:
        by_bucket[b.bucket] += 1
    assert by_bucket.get("P0", 0) >= 1
    assert by_bucket.get("P1", 0) >= 1


def test_cli_query_after_daily(workdir, monkeypatch, fixture_text):
    _patched_bootstrap(monkeypatch, workdir, fixture_text)
    runner = CliRunner()

    runner.invoke(cli, ["--config-dir", str(CONFIG_DIR), "daily"])

    r = runner.invoke(cli, ["--config-dir", str(CONFIG_DIR), "query", "--bucket", "P0"])
    assert r.exit_code == 0, r.output
    assert "[P0]" in r.output
    assert "jamf" in r.output

    r = runner.invoke(cli, ["--config-dir", str(CONFIG_DIR), "query",
                            "--competitor", "intune", "--since", "7d"])
    assert r.exit_code == 0
    assert "intune" in r.output


def test_cli_daily_idempotent_on_repeat(workdir, monkeypatch, fixture_text):
    _patched_bootstrap(monkeypatch, workdir, fixture_text)
    runner = CliRunner()

    r1 = runner.invoke(cli, ["--config-dir", str(CONFIG_DIR), "daily"])
    assert r1.exit_code == 0

    _patched_bootstrap(monkeypatch, workdir, fixture_text)
    r2 = runner.invoke(cli, ["--config-dir", str(CONFIG_DIR), "daily"])
    assert r2.exit_code == 0
    assert "briefs_deduped" in r2.output
    assert "briefs_persisted: 0" in r2.output


def test_cli_pastein_via_text_flag(workdir, monkeypatch, fixture_text):
    one_item = fixture_text.splitlines()[0]
    _patched_bootstrap(monkeypatch, workdir, one_item)
    runner = CliRunner()
    r = runner.invoke(cli, ["--config-dir", str(CONFIG_DIR), "pastein",
                            "-t", "Customer says Jamf is acquiring Identity Automation"])
    assert r.exit_code == 0, r.output
    assert "briefs_persisted: 1" in r.output
