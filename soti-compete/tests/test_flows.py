from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta

from soti_compete.flows import (
    run_daily_scan,
    run_hourly_sweep,
    run_pastein,
    run_sentiment_monthly,
)
from soti_compete.flows.pipeline import (
    dedupe_briefs,
    persist_and_route,
    score_and_build_brief,
)
from tests.conftest import FakeLLM
from tests.conftest import fake_response as _fake_response


def _p0_item() -> dict:
    return {
        "competitor_id": "jamf",
        "headline": "Jamf acquires Y for $200M",
        "summary": "Jamf announced an acquisition expanding device-trust posture.",
        "url": "https://jamf.com/pr/y-acquisition",
        "published_at": (datetime.now(UTC) - timedelta(days=1)).date().isoformat(),
        "news_type": "acquisition",
        "response_type": "obligation",
        "confidence_signal": "multi_source",
        "dimensions": {"strategic_impact": 9, "sales_signal": 7, "roadmap_overlap": 5, "source_quality": 10},
        "sources": [
            {"url": "https://jamf.com/pr/y", "domain": "jamf.com"},
            {"url": "https://reuters.com/x", "domain": "reuters.com"},
        ],
        "gap_analysis": {
            "soti_today": "Limited device-trust integration.",
            "roadmap": "[STUB] Jira not connected",
            "others": "Intune via Entra; Omnissa via Workspace ONE",
        },
    }


def _p2_item() -> dict:
    return {
        "competitor_id": "knox",
        "headline": "Samsung Knox publishes a small documentation update",
        "summary": "Minor doc refresh.",
        "url": "https://samsungknox.com/blog/docs-may",
        "published_at": (datetime.now(UTC) - timedelta(days=40)).date().isoformat(),
        "news_type": "feature_launch",
        "response_type": "housekeeping",
        "confidence_signal": "single",
        "dimensions": {"strategic_impact": 2, "sales_signal": 2, "roadmap_overlap": 2, "source_quality": 5},
        "sources": [{"url": "https://samsungknox.com/blog/docs-may", "domain": "samsungknox.com"}],
        "gap_analysis": {},
    }


def _items_to_jsonl(items: list[dict]) -> str:
    return "\n".join(json.dumps(i) for i in items)


def test_score_and_build_brief_basic(config):
    brief = score_and_build_brief(_p0_item(), config=config, flow="daily")
    assert brief is not None
    assert brief.competitor_id == "jamf"
    assert brief.bucket == "P0"
    assert brief.flow == "daily"
    assert brief.dimensions["competitor_tier"] == 10
    assert brief.dimensions["source_quality"] == 10
    assert brief.url_fingerprint
    assert brief.gap_analysis["roadmap"].startswith("[STUB]")


def test_score_and_build_brief_unknown_competitor_returns_none(config):
    bad = _p0_item()
    bad["competitor_id"] = "blackberry"
    assert score_and_build_brief(bad, config=config, flow="daily") is None


def test_score_and_build_brief_uses_phase1_defaults_for_missing_dims(config):
    item = _p0_item()
    item["dimensions"] = {"strategic_impact": 8}
    brief = score_and_build_brief(item, config=config, flow="daily")
    assert brief.dimensions["sales_signal"] == config.scoring.phase_1_defaults.sales_signal_no_deal_motion
    assert brief.dimensions["roadmap_overlap"] == config.scoring.phase_1_defaults.roadmap_overlap_conservative


def test_score_and_build_brief_clamps_out_of_range(config):
    item = _p0_item()
    item["dimensions"] = {"strategic_impact": 99, "sales_signal": -3, "roadmap_overlap": "bad", "source_quality": 8}
    brief = score_and_build_brief(item, config=config, flow="daily")
    assert brief.dimensions["strategic_impact"] == 10
    assert brief.dimensions["sales_signal"] == 0
    assert brief.dimensions["roadmap_overlap"] == config.scoring.phase_1_defaults.roadmap_overlap_conservative


def test_score_and_build_brief_promotes_source_quality_from_domain(config):
    """Even if LLM under-rates source_quality, a known vendor/tier-1 domain bumps it."""
    item = _p0_item()
    item["dimensions"]["source_quality"] = 2
    item["sources"] = [{"url": "https://reuters.com/x", "domain": "reuters.com"}]
    brief = score_and_build_brief(item, config=config, flow="daily")
    assert brief.dimensions["source_quality"] == 8  # tier_1_press


def test_score_and_build_brief_missing_url_still_works(config):
    item = _p0_item()
    item["url"] = ""
    item["sources"] = []
    brief = score_and_build_brief(item, config=config, flow="pastein")
    assert brief is not None
    assert brief.url == ""
    assert brief.id  # falls back to hash


def test_dedupe_filters_against_storage(config, storage):
    brief = score_and_build_brief(_p0_item(), config=config, flow="daily")
    storage.save_brief(brief)

    duplicate = score_and_build_brief(_p0_item(), config=config, flow="daily")
    fresh, dropped = dedupe_briefs([duplicate], storage=storage, config=config)
    assert fresh == []
    assert dropped == 1


def test_dedupe_passes_through_unseen(config, storage):
    new_item = _p0_item()
    new_item["url"] = "https://jamf.com/pr/different"
    new_item["headline"] = "Totally unrelated Jamf news about something else"
    brief = score_and_build_brief(new_item, config=config, flow="daily")
    fresh, dropped = dedupe_briefs([brief], storage=storage, config=config)
    assert len(fresh) == 1
    assert dropped == 0


def test_persist_and_route_p0_sends_email_and_teams(config, storage, notifiers, tmp_path):
    smtp, teams = notifiers
    brief = score_and_build_brief(_p0_item(), config=config, flow="daily")
    result = persist_and_route(
        [brief], config=config, storage=storage, smtp=smtp, teams=teams, flow="daily",
    )
    assert result.by_bucket["P0"] == 1
    assert result.p0_emails_sent == 1
    assert result.p0_teams_sent == 1
    assert len(list((tmp_path / "outbox").glob("*.eml"))) == 1
    assert len(list((tmp_path / "outbox").glob("*.teams.json"))) == 1


def test_persist_and_route_p2_persists_only(config, storage, notifiers, tmp_path):
    smtp, teams = notifiers
    brief = score_and_build_brief(_p2_item(), config=config, flow="daily")
    assert brief.bucket in {"P2", "DROP"}
    result = persist_and_route(
        [brief], config=config, storage=storage, smtp=smtp, teams=teams, flow="daily",
    )
    assert result.p0_emails_sent == 0
    assert result.p0_teams_sent == 0
    assert list((tmp_path / "outbox").glob("*.eml")) == []
    assert storage.get_brief(brief.id) is not None


def test_persist_and_route_p1_digest_only_when_requested(config, storage, notifiers, tmp_path):
    smtp, teams = notifiers
    item = _p0_item()
    item["dimensions"]["strategic_impact"] = 7
    item["dimensions"]["sales_signal"] = 5
    item["confidence_signal"] = "single"
    brief = score_and_build_brief(item, config=config, flow="daily")
    assert brief.bucket == "P1"

    persist_and_route(
        [brief], config=config, storage=storage, smtp=smtp, teams=teams, flow="daily",
        p1_strategy="digest",
    )
    assert len(list((tmp_path / "outbox").glob("*.eml"))) == 1


def test_run_pastein_end_to_end(config, storage, notifiers, tmp_path):
    smtp, teams = notifiers
    llm = FakeLLM([_fake_response(_items_to_jsonl([_p0_item()]))])

    result = run_pastein(
        "Customer told us Jamf is acquiring Y for $200M. Feels P0.",
        config=config, llm=llm, storage=storage, smtp=smtp, teams=teams,
    )
    assert result.briefs_persisted == 1
    assert result.by_bucket["P0"] == 1
    assert result.p0_emails_sent == 1
    assert result.p0_teams_sent == 1
    assert llm.calls[0]["system"]
    assert "tools" not in llm.calls[0]


def test_run_pastein_empty_content_returns_error(config, storage, notifiers):
    smtp, teams = notifiers
    result = run_pastein("   ", config=config, llm=FakeLLM([]), storage=storage, smtp=smtp, teams=teams)
    assert "empty content" in result.errors[0]


def test_run_pastein_handles_unknown_competitor(config, storage, notifiers):
    smtp, teams = notifiers
    bad = _p0_item()
    bad["competitor_id"] = "blackberry"
    llm = FakeLLM([_fake_response(_items_to_jsonl([bad]))])
    result = run_pastein("noise", config=config, llm=llm, storage=storage, smtp=smtp, teams=teams)
    assert result.briefs_unknown_competitor == 1
    assert result.briefs_persisted == 0


def test_run_pastein_handles_jsonl_diagnostics(config, storage, notifiers):
    smtp, teams = notifiers
    text = json.dumps(_p0_item()) + "\n{this is not json}\n" + json.dumps(_p2_item())
    llm = FakeLLM([_fake_response(text)])
    result = run_pastein("noise", config=config, llm=llm, storage=storage, smtp=smtp, teams=teams)
    assert result.briefs_persisted == 2
    assert len(result.parse_diagnostics) == 1


def test_run_daily_scan_routes_p0_and_digests_p1(config, storage, notifiers, tmp_path):
    smtp, teams = notifiers
    p1 = _p0_item()
    p1["headline"] = "Intune adjusts pricing slightly"
    p1["competitor_id"] = "intune"
    p1["url"] = "https://microsoft.com/intune-pricing"
    p1["dimensions"]["strategic_impact"] = 6
    p1["dimensions"]["sales_signal"] = 4
    p1["confidence_signal"] = "single"

    llm = FakeLLM([_fake_response(_items_to_jsonl([_p0_item(), p1, _p2_item()]), search_count=4)])
    result = run_daily_scan(config=config, llm=llm, storage=storage, smtp=smtp, teams=teams)

    assert result.search_count == 4
    assert result.briefs_total == 3
    assert result.by_bucket["P0"] >= 1
    assert result.p0_emails_sent >= 1
    assert result.p0_teams_sent >= 1
    assert result.p1_digest_sent is True

    kwargs = llm.calls[0]
    assert kwargs["tools"][0]["type"] == "web_search_20250305"
    assert kwargs["tools"][0]["max_uses"] == config.runtime.web_search.budgets.daily


def test_run_daily_scan_dedupes_repeat_runs(config, storage, notifiers):
    smtp, teams = notifiers
    text = _items_to_jsonl([_p0_item()])
    llm1 = FakeLLM([_fake_response(text)])
    r1 = run_daily_scan(config=config, llm=llm1, storage=storage, smtp=smtp, teams=teams)
    assert r1.by_bucket["P0"] == 1

    llm2 = FakeLLM([_fake_response(text)])
    r2 = run_daily_scan(config=config, llm=llm2, storage=storage, smtp=smtp, teams=teams)
    assert r2.briefs_total == 1
    assert r2.briefs_deduped == 1
    assert r2.briefs_persisted == 0


def test_run_hourly_sweep_only_routes_p0(config, storage, notifiers, tmp_path):
    smtp, teams = notifiers
    llm = FakeLLM([_fake_response(_items_to_jsonl([_p0_item(), _p2_item()]))])
    result = run_hourly_sweep(config=config, llm=llm, storage=storage, smtp=smtp, teams=teams)
    assert result.by_bucket["P0"] >= 1
    assert result.p0_emails_sent >= 1
    p1_eml = [p for p in (tmp_path / "outbox").glob("*.eml") if "Compete Daily" in p.read_text(errors="ignore")]
    assert p1_eml == []


def test_run_hourly_sweep_skips_adjacent_competitors_in_routing(config, storage, notifiers):
    smtp, teams = notifiers
    knox_p0 = _p2_item()
    knox_p0["competitor_id"] = "knox"
    knox_p0["dimensions"] = {"strategic_impact": 10, "sales_signal": 9, "roadmap_overlap": 8, "source_quality": 10}
    knox_p0["confidence_signal"] = "multi_source"
    knox_p0["published_at"] = datetime.now(UTC).date().isoformat()

    llm = FakeLLM([_fake_response(_items_to_jsonl([knox_p0]))])
    result = run_hourly_sweep(config=config, llm=llm, storage=storage, smtp=smtp, teams=teams)
    assert result.briefs_persisted == 0  # knox is adjacent and config excludes it from hourly


def test_run_sentiment_monthly_saves_snapshot_per_competitor(config, storage, notifiers):
    smtp, _ = notifiers
    sentiment = {
        "competitor_id": "PLACEHOLDER",
        "period_days": 30,
        "net_sentiment": 0.15,
        "volume": "medium",
        "themes": [{"label": "pricing", "polarity": "negative", "evidence": "users mention price hikes"}],
        "notable_quotes": [{"url": "https://reddit.com/r/sysadmin/x", "platform": "reddit", "text": "..."}],
        "sources": [{"url": "https://reddit.com/r/sysadmin/x", "platform": "reddit"}],
    }
    responses = []
    for c in config.competitors.competitors:
        data = dict(sentiment, competitor_id=c.id)
        responses.append(_fake_response(json.dumps(data)))
    llm = FakeLLM(responses)

    result = run_sentiment_monthly(config=config, llm=llm, storage=storage, smtp=smtp)
    assert result.snapshots_saved == len(config.competitors.competitors)
    assert result.digest_sent is True
    assert storage.query_sentiment(competitor_id="jamf")
