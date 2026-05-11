"""Hourly P0 sweep — direct competitors only, only P0 items routed."""

from __future__ import annotations

import logging

from soti_compete.config import Config
from soti_compete.flows.pipeline import (
    FlowResult,
    dedupe_briefs,
    persist_and_route,
    score_and_build_brief,
)
from soti_compete.jsonl import parse_jsonl
from soti_compete.llm import LLMClient, build_web_search_tool
from soti_compete.llm.prompts import (
    SYSTEM_HOURLY_SWEEP,
    USER_HOURLY_SWEEP,
    format_competitor_list,
)
from soti_compete.notify import SMTPNotifier, TeamsNotifier
from soti_compete.storage import Storage
from soti_compete.time_utils import now_local

log = logging.getLogger(__name__)

ROADMAP_STUB = "[STUB] Jira/Productboard not connected."


def run_hourly_sweep(
    *,
    config: Config,
    llm: LLMClient,
    storage: Storage,
    smtp: SMTPNotifier,
    teams: TeamsNotifier,
) -> FlowResult:
    tz = config.runtime.timezone
    now_iso = now_local(tz).isoformat(timespec="minutes")
    tiers = set(config.runtime.flows.hourly.competitor_tiers)
    routed_buckets = set(config.runtime.flows.hourly.routed_buckets)

    eligible = [(c.id, c.name) for c in config.competitors.competitors if c.tier in tiers]

    user_prompt = USER_HOURLY_SWEEP.substitute(
        now_iso=now_iso,
        direct_list=format_competitor_list(eligible),
        roadmap_stub=ROADMAP_STUB,
    )

    tool = build_web_search_tool(
        max_uses=config.runtime.web_search.budgets.hourly,
        blocked_domains=config.sources.blocked_domains,
    )

    response = llm.complete(system=SYSTEM_HOURLY_SWEEP, user=user_prompt, tools=[tool])
    parsed = parse_jsonl(response.text)
    log.info("hourly_sweep: parsed %d items (%d diagnostics)", len(parsed.records), len(parsed.diagnostics))

    raw_briefs = []
    unknown = 0
    for item in parsed.records:
        b = score_and_build_brief(item, config=config, flow="hourly")
        if b is None:
            unknown += 1
            continue
        if b.competitor_id and config.competitors.by_id(b.competitor_id).tier not in tiers:
            continue
        raw_briefs.append(b)

    fresh, dropped = dedupe_briefs(raw_briefs, storage=storage, config=config)

    p0_only = [b for b in fresh if b.bucket in routed_buckets]
    everything_else = [b for b in fresh if b.bucket not in routed_buckets]

    result = persist_and_route(
        p0_only,
        config=config,
        storage=storage,
        smtp=smtp,
        teams=teams,
        flow="hourly",
    )
    for b in everything_else:
        storage.save_brief(b)
        result.briefs_persisted += 1
        result.by_bucket[b.bucket] = result.by_bucket.get(b.bucket, 0) + 1

    result.briefs_total = len(parsed.records)
    result.briefs_deduped = dropped
    result.briefs_unknown_competitor = unknown
    result.search_count = response.search_count
    result.parse_diagnostics = [
        {"line_no": d.line_no, "error": d.error} for d in parsed.diagnostics
    ]
    return result


__all__ = ["run_hourly_sweep"]
