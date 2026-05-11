from __future__ import annotations

from soti_compete.classify import NewsType, is_acquisition
from soti_compete.config import ScoringConfig


def recency_multiplier(
    scoring: ScoringConfig,
    age_days: float,
    news_type: NewsType | str | None = None,
) -> float:
    if age_days < 0:
        age_days = 0.0
    curve_key = "acquisition" if is_acquisition(news_type) else "default"
    curve = scoring.recency.get(curve_key) or scoring.recency["default"]
    for step in curve:
        if step.max_days is None or age_days <= step.max_days:
            return step.multiplier
    return curve[-1].multiplier


__all__ = ["recency_multiplier"]
