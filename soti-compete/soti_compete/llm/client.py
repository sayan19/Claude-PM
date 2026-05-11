"""Thin Anthropic SDK wrapper.

Tests inject a fake `anthropic_client` so the real API is never called.
Production code constructs an `anthropic.Anthropic()` lazily.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from typing import Any

log = logging.getLogger(__name__)


@dataclass
class Citation:
    url: str
    title: str = ""
    cited_text: str = ""


@dataclass
class LLMResponse:
    text: str
    search_count: int = 0
    citations: list[Citation] = field(default_factory=list)
    stop_reason: str | None = None
    raw: Any = None


class LLMClient:
    def __init__(
        self,
        *,
        model: str,
        max_tokens: int,
        api_key: str | None = None,
        anthropic_client: Any | None = None,
    ):
        self.model = model
        self.max_tokens = max_tokens
        if anthropic_client is not None:
            self._client = anthropic_client
        else:
            import anthropic
            self._client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))

    def complete(
        self,
        *,
        system: str,
        user: str,
        tools: list[dict[str, Any]] | None = None,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        kwargs: dict[str, Any] = {
            "model": self.model,
            "max_tokens": max_tokens or self.max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }
        if tools:
            kwargs["tools"] = tools

        log.debug("anthropic.messages.create model=%s tools=%s", self.model, [t.get("name") for t in (tools or [])])
        msg = self._client.messages.create(**kwargs)
        return _parse_response(msg)


def _block_attr(block: Any, name: str, default: Any = None) -> Any:
    if isinstance(block, dict):
        return block.get(name, default)
    return getattr(block, name, default)


def _parse_response(msg: Any) -> LLMResponse:
    content = _block_attr(msg, "content", []) or []
    text_parts: list[str] = []
    search_count = 0
    citations: list[Citation] = []

    for block in content:
        btype = _block_attr(block, "type")
        if btype == "text":
            text_parts.append(_block_attr(block, "text", "") or "")
            for c in _block_attr(block, "citations", []) or []:
                citations.append(
                    Citation(
                        url=_block_attr(c, "url", "") or "",
                        title=_block_attr(c, "title", "") or "",
                        cited_text=_block_attr(c, "cited_text", "") or "",
                    )
                )
        elif btype == "server_tool_use":
            if _block_attr(block, "name") == "web_search":
                search_count += 1
        elif btype == "web_search_tool_result":
            for r in _block_attr(block, "content", []) or []:
                url = _block_attr(r, "url", "")
                if url:
                    citations.append(
                        Citation(
                            url=url,
                            title=_block_attr(r, "title", "") or "",
                        )
                    )

    return LLMResponse(
        text="\n".join(p for p in text_parts if p),
        search_count=search_count,
        citations=_dedupe_citations(citations),
        stop_reason=_block_attr(msg, "stop_reason"),
        raw=msg,
    )


def _dedupe_citations(items: list[Citation]) -> list[Citation]:
    seen: set[str] = set()
    out: list[Citation] = []
    for c in items:
        if c.url and c.url not in seen:
            seen.add(c.url)
            out.append(c)
    return out


__all__ = ["Citation", "LLMClient", "LLMResponse"]
