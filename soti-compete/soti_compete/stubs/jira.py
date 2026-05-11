"""Jira / Productboard: roadmap overlap. Phase 3 stub."""

from __future__ import annotations

import logging
from dataclasses import dataclass

STUB_TAG = "[STUB]"
log = logging.getLogger(__name__)


@dataclass
class RoadmapItem:
    key: str
    title: str
    status: str
    target_release: str | None


def get_roadmap_overlap(*, news_type: str | None = None, keywords: list[str] | None = None) -> list[RoadmapItem]:
    """Return SOTI roadmap items overlapping with a piece of competitive news.

    Phase 3 wire-in: query Jira via JQL or Productboard via REST.
    """
    log.warning("%s jira.get_roadmap_overlap(news_type=%s, keywords=%s)", STUB_TAG, news_type, keywords)
    return [
        RoadmapItem(
            key=f"{STUB_TAG}-PRD-0",
            title=f"{STUB_TAG} Jira/Productboard not connected.",
            status="unknown",
            target_release=None,
        )
    ]


__all__ = ["RoadmapItem", "get_roadmap_overlap"]
