from __future__ import annotations

import pytest

from soti_compete.classify import ConfidenceSignal, NewsType
from soti_compete.scoring import (
    DimensionScores,
    confidence_multiplier,
    raw_score,
    score,
    source_quality_score,
    tier_score,
)


def test_tier_scores(config):
    assert tier_score(config.scoring, "direct") == 10
    assert tier_score(config.scoring, "adjacent") == 6


def test_source_quality_known(config):
    s = config.scoring
    assert source_quality_score(s, "sec_filing") == 10
    assert source_quality_score(s, "vendor_press") == 10
    assert source_quality_score(s, "analyst") == 10
    assert source_quality_score(s, "tier_1_press") == 8
    assert source_quality_score(s, "secondary_press") == 5
    assert source_quality_score(s, "blog") == 2
    assert source_quality_score(s, "forum") == 2


def test_source_quality_unknown_falls_back_to_blog(config):
    assert source_quality_score(config.scoring, "unknown_class") == 2


def test_raw_score_max_is_10(config):
    dims = DimensionScores(10, 10, 10, 10, 10)
    assert raw_score(config.scoring, dims) == pytest.approx(10.0)


def test_raw_score_min_is_0(config):
    dims = DimensionScores(0, 0, 0, 0, 0)
    assert raw_score(config.scoring, dims) == 0.0


def test_raw_score_clamps_above_10(config):
    dims = DimensionScores(15, 15, 15, 15, 15)
    assert raw_score(config.scoring, dims) == 10.0


def test_raw_score_clamps_negative(config):
    dims = DimensionScores(-3, 5, 5, 5, 5)
    assert raw_score(config.scoring, dims) == pytest.approx(
        (0 * 30 + 5 * 25 + 5 * 20 + 5 * 15 + 5 * 10) / 100
    )


def test_raw_score_weighted_math(config):
    dims = DimensionScores(
        strategic_impact=8,
        sales_signal=5,
        roadmap_overlap=6,
        competitor_tier=10,
        source_quality=8,
    )
    expected = (8 * 30 + 5 * 25 + 6 * 20 + 10 * 15 + 8 * 10) / 100
    assert raw_score(config.scoring, dims) == pytest.approx(expected)


def test_confidence_multipliers(config):
    s = config.scoring
    assert confidence_multiplier(s, ConfidenceSignal.MULTI_SOURCE) == 1.0
    assert confidence_multiplier(s, ConfidenceSignal.SINGLE_TIER1) == 1.0
    assert confidence_multiplier(s, ConfidenceSignal.SINGLE) == 0.8
    assert confidence_multiplier(s, ConfidenceSignal.RUMOR) == 0.5
    assert confidence_multiplier(s, "rumor") == 0.5


def test_score_p0_fresh_high(config):
    dims = DimensionScores(
        strategic_impact=9, sales_signal=8, roadmap_overlap=8,
        competitor_tier=10, source_quality=10,
    )
    r = score(config.scoring, dims, age_days=2, news_type=None,
              confidence_signal=ConfidenceSignal.MULTI_SOURCE)
    assert r.bucket == "P0"
    assert r.recency == 1.0
    assert r.confidence == 1.0
    assert r.final == r.raw


def test_score_recency_drops_to_p1(config):
    dims = DimensionScores(
        strategic_impact=9, sales_signal=8, roadmap_overlap=8,
        competitor_tier=10, source_quality=10,
    )
    r = score(config.scoring, dims, age_days=20, news_type=NewsType.FEATURE_LAUNCH,
              confidence_signal=ConfidenceSignal.MULTI_SOURCE)
    assert r.recency == 0.7
    assert r.bucket in {"P0", "P1"}


def test_score_rumor_demotes(config):
    dims = DimensionScores(
        strategic_impact=9, sales_signal=8, roadmap_overlap=8,
        competitor_tier=10, source_quality=8,
    )
    r = score(config.scoring, dims, age_days=1, news_type=NewsType.FEATURE_LAUNCH,
              confidence_signal=ConfidenceSignal.RUMOR)
    assert r.confidence == 0.5
    assert r.final < r.raw


def test_score_bucket_drop_for_low(config):
    dims = DimensionScores(1, 1, 1, 6, 2)
    r = score(config.scoring, dims, age_days=100, news_type=NewsType.PARTNERSHIP,
              confidence_signal=ConfidenceSignal.SINGLE)
    assert r.bucket == "DROP"


def test_score_negative_age_treated_as_zero(config):
    dims = DimensionScores(8, 6, 6, 10, 8)
    r = score(config.scoring, dims, age_days=-5, news_type=None,
              confidence_signal=ConfidenceSignal.MULTI_SOURCE)
    assert r.recency == 1.0


def test_bucket_boundaries(config):
    s = config.scoring
    assert s.bucket_for(7.5) == "P0"
    assert s.bucket_for(7.4999) == "P1"
    assert s.bucket_for(5.0) == "P1"
    assert s.bucket_for(4.9999) == "P2"
    assert s.bucket_for(2.5) == "P2"
    assert s.bucket_for(2.4999) == "DROP"
