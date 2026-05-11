"""Production wiring: build LLM client, storage, and notifiers from a Config."""

from __future__ import annotations

from dataclasses import dataclass

from soti_compete.config import Config, env_optional, load_config
from soti_compete.llm import LLMClient
from soti_compete.notify import SMTPNotifier, TeamsNotifier
from soti_compete.storage import SQLiteStorage, Storage


@dataclass
class Components:
    config: Config
    llm: LLMClient
    storage: Storage
    smtp: SMTPNotifier
    teams: TeamsNotifier


def bootstrap(config_dir: str | None = None) -> Components:
    config = load_config(config_dir)

    if config.runtime.storage.backend != "sqlite":
        raise RuntimeError(f"unsupported storage backend: {config.runtime.storage.backend}")
    storage = SQLiteStorage(config.runtime.storage.sqlite_path)

    llm = LLMClient(model=config.runtime.model.id, max_tokens=config.runtime.model.max_tokens)

    teams_webhook = None
    p0_teams = config.routing.teams.get("P0")
    if p0_teams and p0_teams.webhook_env:
        teams_webhook = env_optional(p0_teams.webhook_env)

    smtp = SMTPNotifier()
    teams = TeamsNotifier(webhook_url=teams_webhook)

    return Components(config=config, llm=llm, storage=storage, smtp=smtp, teams=teams)


__all__ = ["Components", "bootstrap"]
