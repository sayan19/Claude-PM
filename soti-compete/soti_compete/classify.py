from __future__ import annotations

from enum import StrEnum


class ResponseType(StrEnum):
    OBLIGATION = "obligation"
    INITIATIVE = "initiative"
    HOUSEKEEPING = "housekeeping"


class NewsType(StrEnum):
    ACQUISITION = "acquisition"
    FEATURE_LAUNCH = "feature_launch"
    PRICING = "pricing"
    EXEC_CHANGE = "exec_change"
    CUSTOMER_WIN = "customer_win"
    CUSTOMER_LOSS = "customer_loss"
    PARTNERSHIP = "partnership"
    SECURITY = "security"
    REGULATORY = "regulatory"
    ANALYST = "analyst"


class ConfidenceSignal(StrEnum):
    MULTI_SOURCE = "multi_source"
    SINGLE_TIER1 = "single_tier1"
    SINGLE = "single"
    RUMOR = "rumor"


def coerce_response_type(value: str | None) -> ResponseType:
    if not value:
        return ResponseType.HOUSEKEEPING
    try:
        return ResponseType(value.strip().lower())
    except ValueError:
        return ResponseType.HOUSEKEEPING


def coerce_news_type(value: str | None) -> NewsType | None:
    if not value:
        return None
    try:
        return NewsType(value.strip().lower())
    except ValueError:
        return None


def coerce_confidence(value: str | None) -> ConfidenceSignal:
    if not value:
        return ConfidenceSignal.SINGLE
    try:
        return ConfidenceSignal(value.strip().lower())
    except ValueError:
        return ConfidenceSignal.SINGLE


def is_acquisition(news_type: NewsType | str | None) -> bool:
    if isinstance(news_type, str):
        news_type = coerce_news_type(news_type)
    return news_type == NewsType.ACQUISITION


__all__ = [
    "ConfidenceSignal",
    "NewsType",
    "ResponseType",
    "coerce_confidence",
    "coerce_news_type",
    "coerce_response_type",
    "is_acquisition",
]
