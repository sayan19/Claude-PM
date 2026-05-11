from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest

from soti_compete.storage import Brief, SentimentSnapshot, SQLiteStorage


@pytest.fixture
def storage(tmp_path):
    return SQLiteStorage(tmp_path / "test.db")


def _brief(
    bid: str = "b1",
    bucket: str = "P0",
    competitor_id: str = "jamf",
    title: str = "Jamf launches X",
    created_at: datetime | None = None,
    flow: str = "daily",
    url: str = "https://example.com/a",
) -> Brief:
    return Brief(
        id=bid,
        url=url,
        url_fingerprint="fp" + bid,
        title=title,
        competitor_id=competitor_id,
        news_type="feature_launch",
        response_type="initiative",
        confidence_signal="multi_source",
        bucket=bucket,
        raw_score=7.8,
        recency_multiplier=1.0,
        confidence_multiplier=1.0,
        final_score=7.8,
        dimensions={"strategic_impact": 8, "sales_signal": 5,
                    "roadmap_overlap": 7, "competitor_tier": 10, "source_quality": 8},
        summary="A summary",
        gap_analysis={"soti_today": "supports X partially", "roadmap": "[STUB] Jira not connected"},
        sources=[{"url": "https://jamf.com/pr", "domain": "jamf.com"}],
        flow=flow,
        raw_payload={"score": 7.8},
        created_at=created_at or datetime.now(UTC),
    )


def test_save_and_get_roundtrip(storage):
    b = _brief()
    storage.save_brief(b)
    got = storage.get_brief("b1")
    assert got is not None
    assert got.title == b.title
    assert got.bucket == "P0"
    assert got.dimensions["strategic_impact"] == 8
    assert got.sources == b.sources
    assert got.gap_analysis == b.gap_analysis


def test_get_missing_returns_none(storage):
    assert storage.get_brief("nope") is None


def test_query_by_bucket(storage):
    storage.save_brief(_brief("a", bucket="P0"))
    storage.save_brief(_brief("b", bucket="P1"))
    storage.save_brief(_brief("c", bucket="P0"))
    p0 = storage.query_briefs(bucket="P0")
    assert {x.id for x in p0} == {"a", "c"}


def test_query_by_competitor(storage):
    storage.save_brief(_brief("a", competitor_id="jamf"))
    storage.save_brief(_brief("b", competitor_id="intune"))
    out = storage.query_briefs(competitor_id="intune")
    assert {x.id for x in out} == {"b"}


def test_query_by_flow(storage):
    storage.save_brief(_brief("a", flow="daily"))
    storage.save_brief(_brief("b", flow="hourly"))
    out = storage.query_briefs(flow="hourly")
    assert [x.id for x in out] == ["b"]


def test_query_by_time_range(storage):
    now = datetime.now(UTC)
    storage.save_brief(_brief("old", created_at=now - timedelta(days=10)))
    storage.save_brief(_brief("new", created_at=now))
    out = storage.query_briefs(since=now - timedelta(days=1))
    assert [x.id for x in out] == ["new"]


def test_query_order_desc(storage):
    now = datetime.now(UTC)
    storage.save_brief(_brief("first", created_at=now - timedelta(days=2)))
    storage.save_brief(_brief("second", created_at=now - timedelta(days=1)))
    storage.save_brief(_brief("third", created_at=now))
    out = storage.query_briefs()
    assert [x.id for x in out] == ["third", "second", "first"]


def test_upsert_on_duplicate_id(storage):
    storage.save_brief(_brief("dup", bucket="P1"))
    storage.save_brief(_brief("dup", bucket="P0"))
    got = storage.get_brief("dup")
    assert got.bucket == "P0"
    assert len(storage.query_briefs()) == 1


def test_recent_seen_items(storage):
    now = datetime.now(UTC)
    storage.save_brief(_brief("a", created_at=now))
    storage.save_brief(_brief("b", created_at=now - timedelta(days=45)))
    seen = storage.recent_seen_items(days=30)
    assert len(seen) == 1
    assert seen[0].url_fingerprint == "fpa"
    assert seen[0].competitor_id == "jamf"


def test_sentiment_save_and_query(storage):
    now = datetime.now(UTC)
    snap = SentimentSnapshot(
        id="s1",
        competitor_id="jamf",
        period_start=now - timedelta(days=30),
        period_end=now,
        summary={"net_sentiment": 0.42, "themes": ["pricing", "support"]},
        sources=[{"platform": "reddit", "url": "https://reddit.com/r/sysadmin/x"}],
        created_at=now,
    )
    storage.save_sentiment(snap)
    got = storage.query_sentiment(competitor_id="jamf")
    assert len(got) == 1
    assert got[0].summary["net_sentiment"] == 0.42


def test_ping(storage):
    assert storage.ping() is True
