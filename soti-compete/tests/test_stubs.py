from __future__ import annotations

import logging

from soti_compete.stubs import (
    get_competitor_losses,
    get_recent_mentions,
    get_roadmap_overlap,
)


def test_salesforce_stub_returns_placeholder_and_logs(caplog):
    with caplog.at_level(logging.WARNING):
        out = get_competitor_losses("jamf")
    assert out and "[STUB]" in out[0].notes
    assert any("[STUB]" in r.message for r in caplog.records)


def test_gong_stub_returns_placeholder_and_logs(caplog):
    with caplog.at_level(logging.WARNING):
        out = get_recent_mentions("intune")
    assert out and "[STUB]" in out[0].snippet
    assert any("[STUB]" in r.message for r in caplog.records)


def test_jira_stub_returns_placeholder_and_logs(caplog):
    with caplog.at_level(logging.WARNING):
        out = get_roadmap_overlap(news_type="feature_launch", keywords=["zero trust"])
    assert out and "[STUB]" in out[0].title
    assert any("[STUB]" in r.message for r in caplog.records)
