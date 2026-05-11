from __future__ import annotations

from soti_compete.llm.prompts import (
    SYSTEM_DAILY_SCAN,
    SYSTEM_HOURLY_SWEEP,
    SYSTEM_PASTEIN,
    SYSTEM_SENTIMENT,
    USER_DAILY_SCAN,
    USER_HOURLY_SWEEP,
    USER_PASTEIN,
    USER_SENTIMENT,
    format_competitor_list,
)


def test_daily_system_includes_jsonl_directive():
    assert "JSONL" in SYSTEM_DAILY_SCAN
    assert "one JSON object per line" in SYSTEM_DAILY_SCAN.lower() or "one json object per line" in SYSTEM_DAILY_SCAN.lower()


def test_daily_system_lists_competitor_ids():
    for cid in ["jamf", "omnissa", "intune", "ivanti", "maas360",
                "42gears", "hexnode", "scalefusion", "knox"]:
        assert cid in SYSTEM_DAILY_SCAN


def test_daily_system_warns_against_tier_and_recency_in_output():
    assert "DO NOT include" in SYSTEM_DAILY_SCAN


def test_daily_user_substitution():
    rendered = USER_DAILY_SCAN.substitute(
        lookback_days=7,
        today_iso="2026-05-11",
        timezone="America/Toronto",
        direct_list="  - jamf: Jamf",
        adjacent_list="  - knox: Samsung Knox",
        roadmap_stub="[STUB] Jira not connected",
    )
    assert "7 days" in rendered
    assert "2026-05-11" in rendered
    assert "America/Toronto" in rendered
    assert "[STUB] Jira not connected" in rendered


def test_format_competitor_list_empty():
    assert "(none configured)" in format_competitor_list([])


def test_format_competitor_list_basic():
    out = format_competitor_list([("jamf", "Jamf"), ("intune", "Microsoft Intune")])
    assert "- jamf: Jamf" in out
    assert "- intune: Microsoft Intune" in out


def test_hourly_user_substitution():
    rendered = USER_HOURLY_SWEEP.substitute(
        now_iso="2026-05-11T14:00:00-04:00",
        direct_list="  - jamf: Jamf",
        roadmap_stub="[STUB]",
    )
    assert "2026-05-11T14:00:00-04:00" in rendered


def test_pastein_user_substitution_preserves_content():
    rendered = USER_PASTEIN.substitute(
        roadmap_stub="[STUB]",
        content="customer mentioned $template_var and other things",
    )
    assert "$template_var" in rendered
    assert "customer mentioned" in rendered


def test_sentiment_system_demands_single_json_object():
    assert "SINGLE JSON object" in SYSTEM_SENTIMENT


def test_sentiment_user_substitution():
    rendered = USER_SENTIMENT.substitute(
        competitor_name="Jamf",
        competitor_id="jamf",
        lookback_days=30,
        today_iso="2026-05-11",
        platforms="  - reddit: reddit.com",
        aliases="Jamf Pro, Jamf School",
    )
    assert "Jamf" in rendered
    assert "30 days" in rendered


def test_all_systems_demand_structured_output():
    for s in (SYSTEM_DAILY_SCAN, SYSTEM_HOURLY_SWEEP, SYSTEM_PASTEIN, SYSTEM_SENTIMENT):
        lower = s.lower()
        assert "jsonl" in lower or "json object" in lower
