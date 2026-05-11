"""Salesforce: competitor-loss field. Phase 3 stub."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

STUB_TAG = "[STUB]"
log = logging.getLogger(__name__)


@dataclass
class CompetitorLoss:
    competitor_id: str
    account_name: str
    deal_size_usd: float | None
    closed_at: datetime
    notes: str


def get_competitor_losses(competitor_id: str, *, since_days: int = 90) -> list[CompetitorLoss]:
    """Return closed-lost opportunities attributed to a competitor.

    Phase 3 wire-in: replace with Salesforce REST/Bulk API call.
    """
    log.warning("%s salesforce.get_competitor_losses(%s, since_days=%s)", STUB_TAG, competitor_id, since_days)
    return [
        CompetitorLoss(
            competitor_id=competitor_id,
            account_name=f"{STUB_TAG} ACME Corp",
            deal_size_usd=None,
            closed_at=datetime.now(UTC) - timedelta(days=14),
            notes=f"{STUB_TAG} Salesforce not connected. Replace with live data.",
        )
    ]


__all__ = ["CompetitorLoss", "get_competitor_losses"]
