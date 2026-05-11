"""Pure scoring math. No I/O. Inputs are dimension scores + classifications."""

from __future__ import annotations

from dataclasses import dataclass, field

from soti_compete.classify import ConfidenceSignal, NewsType, coerce_confidence
from soti_compete.config import Bucket, ScoringConfig, Tier
from soti_compete.recency import recency_multiplier


@dataclass(frozen=True)
class DimensionScores:
    strategic_impact: float
    sales_signal: float
    roadmap_overlap: float
    competitor_tier: float
    source_quality: float

    def clamped(self) -> DimensionScores:
        return DimensionScores(
            strategic_impact=_clamp(self.strategic_impact),
            sales_signal=_clamp(self.sales_signal),
            roadmap_overlap=_clamp(self.roadmap_overlap),
            competitor_tier=_clamp(self.competitor_tier),
            source_quality=_clamp(self.source_quality),
        )


@dataclass(frozen=True)
class ScoringResult:
    raw: float
    recency: float
    confidence: float
    final: float
    bucket: Bucket
    breakdown: dict[str, float] = field(default_factory=dict)


def _clamp(x: float, lo: float = 0.0, hi: float = 10.0) -> float:
    return max(lo, min(hi, float(x)))


def tier_score(scoring: ScoringConfig, tier: Tier) -> int:
    return scoring.tier_scores[tier]


def source_quality_score(scoring: ScoringConfig, source_class: str) -> int:
    return scoring.source_quality_scores.get(source_class, scoring.source_quality_scores["blog"])


def raw_score(scoring: ScoringConfig, dims: DimensionScores) -> float:
    d = dims.clamped()
    w = scoring.weights
    raw = (
        d.strategic_impact * w.strategic_impact
        + d.sales_signal * w.sales_signal
        + d.roadmap_overlap * w.roadmap_overlap
        + d.competitor_tier * w.competitor_tier
        + d.source_quality * w.source_quality
    ) / 100.0
    return _clamp(raw)


def confidence_multiplier(scoring: ScoringConfig, signal: ConfidenceSignal | str) -> float:
    key = coerce_confidence(signal if isinstance(signal, str) else signal.value).value
    return float(scoring.confidence[key])


def score(
    scoring: ScoringConfig,
    dims: DimensionScores,
    age_days: float,
    news_type: NewsType | str | None,
    confidence_signal: ConfidenceSignal | str,
) -> ScoringResult:
    raw = raw_score(scoring, dims)
    rec = recency_multiplier(scoring, age_days, news_type)
    conf = confidence_multiplier(scoring, confidence_signal)
    final = _clamp(raw * rec * conf)
    return ScoringResult(
        raw=raw,
        recency=rec,
        confidence=conf,
        final=final,
        bucket=scoring.bucket_for(final),
        breakdown={
            "strategic_impact": dims.clamped().strategic_impact,
            "sales_signal": dims.clamped().sales_signal,
            "roadmap_overlap": dims.clamped().roadmap_overlap,
            "competitor_tier": dims.clamped().competitor_tier,
            "source_quality": dims.clamped().source_quality,
        },
    )


__all__ = [
    "DimensionScores",
    "ScoringResult",
    "confidence_multiplier",
    "raw_score",
    "score",
    "source_quality_score",
    "tier_score",
]
