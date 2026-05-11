"""Resilient JSONL parser.

The system asks Claude to emit one JSON object per line. Real-world failure modes:
    - Markdown code fences (```json ... ```)
    - Prose before/after the JSONL block
    - Trailing commas inside objects/arrays
    - Truncation mid-string (response cut off by max_tokens)
    - A single huge JSON object/array instead of JSONL (model regression)
    - Leading bullets or numbering ("- {...}", "1. {...}")

`parse_jsonl` recovers as many valid records as it can without raising. Errors
land in a per-record `ParseDiagnostic` list so callers can log and move on.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

_FENCE_RE = re.compile(r"```(?:json|jsonl)?\s*\n?(.*?)```", re.DOTALL | re.IGNORECASE)
_LINE_PREFIX_RE = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+")
_TRAILING_COMMA_RE = re.compile(r",(\s*[}\]])")


@dataclass
class ParseDiagnostic:
    line_no: int
    error: str
    raw: str


@dataclass
class ParseResult:
    records: list[dict[str, Any]] = field(default_factory=list)
    diagnostics: list[ParseDiagnostic] = field(default_factory=list)

    def __iter__(self):
        return iter(self.records)

    def __len__(self) -> int:
        return len(self.records)


def _strip_fences(text: str) -> str:
    matches = _FENCE_RE.findall(text)
    if matches:
        return "\n".join(m.strip() for m in matches)
    return text


def _strip_line_prefix(line: str) -> str:
    return _LINE_PREFIX_RE.sub("", line, count=1)


def _strip_trailing_commas(s: str) -> str:
    return _TRAILING_COMMA_RE.sub(r"\1", s)


def _try_load(s: str) -> tuple[Any | None, str | None]:
    try:
        return json.loads(s), None
    except json.JSONDecodeError as e:
        return None, str(e)


def _repair_truncation(s: str) -> str | None:
    """Best-effort: balance brackets/quotes for a truncated object.

    Returns a candidate string, or None if it doesn't look recoverable.
    """
    if not s or s[0] not in "{[":
        return None

    in_string = False
    escape = False
    stack: list[str] = []
    for ch in s:
        if escape:
            escape = False
            continue
        if ch == "\\" and in_string:
            escape = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if ch in "{[":
            stack.append(ch)
        elif ch in "}]" and stack:
            stack.pop()

    repaired = s
    if in_string:
        repaired += '"'
    while stack:
        opener = stack.pop()
        repaired += "}" if opener == "{" else "]"
    return repaired


def _try_repair(s: str) -> dict | list | None:
    """Try a ladder of common repairs."""
    candidates = [s, _strip_trailing_commas(s)]
    repaired = _repair_truncation(s)
    if repaired:
        candidates.append(repaired)
        candidates.append(_strip_trailing_commas(repaired))
    for c in candidates:
        v, err = _try_load(c)
        if err is None:
            return v
    return None


def _coerce_records(value: Any) -> list[dict]:
    if isinstance(value, dict):
        for key in ("items", "results", "records", "briefs", "data"):
            inner = value.get(key)
            if isinstance(inner, list) and len(value) == 1 and all(
                isinstance(r, dict) for r in inner
            ):
                return inner
        return [value]
    if isinstance(value, list):
        return [r for r in value if isinstance(r, dict)]
    return []


def parse_jsonl(text: str) -> ParseResult:
    """Parse JSONL emitted by an LLM. Returns recovered records + diagnostics."""
    result = ParseResult()
    if not text or not text.strip():
        return result

    body = _strip_fences(text).strip()

    whole = _try_repair(body)
    if whole is not None:
        records = _coerce_records(whole)
        if records:
            result.records.extend(records)
            return result

    for line_no, raw_line in enumerate(body.splitlines(), start=1):
        line = _strip_line_prefix(raw_line).strip()
        if not line:
            continue
        if line.startswith(("//", "#")):
            continue
        if not (line.startswith("{") or line.startswith("[")):
            continue

        value = _try_repair(line)
        if value is None:
            result.diagnostics.append(
                ParseDiagnostic(line_no=line_no, error="unparseable line", raw=raw_line)
            )
            continue
        records = _coerce_records(value)
        if records:
            result.records.extend(records)
        else:
            result.diagnostics.append(
                ParseDiagnostic(line_no=line_no, error="no dict records found", raw=raw_line)
            )

    return result


__all__ = ["ParseDiagnostic", "ParseResult", "parse_jsonl"]
