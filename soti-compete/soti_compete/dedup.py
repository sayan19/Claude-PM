"""Dedup utilities: URL canonicalization + fuzzy title matching."""

from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable
from dataclasses import dataclass
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from rapidfuzz import fuzz

_TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "gclid", "fbclid", "mc_cid", "mc_eid", "ref", "ref_src", "ref_url",
    "igshid", "_hsenc", "_hsmi", "hsCtaTracking",
}

_WHITESPACE_RE = re.compile(r"\s+")
_PUNCT_RE = re.compile(r"[^\w\s]")


def canonicalize_url(url: str) -> str:
    if not url:
        return ""
    parts = urlsplit(url.strip())
    scheme = "https" if parts.scheme in {"http", "https", ""} else parts.scheme.lower()
    netloc = parts.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    path = re.sub(r"/+$", "", parts.path) or "/"

    query_pairs = [
        (k, v) for k, v in parse_qsl(parts.query, keep_blank_values=False)
        if k.lower() not in _TRACKING_PARAMS
    ]
    query_pairs.sort()
    query = urlencode(query_pairs)

    return urlunsplit((scheme, netloc, path, query, ""))


def url_fingerprint(url: str) -> str:
    canon = canonicalize_url(url)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:16]


def normalize_title(title: str) -> str:
    if not title:
        return ""
    t = title.lower()
    t = _PUNCT_RE.sub(" ", t)
    t = _WHITESPACE_RE.sub(" ", t).strip()
    return t


def title_similarity(a: str, b: str) -> int:
    a_norm = normalize_title(a)
    b_norm = normalize_title(b)
    if not a_norm or not b_norm:
        return 0
    return int(fuzz.token_set_ratio(a_norm, b_norm))


@dataclass(frozen=True)
class SeenItem:
    url_fingerprint: str
    title: str
    competitor_id: str | None = None


def is_duplicate(
    candidate_url: str,
    candidate_title: str,
    candidate_competitor: str | None,
    seen: Iterable[SeenItem],
    similarity_threshold: int = 90,
) -> bool:
    fp = url_fingerprint(candidate_url) if candidate_url else ""
    for s in seen:
        if fp and s.url_fingerprint == fp:
            return True
        if candidate_competitor and s.competitor_id and s.competitor_id != candidate_competitor:
            continue
        if title_similarity(candidate_title, s.title) >= similarity_threshold:
            return True
    return False


__all__ = [
    "SeenItem",
    "canonicalize_url",
    "is_duplicate",
    "normalize_title",
    "title_similarity",
    "url_fingerprint",
]
