from __future__ import annotations

from datetime import UTC, datetime
from zoneinfo import ZoneInfo

from dateutil import parser as date_parser


def tz(name: str) -> ZoneInfo:
    return ZoneInfo(name)


def now_local(timezone_name: str) -> datetime:
    return datetime.now(tz(timezone_name))


def now_utc() -> datetime:
    return datetime.now(UTC)


def parse_when(value: str | datetime | None) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=UTC)
    try:
        dt = date_parser.parse(value)
    except (ValueError, TypeError):
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=UTC)
    return dt


def age_days(when: datetime, *, reference: datetime | None = None) -> float:
    ref = reference or now_utc()
    if when.tzinfo is None:
        when = when.replace(tzinfo=UTC)
    if ref.tzinfo is None:
        ref = ref.replace(tzinfo=UTC)
    return (ref - when).total_seconds() / 86400.0


__all__ = ["age_days", "now_local", "now_utc", "parse_when", "tz"]
