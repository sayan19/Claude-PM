from __future__ import annotations

from pathlib import Path

import pytest

from soti_compete.llm.client import LLMResponse
from soti_compete.notify import SMTPNotifier, TeamsNotifier
from soti_compete.storage import SQLiteStorage

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = REPO_ROOT / "config"


@pytest.fixture
def config_dir() -> Path:
    return CONFIG_DIR


@pytest.fixture
def config():
    from soti_compete.config import load_config

    return load_config(CONFIG_DIR)


@pytest.fixture
def storage(tmp_path):
    return SQLiteStorage(tmp_path / "test.db")


@pytest.fixture
def notifiers(tmp_path):
    outbox = tmp_path / "outbox"
    smtp = SMTPNotifier(host="", dry_run=True, outbox_dir=outbox, sender="bot@soti.example")
    teams = TeamsNotifier(webhook_url="", dry_run=True, outbox_dir=outbox)
    return smtp, teams


class FakeLLM:
    """Replays canned LLM responses. Captures each `complete()` call in `calls`."""

    def __init__(self, responses: list[LLMResponse]):
        self._responses = list(responses)
        self.calls: list[dict] = []

    def complete(self, **kwargs):
        self.calls.append(kwargs)
        if not self._responses:
            return LLMResponse(text="")
        return self._responses.pop(0)


def fake_response(text: str, *, search_count: int = 0) -> LLMResponse:
    return LLMResponse(text=text, search_count=search_count, stop_reason="end_turn")
