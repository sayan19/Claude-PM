"""Gong: call transcripts. Phase 3 stub."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

STUB_TAG = "[STUB]"
log = logging.getLogger(__name__)


@dataclass
class GongMention:
    competitor_id: str
    call_id: str
    speaker_role: str
    snippet: str
    occurred_at: datetime


def get_recent_mentions(competitor_id: str, *, since_days: int = 30) -> list[GongMention]:
    """Return recent Gong call transcript mentions of the competitor.

    Phase 3 wire-in: replace with Gong API call (POST /v2/calls/transcript).
    """
    log.warning("%s gong.get_recent_mentions(%s, since_days=%s)", STUB_TAG, competitor_id, since_days)
    return [
        GongMention(
            competitor_id=competitor_id,
            call_id=f"{STUB_TAG}-call-1",
            speaker_role="prospect",
            snippet=f"{STUB_TAG} Gong not connected.",
            occurred_at=datetime.now(UTC) - timedelta(days=3),
        )
    ]


__all__ = ["GongMention", "get_recent_mentions"]
