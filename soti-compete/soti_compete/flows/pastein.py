"""Paste-in flow: a seller/CSM submits raw text; we score and route."""

from __future__ import annotations

import logging

from soti_compete.config import Config
from soti_compete.flows.pipeline import (
    ROADMAP_STUB,
    FlowResult,
    persist_and_route,
    score_and_build_brief,
)
from soti_compete.jsonl import parse_jsonl
from soti_compete.llm import LLMClient
from soti_compete.llm.prompts import SYSTEM_PASTEIN, USER_PASTEIN
from soti_compete.notify import SMTPNotifier, TeamsNotifier
from soti_compete.storage import Storage

log = logging.getLogger(__name__)


def run_pastein(
    content: str,
    *,
    config: Config,
    llm: LLMClient,
    storage: Storage,
    smtp: SMTPNotifier,
    teams: TeamsNotifier,
) -> FlowResult:
    content = (content or "").strip()
    if not content:
        result = FlowResult(flow="pastein")
        result.errors.append("empty content")
        return result

    user_prompt = USER_PASTEIN.substitute(roadmap_stub=ROADMAP_STUB, content=content)
    response = llm.complete(system=SYSTEM_PASTEIN, user=user_prompt)

    parsed = parse_jsonl(response.text)
    log.info("pastein: parsed %d items (%d diagnostics)", len(parsed.records), len(parsed.diagnostics))

    briefs = []
    unknown = 0
    for item in parsed.records:
        b = score_and_build_brief(item, config=config, flow="pastein")
        if b is None:
            unknown += 1
            continue
        briefs.append(b)

    result = persist_and_route(
        briefs,
        config=config,
        storage=storage,
        smtp=smtp,
        teams=teams,
        flow="pastein",
        p1_strategy="individual",
    )
    result.briefs_total = len(parsed.records)
    result.briefs_unknown_competitor = unknown
    result.parse_diagnostics = [
        {"line_no": d.line_no, "error": d.error} for d in parsed.diagnostics
    ]
    result.search_count = response.search_count
    return result


__all__ = ["run_pastein"]
