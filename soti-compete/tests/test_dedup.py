from __future__ import annotations

from soti_compete.dedup import (
    SeenItem,
    canonicalize_url,
    is_duplicate,
    normalize_title,
    title_similarity,
    url_fingerprint,
)


def test_canonicalize_strips_tracking():
    a = "https://www.example.com/article?utm_source=twitter&utm_medium=social&id=42"
    b = "https://example.com/article?id=42"
    assert canonicalize_url(a) == canonicalize_url(b)


def test_canonicalize_trailing_slash():
    assert canonicalize_url("https://example.com/a/b/") == canonicalize_url("https://example.com/a/b")


def test_canonicalize_query_order_independent():
    a = "https://example.com/x?b=2&a=1"
    b = "https://example.com/x?a=1&b=2"
    assert canonicalize_url(a) == canonicalize_url(b)


def test_canonicalize_scheme_normalized():
    assert canonicalize_url("HTTP://Example.com/X").startswith("https://example.com")


def test_canonicalize_empty():
    assert canonicalize_url("") == ""


def test_fingerprint_stable_and_short():
    fp = url_fingerprint("https://example.com/a")
    assert len(fp) == 16
    assert fp == url_fingerprint("https://www.example.com/a/?utm_source=x")


def test_normalize_title_lowercases_and_strips_punct():
    assert normalize_title("Jamf Pro: \"Now with Zero-Trust!\"") == "jamf pro now with zero trust"


def test_title_similarity_identical():
    assert title_similarity("Jamf launches X", "Jamf launches X") == 100


def test_title_similarity_minor_variation():
    a = "Jamf launches new feature for iOS device management"
    b = "Jamf Launches New Feature for iOS Device Management."
    assert title_similarity(a, b) >= 95


def test_title_similarity_different():
    a = "Jamf launches feature X"
    b = "Microsoft Intune announces pricing change"
    assert title_similarity(a, b) < 50


def test_title_similarity_empty():
    assert title_similarity("", "anything") == 0
    assert title_similarity("anything", "") == 0


def test_is_duplicate_by_url_fingerprint():
    seen = [SeenItem(url_fingerprint=url_fingerprint("https://example.com/a"), title="X")]
    assert is_duplicate(
        "https://www.example.com/a/?utm_source=tw",
        "totally different title",
        None,
        seen,
    ) is True


def test_is_duplicate_by_title():
    seen = [SeenItem(url_fingerprint="abcd", title="Jamf launches new iOS feature")]
    assert is_duplicate(
        "https://other.example/x",
        "Jamf Launches New iOS Feature!",
        None,
        seen,
        similarity_threshold=90,
    ) is True


def test_is_not_duplicate():
    seen = [SeenItem(url_fingerprint="abcd", title="Jamf launches feature")]
    assert is_duplicate(
        "https://different.example/y",
        "Microsoft Intune pricing change",
        None,
        seen,
        similarity_threshold=90,
    ) is False


def test_title_match_respects_competitor_when_set():
    seen = [
        SeenItem(url_fingerprint="abcd", title="New iOS feature announced", competitor_id="jamf")
    ]
    # candidate is for a different competitor — title alone shouldn't trigger
    assert is_duplicate(
        "https://example.com/intune-story",
        "New iOS feature announced",
        "intune",
        seen,
        similarity_threshold=90,
    ) is False


def test_threshold_can_be_loosened():
    seen = [SeenItem(url_fingerprint="abcd", title="Jamf launches feature for iOS")]
    candidate_title = "Jamf reveals new tool for iPhones"
    assert is_duplicate(
        "https://example.com/x",
        candidate_title,
        None,
        seen,
        similarity_threshold=99,
    ) is False
