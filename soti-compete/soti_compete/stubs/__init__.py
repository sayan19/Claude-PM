"""Phase 3 wire-in points.

Each module exposes a typed interface that returns placeholder data tagged
`[STUB]` and logs at WARNING. When the upstream system is wired up (Salesforce,
Gong, Jira/Productboard), only the function bodies change.
"""
from soti_compete.stubs.gong import GongMention, get_recent_mentions
from soti_compete.stubs.jira import RoadmapItem, get_roadmap_overlap
from soti_compete.stubs.salesforce import CompetitorLoss, get_competitor_losses

__all__ = [
    "CompetitorLoss",
    "GongMention",
    "RoadmapItem",
    "get_competitor_losses",
    "get_recent_mentions",
    "get_roadmap_overlap",
]
