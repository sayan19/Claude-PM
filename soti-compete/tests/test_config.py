from __future__ import annotations

import pytest

from soti_compete.config import load_config


def test_load_config_succeeds(config_dir):
    cfg = load_config(config_dir)
    assert cfg.competitors.competitors
    assert {c.id for c in cfg.competitors.competitors} >= {
        "jamf", "omnissa", "intune", "ivanti", "maas360",
        "42gears", "hexnode", "scalefusion", "knox",
    }


def test_direct_competitors(config):
    ids = {c.id for c in config.competitors.direct()}
    assert ids == {"jamf", "omnissa", "intune", "ivanti", "maas360"}


def test_weights_sum_to_100(config):
    w = config.scoring.weights
    total = (
        w.strategic_impact + w.sales_signal + w.roadmap_overlap
        + w.competitor_tier + w.source_quality
    )
    assert total == 100


def test_bucket_for(config):
    s = config.scoring
    assert s.bucket_for(9.0) == "P0"
    assert s.bucket_for(7.5) == "P0"
    assert s.bucket_for(7.49) == "P1"
    assert s.bucket_for(5.0) == "P1"
    assert s.bucket_for(4.99) == "P2"
    assert s.bucket_for(2.5) == "P2"
    assert s.bucket_for(2.49) == "DROP"
    assert s.bucket_for(0.0) == "DROP"


def test_classify_domain(config):
    s = config.sources
    assert s.classify_domain("sec.gov") == "sec_filing"
    assert s.classify_domain("www.sec.gov") == "sec_filing"
    assert s.classify_domain("bloomberg.com") == "tier_1_press"
    assert s.classify_domain("gartner.com") == "analyst"
    assert s.classify_domain("jamf.com", competitor_id="jamf") == "vendor_press"
    assert s.classify_domain("randomblog.example") == "secondary"


def test_missing_config_dir_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_config(tmp_path / "does-not-exist")


def test_partial_config_dir_raises(tmp_path):
    (tmp_path / "competitors.yaml").write_text("competitors: []")
    with pytest.raises(FileNotFoundError, match="missing config files"):
        load_config(tmp_path)
