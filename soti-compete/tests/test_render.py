from __future__ import annotations

from datetime import UTC, datetime

from soti_compete.notify.render import render_email, render_teams_card
from soti_compete.storage import Brief


def _brief(**kw) -> Brief:
    defaults = dict(
        id="b1",
        url="https://jamf.com/pr/x",
        url_fingerprint="fp1",
        title="Jamf acquires Y for $200M",
        competitor_id="jamf",
        news_type="acquisition",
        response_type="obligation",
        confidence_signal="multi_source",
        bucket="P0",
        raw_score=8.2,
        recency_multiplier=1.0,
        confidence_multiplier=1.0,
        final_score=8.2,
        dimensions={"strategic_impact": 9, "sales_signal": 7,
                    "roadmap_overlap": 6, "competitor_tier": 10, "source_quality": 10},
        summary="Jamf announced a $200M acquisition expanding into device-trust posture.",
        gap_analysis={
            "soti_today": "Limited device-trust integration",
            "roadmap": "[STUB] Jira not connected — see PRD-1234 when wired",
            "others": "Intune has Microsoft Entra integration; Omnissa via Workspace ONE",
        },
        sources=[
            {"url": "https://jamf.com/pr/x", "domain": "jamf.com"},
            {"url": "https://reuters.com/x", "domain": "reuters.com"},
        ],
        flow="daily",
        raw_payload={},
        created_at=datetime(2026, 5, 10, 7, 0, tzinfo=UTC),
    )
    defaults.update(kw)
    return Brief(**defaults)


def test_render_email_contains_key_fields():
    e = render_email([_brief()], subject="[P0 COMPETE] Jamf acquires Y")
    assert e.subject == "[P0 COMPETE] Jamf acquires Y"
    assert "Jamf acquires Y for $200M" in e.plaintext
    assert "P0" in e.html
    assert "Jamf acquires Y for $200M" in e.html
    assert "8.20" in e.html
    assert "[STUB]" in e.html
    assert "reuters.com" in e.html


def test_render_email_plaintext_has_no_html():
    e = render_email([_brief()], subject="x")
    assert "<" not in e.plaintext
    assert ">" not in e.plaintext or e.plaintext.count(">") <= 2


def test_render_email_html_escapes_user_content():
    b = _brief(title="<script>alert(1)</script> Jamf does a thing")
    e = render_email([b], subject="test")
    assert "<script>" not in e.html
    assert "&lt;script&gt;" in e.html


def test_render_email_multiple_briefs():
    briefs = [_brief(id="a"), _brief(id="b", title="Intune pricing change", competitor_id="intune")]
    e = render_email(briefs, subject="P1 Digest", heading="Daily P1 Digest")
    assert "Jamf acquires Y for $200M" in e.html
    assert "Intune pricing change" in e.html
    assert "Daily P1 Digest" in e.html


def test_render_teams_card_basic():
    card = render_teams_card(_brief())
    assert card["type"] == "message"
    assert len(card["attachments"]) == 1
    content = card["attachments"][0]["content"]
    assert content["type"] == "AdaptiveCard"

    text_blocks = [b for b in content["body"] if b.get("type") == "TextBlock"]
    assert any("Jamf acquires Y" in b["text"] for b in text_blocks)

    facts = [b for b in content["body"] if b.get("type") == "FactSet"][0]["facts"]
    titles = [f["title"] for f in facts]
    assert "Competitor" in titles
    assert "Final score" in titles
    assert "SOTI today" in titles


def test_render_teams_card_actions_have_urls():
    card = render_teams_card(_brief())
    actions = card["attachments"][0]["content"]["actions"]
    assert len(actions) >= 1
    for a in actions:
        assert a["type"] == "Action.OpenUrl"
        assert a["url"].startswith("https://")


def test_render_teams_card_caps_actions_at_4():
    b = _brief(sources=[{"url": f"https://example.com/{i}", "domain": f"e{i}.com"} for i in range(10)])
    card = render_teams_card(b)
    actions = card["attachments"][0]["content"]["actions"]
    assert len(actions) == 4
