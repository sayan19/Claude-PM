"""Monthly sentiment job: one snapshot per tracked competitor.

Aggregates Reddit/Peerspot/G2 mentions via `web_search` with `allowed_domains`
filters. Output is a single JSON object per competitor (not JSONL) — the
sentiment prompt enforces this.
"""

from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

from soti_compete.config import Config
from soti_compete.jsonl import parse_jsonl
from soti_compete.llm import LLMClient, build_web_search_tool
from soti_compete.llm.prompts import SYSTEM_SENTIMENT, USER_SENTIMENT
from soti_compete.notify import SMTPNotifier
from soti_compete.notify.render import render_email
from soti_compete.storage import SentimentSnapshot, Storage
from soti_compete.storage.base import Brief
from soti_compete.time_utils import now_local

log = logging.getLogger(__name__)


@dataclass
class SentimentResult:
    flow: str = "sentiment"
    competitors_scanned: int = 0
    snapshots_saved: int = 0
    digest_sent: bool = False
    search_count: int = 0
    parse_diagnostics: list[dict[str, Any]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def _platforms_block(config: Config) -> tuple[str, list[str]]:
    lines = []
    domains: list[str] = []
    for platform, spec in config.sources.sentiment_sources.items():
        allowed = spec.get("allowed_domains") or []
        domains.extend(allowed)
        lines.append(f"  - {platform}: {', '.join(allowed)}")
    return "\n".join(lines), list(dict.fromkeys(domains))


def _scan_one(
    *,
    competitor_name: str,
    competitor_id: str,
    aliases: list[str],
    platforms_text: str,
    allowed_domains: list[str],
    config: Config,
    llm: LLMClient,
    now_iso: str,
) -> tuple[dict | None, int, list[dict[str, Any]]]:
    user_prompt = USER_SENTIMENT.substitute(
        competitor_name=competitor_name,
        competitor_id=competitor_id,
        lookback_days=config.runtime.flows.sentiment.lookback_days,
        today_iso=now_iso,
        platforms=platforms_text,
        aliases=", ".join(aliases) or "(none)",
    )

    tool = build_web_search_tool(
        max_uses=config.runtime.web_search.budgets.sentiment_per_competitor,
        allowed_domains=allowed_domains,
        blocked_domains=config.sources.blocked_domains,
    )

    response = llm.complete(system=SYSTEM_SENTIMENT, user=user_prompt, tools=[tool])
    parsed = parse_jsonl(response.text)
    diagnostics = [{"line_no": d.line_no, "error": d.error} for d in parsed.diagnostics]

    if not parsed.records:
        log.warning("sentiment: no parseable snapshot for %s", competitor_id)
        return None, response.search_count, diagnostics

    return parsed.records[0], response.search_count, diagnostics


def run_sentiment_monthly(
    *,
    config: Config,
    llm: LLMClient,
    storage: Storage,
    smtp: SMTPNotifier,
) -> SentimentResult:
    tz = config.runtime.timezone
    today = now_local(tz).date()
    period_days = config.runtime.flows.sentiment.lookback_days
    period_start = today - timedelta(days=period_days)
    now_iso = today.isoformat()

    platforms_text, allowed_domains = _platforms_block(config)

    result = SentimentResult()
    snapshots: list[SentimentSnapshot] = []
    for c in config.competitors.competitors:
        result.competitors_scanned += 1
        data, search_count, diagnostics = _scan_one(
            competitor_name=c.name,
            competitor_id=c.id,
            aliases=c.aliases,
            platforms_text=platforms_text,
            allowed_domains=allowed_domains,
            config=config,
            llm=llm,
            now_iso=now_iso,
        )
        result.search_count += search_count
        result.parse_diagnostics.extend(diagnostics)
        if data is None:
            result.errors.append(f"{c.id}: no snapshot returned")
            continue

        snapshot = SentimentSnapshot(
            id=f"{c.id}-{today.isoformat()}-{uuid.uuid4().hex[:6]}",
            competitor_id=c.id,
            period_start=_to_dt(period_start),
            period_end=_to_dt(today),
            summary=data,
            sources=data.get("sources") or [],
        )
        storage.save_sentiment(snapshot)
        snapshots.append(snapshot)
        result.snapshots_saved += 1

    if snapshots:
        result.digest_sent = _send_digest(snapshots, config=config, smtp=smtp, today_iso=now_iso)

    return result


def _to_dt(d: date):
    from datetime import UTC, datetime
    return datetime(d.year, d.month, d.day, tzinfo=UTC)


def _send_digest(
    snapshots: list[SentimentSnapshot],
    *,
    config: Config,
    smtp: SMTPNotifier,
    today_iso: str,
) -> bool:
    route = config.routing.email.get("sentiment")
    if not route or not route.to:
        return False

    briefs = [_snapshot_to_brief(s) for s in snapshots]
    subject = f"{route.subject_prefix} {today_iso}".strip()
    rendered = render_email(
        briefs,
        subject=subject,
        heading="Monthly Public Sentiment Snapshot",
        subheading=f"{len(snapshots)} competitor(s)",
    )
    res = smtp.send(to=route.to, cc=route.cc, rendered=rendered)
    return res.success


def _snapshot_to_brief(s: SentimentSnapshot) -> Brief:
    data = s.summary or {}
    themes = data.get("themes") or []
    theme_text = "; ".join(f"{t.get('label')} ({t.get('polarity', 'mixed')})" for t in themes[:6])
    summary = (
        f"Net sentiment {data.get('net_sentiment', 0):+.2f} ({data.get('volume', 'unknown')} volume). "
        f"Themes: {theme_text or 'n/a'}."
    )
    return Brief(
        id=s.id,
        url="",
        url_fingerprint="",
        title=f"{s.competitor_id}: sentiment snapshot",
        competitor_id=s.competitor_id,
        news_type="analyst",
        response_type="housekeeping",
        confidence_signal="multi_source",
        bucket="P2",
        raw_score=0.0,
        recency_multiplier=1.0,
        confidence_multiplier=1.0,
        final_score=0.0,
        dimensions={},
        summary=summary,
        gap_analysis={},
        sources=[
            {"url": q.get("url", ""), "domain": q.get("platform", "")}
            for q in (data.get("notable_quotes") or []) if q.get("url")
        ] + (data.get("sources") or []),
        flow="sentiment",
        raw_payload=data,
        created_at=s.created_at,
    )


__all__ = ["SentimentResult", "run_sentiment_monthly"]
