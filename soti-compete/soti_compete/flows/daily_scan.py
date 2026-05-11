"""Daily 7am scan: web_search → JSONL → score → dedup → store → route."""

from __future__ import annotations

import logging

from soti_compete.config import Config
from soti_compete.flows.pipeline import (
    ROADMAP_STUB,
    FlowResult,
    dedupe_briefs,
    persist_and_route,
    score_and_build_brief,
)
from soti_compete.jsonl import parse_jsonl
from soti_compete.llm import LLMClient, build_web_search_tool
from soti_compete.llm.prompts import (
    SYSTEM_DAILY_SCAN,
    USER_DAILY_SCAN,
    format_competitor_list,
)
from soti_compete.notify import SMTPNotifier, TeamsNotifier
from soti_compete.storage import Storage
from soti_compete.time_utils import now_local

log = logging.getLogger(__name__)


def run_daily_scan(
    *,
    config: Config,
    llm: LLMClient,
    storage: Storage,
    smtp: SMTPNotifier,
    teams: TeamsNotifier,
) -> FlowResult:
    today = now_local(config.runtime.timezone).date().isoformat()
    direct = [(c.id, c.name) for c in config.competitors.competitors if c.tier == "direct"]
    adjacent = [(c.id, c.name) for c in config.competitors.competitors if c.tier == "adjacent"]

    user_prompt = USER_DAILY_SCAN.substitute(
        lookback_days=config.runtime.flows.daily.lookback_days,
        today_iso=today,
        timezone=config.runtime.timezone,
        direct_list=format_competitor_list(direct),
        adjacent_list=format_competitor_list(adjacent),
        roadmap_stub=ROADMAP_STUB,
    )

    tool = build_web_search_tool(
        max_uses=config.runtime.web_search.budgets.daily,
        blocked_domains=config.sources.blocked_domains,
    )

    response = llm.complete(system=SYSTEM_DAILY_SCAN, user=user_prompt, tools=[tool])
    log.info("daily_scan: web_search uses=%d stop_reason=%s", response.search_count, response.stop_reason)

    parsed = parse_jsonl(response.text)
    log.info("daily_scan: parsed %d items (%d diagnostics)", len(parsed.records), len(parsed.diagnostics))

    raw_briefs = []
    unknown = 0
    for item in parsed.records:
        b = score_and_build_brief(item, config=config, flow="daily")
        if b is None:
            unknown += 1
            continue
        raw_briefs.append(b)

    fresh, dropped = dedupe_briefs(raw_briefs, storage=storage, config=config)

    result = persist_and_route(
        fresh,
        config=config,
        storage=storage,
        smtp=smtp,
        teams=teams,
        flow="daily",
        p1_strategy="digest",
    )
    result.briefs_total = len(parsed.records)
    result.briefs_deduped = dropped
    result.briefs_unknown_competitor = unknown
    result.search_count = response.search_count
    result.parse_diagnostics = [
        {"line_no": d.line_no, "error": d.error} for d in parsed.diagnostics
    ]
    return result


__all__ = ["run_daily_scan"]
