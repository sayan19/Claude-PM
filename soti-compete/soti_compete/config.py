from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, field_validator

Tier = Literal["direct", "adjacent"]
Bucket = Literal["P0", "P1", "P2", "DROP"]
ConfidenceKey = Literal["multi_source", "single_tier1", "single", "rumor"]


class Competitor(BaseModel):
    id: str
    name: str
    tier: Tier
    aliases: list[str] = []
    search_hints: list[str] = []


class CompetitorsConfig(BaseModel):
    competitors: list[Competitor]

    def by_id(self, cid: str) -> Competitor | None:
        return next((c for c in self.competitors if c.id == cid), None)

    def direct(self) -> list[Competitor]:
        return [c for c in self.competitors if c.tier == "direct"]


class RecencyStep(BaseModel):
    max_days: int | None
    multiplier: float


class WeightsConfig(BaseModel):
    strategic_impact: int
    sales_signal: int
    roadmap_overlap: int
    competitor_tier: int
    source_quality: int

    @field_validator("source_quality")
    @classmethod
    def _check_sum(cls, v: int, info) -> int:
        total = (
            info.data.get("strategic_impact", 0)
            + info.data.get("sales_signal", 0)
            + info.data.get("roadmap_overlap", 0)
            + info.data.get("competitor_tier", 0)
            + v
        )
        if total != 100:
            raise ValueError(f"weights must sum to 100, got {total}")
        return v


class BucketDef(BaseModel):
    name: Bucket
    min: float


class Phase1Defaults(BaseModel):
    sales_signal_no_deal_motion: int
    sales_signal_with_deal_motion: int
    roadmap_overlap_conservative: int


class ScoringConfig(BaseModel):
    weights: WeightsConfig
    tier_scores: dict[str, int]
    source_quality_scores: dict[str, int]
    phase_1_defaults: Phase1Defaults
    recency: dict[str, list[RecencyStep]]
    confidence: dict[str, float]
    buckets: list[BucketDef]
    news_types: list[str]
    response_types: list[str]

    def bucket_for(self, score: float) -> Bucket:
        for b in sorted(self.buckets, key=lambda x: -x.min):
            if score >= b.min:
                return b.name
        return "DROP"


class SourcesConfig(BaseModel):
    tier_1_press_domains: list[str]
    analyst_domains: list[str]
    sec_filing_domains: list[str]
    vendor_press_domains: dict[str, list[str]]
    blocked_domains: list[str] = []
    sentiment_sources: dict[str, dict]

    def classify_domain(self, domain: str, competitor_id: str | None = None) -> str:
        d = domain.lower().lstrip(".")
        if any(d.endswith(x) for x in self.sec_filing_domains):
            return "sec_filing"
        if competitor_id and any(
            d.endswith(x) for x in self.vendor_press_domains.get(competitor_id, [])
        ):
            return "vendor_press"
        if any(d.endswith(x) for x in self.analyst_domains):
            return "analyst"
        if any(d.endswith(x) for x in self.tier_1_press_domains):
            return "tier_1_press"
        return "secondary"


class EmailRoute(BaseModel):
    to: list[str] = []
    cc: list[str] = []
    subject_prefix: str = ""
    digest: bool = False
    digest_only: bool = False


class TeamsRoute(BaseModel):
    webhook_env: str | None = None
    title_prefix: str = ""
    enabled: bool = True


class RoutingConfig(BaseModel):
    email: dict[str, EmailRoute]
    teams: dict[str, TeamsRoute]


class ModelConfig(BaseModel):
    id: str
    max_tokens: int = 8192


class StorageConfig(BaseModel):
    backend: Literal["sqlite"]
    sqlite_path: str


class WebSearchBudgets(BaseModel):
    daily: int
    hourly: int
    sentiment_per_competitor: int
    pastein: int


class WebSearchConfig(BaseModel):
    budgets: WebSearchBudgets
    default_max_uses: int


class DedupConfig(BaseModel):
    title_similarity_threshold: int
    lookback_days: int


class HourlyFlowConfig(BaseModel):
    lookback_hours: int
    competitor_tiers: list[Tier]
    routed_buckets: list[Bucket]


class DailyFlowConfig(BaseModel):
    lookback_days: int


class SentimentFlowConfig(BaseModel):
    lookback_days: int


class FlowsConfig(BaseModel):
    daily: DailyFlowConfig
    hourly: HourlyFlowConfig
    sentiment: SentimentFlowConfig


class RuntimeConfig(BaseModel):
    model: ModelConfig
    timezone: str
    storage: StorageConfig
    web_search: WebSearchConfig
    dedup: DedupConfig
    flows: FlowsConfig


class Config(BaseModel):
    competitors: CompetitorsConfig
    scoring: ScoringConfig
    sources: SourcesConfig
    routing: RoutingConfig
    runtime: RuntimeConfig


def _read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top-level YAML must be a mapping")
    return data


def load_config(config_dir: str | os.PathLike | None = None) -> Config:
    base = Path(config_dir or os.environ.get("SOTI_COMPETE_CONFIG_DIR", "config"))
    if not base.is_dir():
        raise FileNotFoundError(f"config dir not found: {base}")

    required = ["competitors", "scoring", "sources", "routing", "runtime"]
    missing = [n for n in required if not (base / f"{n}.yaml").is_file()]
    if missing:
        raise FileNotFoundError(f"missing config files: {missing}")

    return Config(
        competitors=CompetitorsConfig(**_read_yaml(base / "competitors.yaml")),
        scoring=ScoringConfig(**_read_yaml(base / "scoring.yaml")),
        sources=SourcesConfig(**_read_yaml(base / "sources.yaml")),
        routing=RoutingConfig(**_read_yaml(base / "routing.yaml")),
        runtime=RuntimeConfig(**_read_yaml(base / "runtime.yaml")),
    )


def env_required(name: str) -> str:
    v = os.environ.get(name)
    if not v:
        raise RuntimeError(f"required env var not set: {name}")
    return v


def env_optional(name: str, default: str = "") -> str:
    return os.environ.get(name, default)


def is_dry_run() -> bool:
    return os.environ.get("SOTI_COMPETE_DRY_RUN", "").lower() in {"1", "true", "yes"}


def data_dir() -> Path:
    p = Path(os.environ.get("SOTI_COMPETE_DATA_DIR", "data"))
    p.mkdir(parents=True, exist_ok=True)
    return p


__all__ = [
    "Bucket",
    "Competitor",
    "CompetitorsConfig",
    "Config",
    "ConfidenceKey",
    "RoutingConfig",
    "ScoringConfig",
    "SourcesConfig",
    "RuntimeConfig",
    "Tier",
    "data_dir",
    "env_optional",
    "env_required",
    "is_dry_run",
    "load_config",
]
