from __future__ import annotations

from soti_compete.jsonl import parse_jsonl


def test_empty_input():
    r = parse_jsonl("")
    assert r.records == []
    assert r.diagnostics == []


def test_whitespace_only():
    r = parse_jsonl("   \n\n   \t  \n")
    assert r.records == []


def test_basic_jsonl():
    text = '{"a": 1}\n{"a": 2}\n{"a": 3}'
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2, 3]
    assert r.diagnostics == []


def test_blank_lines_between():
    text = '{"a": 1}\n\n\n{"a": 2}\n'
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2]


def test_markdown_fences():
    text = '''Sure, here are the items:

```json
{"a": 1}
{"a": 2}
```

Hope that helps!'''
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2]


def test_jsonl_fence_label():
    text = '```jsonl\n{"a": 1}\n{"a": 2}\n```'
    r = parse_jsonl(text)
    assert len(r.records) == 2


def test_fence_without_language():
    text = '```\n{"a": 1}\n```'
    r = parse_jsonl(text)
    assert r.records == [{"a": 1}]


def test_prose_around_jsonl_no_fences():
    text = (
        "Here is what I found.\n"
        '{"a": 1, "title": "Jamf launches X"}\n'
        '{"a": 2, "title": "Intune pricing change"}\n'
        "That is all for now."
    )
    r = parse_jsonl(text)
    assert len(r.records) == 2


def test_trailing_commas_inside_object():
    text = '{"a": 1, "b": 2,}\n{"a": 3,}'
    r = parse_jsonl(text)
    assert r.records == [{"a": 1, "b": 2}, {"a": 3}]


def test_trailing_comma_in_nested_array():
    text = '{"items": [1, 2, 3,]}'
    r = parse_jsonl(text)
    assert r.records == [{"items": [1, 2, 3]}]


def test_truncation_mid_string():
    text = '{"a": 1, "title": "Jamf launches some really long pr'
    r = parse_jsonl(text)
    assert len(r.records) == 1
    assert r.records[0]["a"] == 1
    assert r.records[0]["title"].startswith("Jamf launches")


def test_truncation_mid_object():
    text = '{"a": 1}\n{"a": 2, "nested": {"k":'
    r = parse_jsonl(text)
    assert r.records[0] == {"a": 1}
    assert len(r.records) >= 1


def test_single_big_json_object_with_items_array():
    text = '{"items": [{"a": 1}, {"a": 2}, {"a": 3}]}'
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2, 3]


def test_single_big_json_array():
    text = '[{"a": 1}, {"a": 2}]'
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2]


def test_bulleted_list_prefix():
    text = (
        '- {"a": 1}\n'
        '- {"a": 2}\n'
        '* {"a": 3}\n'
    )
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2, 3]


def test_numbered_list_prefix():
    text = '1. {"a": 1}\n2. {"a": 2}\n3) {"a": 3}'
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2, 3]


def test_garbage_line_produces_diagnostic():
    text = '{"a": 1}\nthis is not json at all\n{"a": 2}'
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2]
    assert r.diagnostics == []


def test_partially_broken_line_produces_diagnostic():
    text = '{"a": 1}\n{this is not valid json}\n{"a": 2}'
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2]
    assert len(r.diagnostics) == 1
    assert r.diagnostics[0].line_no == 2


def test_unicode_preserved():
    text = '{"title": "Omnissa: \\u201cZero Trust\\u201d push"}'
    r = parse_jsonl(text)
    assert "Zero Trust" in r.records[0]["title"]


def test_nested_objects_intact():
    text = '{"a": 1, "scores": {"strategic": 8, "sales": 4}, "tags": ["jamf", "pricing"]}'
    r = parse_jsonl(text)
    assert r.records[0]["scores"]["strategic"] == 8
    assert r.records[0]["tags"] == ["jamf", "pricing"]


def test_comments_lines_skipped():
    text = '// comment\n# also comment\n{"a": 1}'
    r = parse_jsonl(text)
    assert r.records == [{"a": 1}]


def test_long_realistic_brief_truncated():
    text = (
        '```json\n'
        '{"id": "j1", "competitor": "jamf", "headline": "Jamf acquires X",'
        ' "score": 8.2, "bucket": "P0", "sources": ["https://jamf.com/pr"]}\n'
        '{"id": "j2", "competitor": "intune", "headline": "Intune pricing change",'
        ' "score": 5.1, "bucket": "P1", "sources": ["https://microsoft.com'
    )
    r = parse_jsonl(text)
    assert r.records[0]["id"] == "j1"
    assert r.records[0]["score"] == 8.2
    assert len(r.records) == 2
    assert r.records[1]["id"] == "j2"


def test_results_key_alias():
    text = '{"results": [{"a": 1}, {"a": 2}]}'
    r = parse_jsonl(text)
    assert [x["a"] for x in r.records] == [1, 2]


def test_briefs_key_alias():
    text = '{"briefs": [{"headline": "x"}, {"headline": "y"}]}'
    r = parse_jsonl(text)
    assert [x["headline"] for x in r.records] == ["x", "y"]


def test_empty_array_in_wrapper():
    text = '{"items": []}'
    r = parse_jsonl(text)
    assert r.records == []
