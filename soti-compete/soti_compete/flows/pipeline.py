"""Shared pipeline helpers used by every flow.

The flows are thin orchestrators that:
  1. Call the LLM with a prompt
  2. parse_jsonl(response.text)
  3. score_and_build_brief() each parsed item
  4. dedupe_briefs() against recent storage
  5. persist_and_route() based on bucket

Everything here is pure-ish (no Anthropic, no network) so it's straightforward
to unit-test by injecting fake LLM responses.
"""

from __future__ import annotations

import hashlib
import logging
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any
from urllib.parse import urlsplit

from soti_compete.classify import (
    coerce_confidence,
    coerce_news_type,
    coerce_response_type,
)
from soti_compete.config import Config
from soti_compete.dedup import (
    SeenItem,
    canonicalize_url,
    is_duplicate,
    url_fingerprint,
)
from soti_compete.notify import SMTPNotifier, TeamsNotifier
from soti_compete.notify.base import NotifyResult
from soti_compete.notify.render import render_email, render_teams_card
from soti_compete.scoring import DimensionScores, score, tier_score
from soti_compete.storage import Brief, Storage
from soti_compete.time_utils import age_days, now_utc, parse_when

log = logging.getLogger(__name__)


@dataclass
class FlowResult:
    flow: str
    briefs_total: int = 0
    briefs_persisted: int = 0
    briefs_deduped: int = 0
    briefs_unknown_competitor: int = 0
    by_bucket: dict[str, int] = field(default_factory=lambda: {"P0": 0, "P1": 0, "P2": 0, "DROP": 0})
    p0_emails_sent: int = 0
    p0_teams_sent: int = 0
    p1_digest_sent: bool = False
    parse_diagnostics: list[dict[str, Any]] = field(default_factory=list)
    search_count: int = 0
    errors: list[str] = field(default_factory=list)


def _domain_of(url: str) -> str:
    if not url:
        return ""
    try:
        netloc = urlsplit(url).netloc.lower()
    except ValueError:
        return ""
    return netloc[4:] if netloc.startswith("www.") else netloc


def _source_class(domain: str, competitor_id: str | None, config: Config) -> str:
    return config.sources.classify_domain(domain, competitor_id) if domain else "secondary"


def _brief_id(url: str, title: str, competitor_id: str | None, published_at: datetime | None) -> str:
    fp = url_fingerprint(url) if url else ""
    if fp:
        return fp
    raw = f"{competitor_id or ''}|{title}|{published_at.isoformat() if published_at else ''}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def _coerce_int(value: Any, default: int) -> int:
    try:
        v = int(round(float(value)))
        return max(0, min(10, v))
    except (TypeError, ValueError):
        return default


def score_and_build_brief(
    item: dict[str, Any],
    *,
    config: Config,
    flow: str,
    now: datetime | None = None,
) -> Brief | None:
    """Transform one parsed LLM item into a scored, persisted-ready Brief.

    Returns None if the competitor id is unknown — we don't score outside the
    tracked list. Caller logs and counts.
    """
    competitor_id = (item.get("competitor_id") or "").strip().lower() or None
    competitor = config.competitors.by_id(competitor_id) if competitor_id else None
    if competitor is None:
        log.info("skip item: unknown competitor_id=%r", competitor_id)
        return None

    raw_dims = item.get("dimensions") or {}
    primary_url = item.get("url") or ""
    sources_in = item.get("sources") or []
    if not sources_in and primary_url:
        sources_in = [{"url": primary_url, "domain": _domain_of(primary_url)}]

    primary_source_class = _source_class(
        _domain_of(sources_in[0]["url"]) if sources_in else "",
        competitor_id,
        config,
    )
    sq_from_model = _coerce_int(raw_dims.get("source_quality"), default=-1)
    sq_from_domain = config.scoring.source_quality_scores.get(primary_source_class, 2)
    source_quality = max(sq_from_model, sq_from_domain) if sq_from_model >= 0 else sq_from_domain

    dims = DimensionScores(
        strategic_impact=_coerce_int(raw_dims.get("strategic_impact"), default=4),
        sales_signal=_coerce_int(
            raw_dims.get("sales_signal"),
            default=config.scoring.phase_1_defaults.sales_signal_no_deal_motion,
        ),
        roadmap_overlap=_coerce_int(
            raw_dims.get("roadmap_overlap"),
            default=config.scoring.phase_1_defaults.roadmap_overlap_conservative,
        ),
        competitor_tier=tier_score(config.scoring, competitor.tier),
        source_quality=source_quality,
    )

    published_at = parse_when(item.get("published_at"))
    age = age_days(published_at, reference=now or now_utc()) if published_at else 0.0

    news_type = coerce_news_type(item.get("news_type"))
    response_type = coerce_response_type(item.get("response_type"))
    confidence = coerce_confidence(item.get("confidence_signal"))

    result = score(
        config.scoring,
        dims,
        age_days=age,
        news_type=news_type,
        confidence_signal=confidence,
    )

    title = (item.get("headline") or "").strip() or "[no headline]"
    summary = (item.get("summary") or "").strip()
    gap = item.get("gap_analysis") or {}
    enriched_sources = [
        {"url": s.get("url", ""), "domain": s.get("domain") or _domain_of(s.get("url", ""))}
        for s in sources_in
        if s.get("url")
    ]

    return Brief(
        id=_brief_id(primary_url, title, competitor_id, published_at),
        url=canonicalize_url(primary_url),
        url_fingerprint=url_fingerprint(primary_url) if primary_url else "",
        title=title,
        competitor_id=competitor_id,
        news_type=news_type.value if news_type else None,
        response_type=response_type.value,
        confidence_signal=confidence.value,
        bucket=result.bucket,
        raw_score=result.raw,
        recency_multiplier=result.recency,
        confidence_multiplier=result.confidence,
        final_score=result.final,
        dimensions=result.breakdown,
        summary=summary,
        gap_analysis=gap,
        sources=enriched_sources,
        flow=flow,
        raw_payload=item,
        created_at=now or now_utc(),
    )


def dedupe_briefs(
    briefs: list[Brief],
    *,
    storage: Storage,
    config: Config,
) -> tuple[list[Brief], int]:
    """Remove items already seen in storage within the dedup lookback window.

    Returns (fresh_briefs, dropped_count). New items found in this batch are
    added to the running seen-set so intra-batch duplicates are also removed.
    """
    threshold = config.runtime.dedup.title_similarity_threshold
    lookback = config.runtime.dedup.lookback_days
    seen = storage.recent_seen_items(lookback)

    fresh: list[Brief] = []
    dropped = 0
    for b in briefs:
        if is_duplicate(b.url, b.title, b.competitor_id, seen, similarity_threshold=threshold):
            dropped += 1
            continue
        fresh.append(b)
        seen.append(SeenItem(url_fingerprint=b.url_fingerprint, title=b.title, competitor_id=b.competitor_id))
    return fresh, dropped


def _send_p0(
    brief: Brief,
    *,
    config: Config,
    smtp: SMTPNotifier,
    teams: TeamsNotifier,
) -> tuple[bool, bool]:
    email_sent = False
    teams_sent = False

    email_route = config.routing.email.get("P0")
    if email_route and email_route.to:
        subject = f"{email_route.subject_prefix} {brief.title}".strip()
        rendered = render_email([brief], subject=subject, heading=subject)
        res: NotifyResult = smtp.send(to=email_route.to, cc=email_route.cc, rendered=rendered)
        email_sent = res.success

    teams_route = config.routing.teams.get("P0")
    if teams_route and teams_route.enabled:
        card = render_teams_card(brief, title_prefix=teams_route.title_prefix or "P0 Competitive Alert")
        res = teams.send(payload=card)
        teams_sent = res.success

    return email_sent, teams_sent


def _send_p1_digest(
    briefs: list[Brief],
    *,
    config: Config,
    smtp: SMTPNotifier,
    flow: str,
) -> bool:
    if not briefs:
        return False
    route = config.routing.email.get("P1")
    if not route or not route.to:
        return False
    if flow != "daily" and not (route.digest or route.digest_only):
        return False
    subject = f"{route.subject_prefix} {date.today().isoformat()}".strip()
    rendered = render_email(briefs, subject=subject, heading="P1 Digest", subheading=f"{len(briefs)} item(s)")
    res = smtp.send(to=route.to, cc=route.cc, rendered=rendered)
    return res.success


def persist_and_route(
    briefs: list[Brief],
    *,
    config: Config,
    storage: Storage,
    smtp: SMTPNotifier,
    teams: TeamsNotifier,
    flow: str,
    route_p1_digest: bool = False,
    route_p1_individually: bool = False,
) -> FlowResult:
    result = FlowResult(flow=flow, briefs_total=len(briefs))

    p1_items: list[Brief] = []
    for b in briefs:
        storage.save_brief(b)
        result.briefs_persisted += 1
        result.by_bucket[b.bucket] = result.by_bucket.get(b.bucket, 0) + 1

        if b.bucket == "P0":
            email_sent, teams_sent = _send_p0(b, config=config, smtp=smtp, teams=teams)
            result.p0_emails_sent += int(email_sent)
            result.p0_teams_sent += int(teams_sent)
        elif b.bucket == "P1":
            if route_p1_individually:
                route = config.routing.email.get("P1")
                if route and route.to:
                    subject = f"{route.subject_prefix} {b.title}".strip()
                    rendered = render_email([b], subject=subject, heading=subject)
                    smtp.send(to=route.to, cc=route.cc, rendered=rendered)
            else:
                p1_items.append(b)

    if route_p1_digest and p1_items:
        result.p1_digest_sent = _send_p1_digest(p1_items, config=config, smtp=smtp, flow=flow)

    return result


__all__ = [
    "FlowResult",
    "dedupe_briefs",
    "persist_and_route",
    "score_and_build_brief",
]
