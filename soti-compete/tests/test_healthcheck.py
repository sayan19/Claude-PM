from __future__ import annotations

import pytest

from soti_compete.healthcheck import run_healthcheck


@pytest.fixture(autouse=True)
def isolated_env(monkeypatch, tmp_path):
    monkeypatch.setenv("SOTI_COMPETE_DRY_RUN", "true")
    monkeypatch.setenv("SOTI_COMPETE_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test")
    monkeypatch.setenv("SMTP_HOST", "")
    monkeypatch.setenv("TEAMS_WEBHOOK_URL", "")


def test_run_healthcheck_returns_ok_in_dry_run(config_dir, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    report = run_healthcheck(str(config_dir))
    assert report.ok is True
    names = [r.name for r in report.results]
    assert names == ["config", "anthropic_env", "storage", "smtp", "teams", "outbox"]


def test_run_healthcheck_fails_without_anthropic_key(config_dir, monkeypatch, tmp_path):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.chdir(tmp_path)
    report = run_healthcheck(str(config_dir))
    assert report.ok is False
    bad = [r for r in report.results if r.name == "anthropic_env"][0]
    assert bad.ok is False


def test_run_healthcheck_fails_on_bad_config(tmp_path):
    report = run_healthcheck(str(tmp_path / "missing-config-dir"))
    assert report.ok is False
    assert report.results[0].name == "config"
    assert report.results[0].ok is False


def test_format_report(config_dir, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    report = run_healthcheck(str(config_dir))
    out = report.format()
    assert "OVERALL" in out
    assert "config" in out
