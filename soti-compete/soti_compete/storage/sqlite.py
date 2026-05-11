from __future__ import annotations

import json
import sqlite3
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from soti_compete.config import Bucket
from soti_compete.dedup import SeenItem
from soti_compete.storage.base import Brief, SentimentSnapshot, Storage

_SCHEMA = """
CREATE TABLE IF NOT EXISTS briefs (
    id TEXT PRIMARY KEY,
    url TEXT,
    url_fingerprint TEXT,
    title TEXT NOT NULL,
    competitor_id TEXT,
    news_type TEXT,
    response_type TEXT,
    confidence_signal TEXT,
    bucket TEXT NOT NULL,
    raw_score REAL NOT NULL,
    recency_multiplier REAL NOT NULL,
    confidence_multiplier REAL NOT NULL,
    final_score REAL NOT NULL,
    dimensions_json TEXT NOT NULL,
    summary TEXT,
    gap_analysis_json TEXT,
    sources_json TEXT,
    raw_payload_json TEXT,
    flow TEXT,
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_briefs_created_at ON briefs(created_at);
CREATE INDEX IF NOT EXISTS idx_briefs_bucket ON briefs(bucket);
CREATE INDEX IF NOT EXISTS idx_briefs_competitor ON briefs(competitor_id);
CREATE INDEX IF NOT EXISTS idx_briefs_url_fp ON briefs(url_fingerprint);

CREATE TABLE IF NOT EXISTS sentiment_snapshots (
    id TEXT PRIMARY KEY,
    competitor_id TEXT NOT NULL,
    period_start TEXT NOT NULL,
    period_end TEXT NOT NULL,
    summary_json TEXT NOT NULL,
    sources_json TEXT,
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_sentiment_competitor ON sentiment_snapshots(competitor_id);
CREATE INDEX IF NOT EXISTS idx_sentiment_created ON sentiment_snapshots(created_at);
"""


_INSERT_BRIEF_SQL = """
INSERT OR REPLACE INTO briefs (
    id, url, url_fingerprint, title, competitor_id, news_type, response_type,
    confidence_signal, bucket, raw_score, recency_multiplier, confidence_multiplier,
    final_score, dimensions_json, summary, gap_analysis_json, sources_json,
    raw_payload_json, flow, created_at
) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
"""


def _iso(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC).isoformat()


def _parse(iso: str) -> datetime:
    return datetime.fromisoformat(iso)


def _brief_row(brief: Brief) -> tuple:
    return (
        brief.id,
        brief.url,
        brief.url_fingerprint,
        brief.title,
        brief.competitor_id,
        brief.news_type,
        brief.response_type,
        brief.confidence_signal,
        brief.bucket,
        brief.raw_score,
        brief.recency_multiplier,
        brief.confidence_multiplier,
        brief.final_score,
        json.dumps(brief.dimensions),
        brief.summary,
        json.dumps(brief.gap_analysis),
        json.dumps(brief.sources),
        json.dumps(brief.raw_payload),
        brief.flow,
        _iso(brief.created_at),
    )


class SQLiteStorage(Storage):
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def _init_schema(self) -> None:
        with self._connect() as conn:
            conn.executescript(_SCHEMA)

    def save_brief(self, brief: Brief) -> None:
        with self._connect() as conn:
            conn.execute(_INSERT_BRIEF_SQL, _brief_row(brief))

    def save_briefs(self, briefs: list[Brief]) -> None:
        if not briefs:
            return
        with self._connect() as conn:
            conn.executemany(_INSERT_BRIEF_SQL, [_brief_row(b) for b in briefs])

    def get_brief(self, brief_id: str) -> Brief | None:
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM briefs WHERE id = ?", (brief_id,)).fetchone()
        return _row_to_brief(row) if row else None

    def query_briefs(
        self,
        *,
        since: datetime | None = None,
        until: datetime | None = None,
        bucket: Bucket | None = None,
        competitor_id: str | None = None,
        flow: str | None = None,
        limit: int = 200,
    ) -> list[Brief]:
        clauses = []
        params: list[Any] = []
        if since:
            clauses.append("created_at >= ?")
            params.append(_iso(since))
        if until:
            clauses.append("created_at < ?")
            params.append(_iso(until))
        if bucket:
            clauses.append("bucket = ?")
            params.append(bucket)
        if competitor_id:
            clauses.append("competitor_id = ?")
            params.append(competitor_id)
        if flow:
            clauses.append("flow = ?")
            params.append(flow)

        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        sql = f"SELECT * FROM briefs {where} ORDER BY created_at DESC LIMIT ?"
        params.append(limit)
        with self._connect() as conn:
            rows = conn.execute(sql, params).fetchall()
        return [_row_to_brief(r) for r in rows]

    def recent_seen_items(self, days: int) -> list[SeenItem]:
        cutoff = datetime.now(UTC) - timedelta(days=days)
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT url_fingerprint, title, competitor_id FROM briefs WHERE created_at >= ?",
                (_iso(cutoff),),
            ).fetchall()
        return [
            SeenItem(
                url_fingerprint=r["url_fingerprint"] or "",
                title=r["title"] or "",
                competitor_id=r["competitor_id"],
            )
            for r in rows
        ]

    def save_sentiment(self, snapshot: SentimentSnapshot) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO sentiment_snapshots (
                    id, competitor_id, period_start, period_end, summary_json, sources_json, created_at
                ) VALUES (?,?,?,?,?,?,?)
                """,
                (
                    snapshot.id,
                    snapshot.competitor_id,
                    _iso(snapshot.period_start),
                    _iso(snapshot.period_end),
                    json.dumps(snapshot.summary),
                    json.dumps(snapshot.sources),
                    _iso(snapshot.created_at),
                ),
            )

    def query_sentiment(
        self,
        *,
        competitor_id: str | None = None,
        since: datetime | None = None,
        limit: int = 100,
    ) -> list[SentimentSnapshot]:
        clauses = []
        params: list[Any] = []
        if competitor_id:
            clauses.append("competitor_id = ?")
            params.append(competitor_id)
        if since:
            clauses.append("created_at >= ?")
            params.append(_iso(since))
        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        sql = f"SELECT * FROM sentiment_snapshots {where} ORDER BY created_at DESC LIMIT ?"
        params.append(limit)
        with self._connect() as conn:
            rows = conn.execute(sql, params).fetchall()
        return [_row_to_sentiment(r) for r in rows]

    def ping(self) -> bool:
        try:
            with self._connect() as conn:
                conn.execute("SELECT 1").fetchone()
            return True
        except sqlite3.Error:
            return False


def _row_to_brief(row: sqlite3.Row) -> Brief:
    return Brief(
        id=row["id"],
        url=row["url"] or "",
        url_fingerprint=row["url_fingerprint"] or "",
        title=row["title"],
        competitor_id=row["competitor_id"],
        news_type=row["news_type"],
        response_type=row["response_type"] or "housekeeping",
        confidence_signal=row["confidence_signal"] or "single",
        bucket=row["bucket"],
        raw_score=row["raw_score"],
        recency_multiplier=row["recency_multiplier"],
        confidence_multiplier=row["confidence_multiplier"],
        final_score=row["final_score"],
        dimensions=json.loads(row["dimensions_json"] or "{}"),
        summary=row["summary"] or "",
        gap_analysis=json.loads(row["gap_analysis_json"] or "{}"),
        sources=json.loads(row["sources_json"] or "[]"),
        raw_payload=json.loads(row["raw_payload_json"] or "{}"),
        flow=row["flow"] or "daily",
        created_at=_parse(row["created_at"]),
    )


def _row_to_sentiment(row: sqlite3.Row) -> SentimentSnapshot:
    return SentimentSnapshot(
        id=row["id"],
        competitor_id=row["competitor_id"],
        period_start=_parse(row["period_start"]),
        period_end=_parse(row["period_end"]),
        summary=json.loads(row["summary_json"]),
        sources=json.loads(row["sources_json"] or "[]"),
        created_at=_parse(row["created_at"]),
    )


__all__ = ["SQLiteStorage"]
