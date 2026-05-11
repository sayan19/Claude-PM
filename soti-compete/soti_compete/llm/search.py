"""Web-search tool wiring + per-run budget.

The Anthropic web_search tool is server-side. We configure it with
allowed/blocked domains and a hard `max_uses` cap, then track actual usage
across multiple model calls inside a single flow run.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

log = logging.getLogger(__name__)

WEB_SEARCH_TOOL_TYPE = "web_search_20250305"


class BudgetExceededError(RuntimeError):
    pass


@dataclass
class WebSearchBudget:
    """Tracks web_search usage across LLM calls in one flow run."""

    limit: int
    used: int = 0

    @property
    def remaining(self) -> int:
        return max(0, self.limit - self.used)

    def can_search(self, want: int = 1) -> bool:
        return self.used + want <= self.limit

    def record(self, count: int) -> None:
        self.used += count
        if self.used > self.limit:
            log.warning("web_search budget exceeded: used=%s limit=%s", self.used, self.limit)


def build_web_search_tool(
    *,
    max_uses: int,
    allowed_domains: list[str] | None = None,
    blocked_domains: list[str] | None = None,
) -> dict[str, Any]:
    tool: dict[str, Any] = {
        "type": WEB_SEARCH_TOOL_TYPE,
        "name": "web_search",
        "max_uses": max(1, int(max_uses)),
    }
    if allowed_domains:
        tool["allowed_domains"] = list(dict.fromkeys(allowed_domains))
    if blocked_domains:
        tool["blocked_domains"] = list(dict.fromkeys(blocked_domains))
    return tool


__all__ = [
    "BudgetExceededError",
    "WEB_SEARCH_TOOL_TYPE",
    "WebSearchBudget",
    "build_web_search_tool",
]
