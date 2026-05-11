from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from typing import Any

from soti_compete.config import Bucket
from soti_compete.dedup import SeenItem


@dataclass
class Brief:
    id: str
    url: str
    url_fingerprint: str
    title: str
    competitor_id: str | None
    news_type: str | None
    response_type: str
    confidence_signal: str
    bucket: Bucket
    raw_score: float
    recency_multiplier: float
    confidence_multiplier: float
    final_score: float
    dimensions: dict[str, float]
    summary: str = ""
    gap_analysis: dict[str, Any] = field(default_factory=dict)
    sources: list[dict[str, Any]] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    flow: str = "daily"
    raw_payload: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["created_at"] = self.created_at.astimezone(UTC).isoformat()
        return d


@dataclass
class SentimentSnapshot:
    id: str
    competitor_id: str
    period_start: datetime
    period_end: datetime
    summary: dict[str, Any]
    sources: list[dict[str, Any]] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


class Storage(ABC):
    @abstractmethod
    def save_brief(self, brief: Brief) -> None: ...

    @abstractmethod
    def get_brief(self, brief_id: str) -> Brief | None: ...

    @abstractmethod
    def query_briefs(
        self,
        *,
        since: datetime | None = None,
        until: datetime | None = None,
        bucket: Bucket | None = None,
        competitor_id: str | None = None,
        flow: str | None = None,
        limit: int = 200,
    ) -> list[Brief]: ...

    @abstractmethod
    def recent_seen_items(self, days: int) -> list[SeenItem]: ...

    @abstractmethod
    def save_sentiment(self, snapshot: SentimentSnapshot) -> None: ...

    @abstractmethod
    def query_sentiment(
        self,
        *,
        competitor_id: str | None = None,
        since: datetime | None = None,
        limit: int = 100,
    ) -> list[SentimentSnapshot]: ...

    @abstractmethod
    def ping(self) -> bool: ...


__all__ = ["Brief", "SentimentSnapshot", "Storage"]
