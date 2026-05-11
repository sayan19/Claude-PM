from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

from soti_compete.llm.client import LLMClient, _parse_response


def _block(type_: str, **kw) -> SimpleNamespace:
    return SimpleNamespace(type=type_, **kw)


def _fake_msg(content: list, stop_reason: str = "end_turn") -> SimpleNamespace:
    return SimpleNamespace(content=content, stop_reason=stop_reason)


def test_complete_passes_through_args():
    fake = MagicMock()
    fake.messages.create.return_value = _fake_msg(
        [_block("text", text="hello", citations=None)]
    )
    client = LLMClient(model="claude-sonnet-4-6", max_tokens=2048, anthropic_client=fake)

    out = client.complete(system="sys", user="hi")

    fake.messages.create.assert_called_once()
    kwargs = fake.messages.create.call_args.kwargs
    assert kwargs["model"] == "claude-sonnet-4-6"
    assert kwargs["max_tokens"] == 2048
    assert kwargs["system"] == "sys"
    assert kwargs["messages"] == [{"role": "user", "content": "hi"}]
    assert "tools" not in kwargs
    assert out.text == "hello"


def test_complete_with_tools_and_override():
    fake = MagicMock()
    fake.messages.create.return_value = _fake_msg([_block("text", text="ok", citations=None)])
    client = LLMClient(model="m", max_tokens=2048, anthropic_client=fake)

    tools = [{"type": "web_search_20250305", "name": "web_search", "max_uses": 3}]
    client.complete(system="s", user="u", tools=tools, max_tokens=512)

    kwargs = fake.messages.create.call_args.kwargs
    assert kwargs["max_tokens"] == 512
    assert kwargs["tools"] == tools


def test_parse_concatenates_text_blocks():
    msg = _fake_msg([
        _block("text", text="line1\n", citations=None),
        _block("text", text="line2", citations=None),
    ])
    r = _parse_response(msg)
    assert r.text == "line1\n\nline2"


def test_parse_counts_server_tool_use_web_search():
    msg = _fake_msg([
        _block("server_tool_use", name="web_search", id="x1"),
        _block("server_tool_use", name="web_search", id="x2"),
        _block("server_tool_use", name="other_tool", id="x3"),
        _block("text", text="done", citations=None),
    ])
    r = _parse_response(msg)
    assert r.search_count == 2


def test_parse_collects_citations_from_text_blocks():
    cit = SimpleNamespace(url="https://jamf.com/pr", title="Jamf PR", cited_text="…")
    msg = _fake_msg([
        _block("text", text="something", citations=[cit]),
    ])
    r = _parse_response(msg)
    assert len(r.citations) == 1
    assert r.citations[0].url == "https://jamf.com/pr"


def test_parse_collects_citations_from_search_result_blocks():
    result_a = SimpleNamespace(url="https://reuters.com/x", title="R", page_age=None)
    result_b = SimpleNamespace(url="https://wsj.com/y", title="W", page_age=None)
    msg = _fake_msg([
        _block("web_search_tool_result", content=[result_a, result_b]),
        _block("text", text="ok", citations=None),
    ])
    r = _parse_response(msg)
    urls = {c.url for c in r.citations}
    assert urls == {"https://reuters.com/x", "https://wsj.com/y"}


def test_parse_dedupes_citations():
    cit = SimpleNamespace(url="https://jamf.com/pr", title="Jamf PR", cited_text="…")
    result = SimpleNamespace(url="https://jamf.com/pr", title="dup", page_age=None)
    msg = _fake_msg([
        _block("text", text="a", citations=[cit]),
        _block("web_search_tool_result", content=[result]),
    ])
    r = _parse_response(msg)
    assert len(r.citations) == 1


def test_parse_handles_dict_blocks():
    msg = SimpleNamespace(
        content=[
            {"type": "text", "text": "hi", "citations": []},
            {"type": "server_tool_use", "name": "web_search"},
        ],
        stop_reason="end_turn",
    )
    r = _parse_response(msg)
    assert r.text == "hi"
    assert r.search_count == 1


def test_parse_empty_content():
    msg = _fake_msg([])
    r = _parse_response(msg)
    assert r.text == ""
    assert r.search_count == 0
    assert r.citations == []


def test_parse_propagates_stop_reason():
    msg = _fake_msg([_block("text", text="x", citations=None)], stop_reason="max_tokens")
    r = _parse_response(msg)
    assert r.stop_reason == "max_tokens"
