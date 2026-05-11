from __future__ import annotations

from soti_compete.classify import (
    ConfidenceSignal,
    NewsType,
    ResponseType,
    coerce_confidence,
    coerce_news_type,
    coerce_response_type,
    is_acquisition,
)


def test_response_type_known():
    assert coerce_response_type("obligation") == ResponseType.OBLIGATION
    assert coerce_response_type("INITIATIVE") == ResponseType.INITIATIVE
    assert coerce_response_type("  housekeeping  ") == ResponseType.HOUSEKEEPING


def test_response_type_unknown_falls_back():
    assert coerce_response_type("garbage") == ResponseType.HOUSEKEEPING
    assert coerce_response_type(None) == ResponseType.HOUSEKEEPING
    assert coerce_response_type("") == ResponseType.HOUSEKEEPING


def test_news_type_known():
    assert coerce_news_type("acquisition") == NewsType.ACQUISITION
    assert coerce_news_type("FEATURE_LAUNCH") == NewsType.FEATURE_LAUNCH


def test_news_type_unknown():
    assert coerce_news_type("merger") is None
    assert coerce_news_type(None) is None
    assert coerce_news_type("") is None


def test_confidence_signals():
    assert coerce_confidence("multi_source") == ConfidenceSignal.MULTI_SOURCE
    assert coerce_confidence("RUMOR") == ConfidenceSignal.RUMOR
    assert coerce_confidence("garbage") == ConfidenceSignal.SINGLE
    assert coerce_confidence(None) == ConfidenceSignal.SINGLE


def test_is_acquisition():
    assert is_acquisition(NewsType.ACQUISITION) is True
    assert is_acquisition("acquisition") is True
    assert is_acquisition("ACQUISITION") is True
    assert is_acquisition(NewsType.FEATURE_LAUNCH) is False
    assert is_acquisition(None) is False
    assert is_acquisition("merger") is False
