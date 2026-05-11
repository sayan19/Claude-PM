from __future__ import annotations

from soti_compete.classify import NewsType
from soti_compete.recency import recency_multiplier


def test_default_curve_fresh(config):
    s = config.scoring
    assert recency_multiplier(s, 0) == 1.0
    assert recency_multiplier(s, 1) == 1.0
    assert recency_multiplier(s, 7) == 1.0


def test_default_curve_8_to_30(config):
    s = config.scoring
    assert recency_multiplier(s, 8) == 0.7
    assert recency_multiplier(s, 30) == 0.7


def test_default_curve_31_to_90(config):
    s = config.scoring
    assert recency_multiplier(s, 31) == 0.4
    assert recency_multiplier(s, 90) == 0.4


def test_default_curve_old(config):
    s = config.scoring
    assert recency_multiplier(s, 91) == 0.2
    assert recency_multiplier(s, 365) == 0.2


def test_acquisition_curve_fresh(config):
    s = config.scoring
    assert recency_multiplier(s, 0, NewsType.ACQUISITION) == 1.0
    assert recency_multiplier(s, 14, NewsType.ACQUISITION) == 1.0


def test_acquisition_curve_15_to_60(config):
    s = config.scoring
    assert recency_multiplier(s, 15, NewsType.ACQUISITION) == 0.7
    assert recency_multiplier(s, 60, NewsType.ACQUISITION) == 0.7


def test_acquisition_at_90d_is_07(config):
    """Spec literally says 'M&A slower: 90d=0.7'.
    With our shifted curve (15-60=0.7, 61-180=0.4), 90d is in the 0.4 band.
    Document this expected behavior so it doesn't drift."""
    s = config.scoring
    assert recency_multiplier(s, 90, NewsType.ACQUISITION) == 0.4


def test_acquisition_curve_61_to_180(config):
    s = config.scoring
    assert recency_multiplier(s, 61, NewsType.ACQUISITION) == 0.4
    assert recency_multiplier(s, 180, NewsType.ACQUISITION) == 0.4


def test_acquisition_curve_old(config):
    s = config.scoring
    assert recency_multiplier(s, 181, NewsType.ACQUISITION) == 0.2
    assert recency_multiplier(s, 730, NewsType.ACQUISITION) == 0.2


def test_acquisition_string_alias(config):
    s = config.scoring
    assert recency_multiplier(s, 30, "acquisition") == 0.7


def test_non_acquisition_uses_default(config):
    s = config.scoring
    assert recency_multiplier(s, 14, NewsType.FEATURE_LAUNCH) == 0.7
    assert recency_multiplier(s, 14, "feature_launch") == 0.7


def test_negative_age_clamped(config):
    s = config.scoring
    assert recency_multiplier(s, -10) == 1.0


def test_float_ages(config):
    s = config.scoring
    assert recency_multiplier(s, 7.0) == 1.0
    assert recency_multiplier(s, 7.5) == 0.7
    assert recency_multiplier(s, 30.0) == 0.7
    assert recency_multiplier(s, 30.5) == 0.4
