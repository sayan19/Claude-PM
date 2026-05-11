from __future__ import annotations

from soti_compete.llm.search import (
    WEB_SEARCH_TOOL_TYPE,
    WebSearchBudget,
    build_web_search_tool,
)


def test_build_minimal():
    t = build_web_search_tool(max_uses=5)
    assert t["type"] == WEB_SEARCH_TOOL_TYPE
    assert t["name"] == "web_search"
    assert t["max_uses"] == 5
    assert "allowed_domains" not in t
    assert "blocked_domains" not in t


def test_build_with_allow_and_block():
    t = build_web_search_tool(
        max_uses=10,
        allowed_domains=["bloomberg.com", "reuters.com"],
        blocked_domains=["pinterest.com"],
    )
    assert t["allowed_domains"] == ["bloomberg.com", "reuters.com"]
    assert t["blocked_domains"] == ["pinterest.com"]


def test_build_dedupes_domains_preserving_order():
    t = build_web_search_tool(
        max_uses=3,
        allowed_domains=["bloomberg.com", "reuters.com", "bloomberg.com"],
    )
    assert t["allowed_domains"] == ["bloomberg.com", "reuters.com"]


def test_max_uses_minimum_is_1():
    t = build_web_search_tool(max_uses=0)
    assert t["max_uses"] == 1


def test_budget_initial_state():
    b = WebSearchBudget(limit=5)
    assert b.used == 0
    assert b.remaining == 5
    assert b.can_search(1) is True
    assert b.can_search(5) is True
    assert b.can_search(6) is False


def test_budget_record():
    b = WebSearchBudget(limit=5)
    b.record(2)
    assert b.used == 2
    assert b.remaining == 3
    b.record(3)
    assert b.remaining == 0
    assert b.can_search(1) is False


def test_budget_record_over_does_not_crash():
    b = WebSearchBudget(limit=5)
    b.record(10)
    assert b.used == 10
    assert b.remaining == 0
