"""SOTI Compete command-line entry point."""

from __future__ import annotations

import logging
import re
import sys
from dataclasses import asdict
from datetime import UTC, datetime, timedelta

import click

from soti_compete.bootstrap import bootstrap
from soti_compete.flows import (
    run_daily_scan,
    run_hourly_sweep,
    run_pastein,
    run_sentiment_monthly,
)
from soti_compete.healthcheck import run_healthcheck

_REL_RE = re.compile(r"^(\d+)([dhwm])$")


def _setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(name)s: %(message)s")


def _parse_since(value: str | None) -> datetime | None:
    if not value:
        return None
    m = _REL_RE.match(value.strip())
    if m:
        n, unit = int(m.group(1)), m.group(2)
        delta = {"h": timedelta(hours=n), "d": timedelta(days=n),
                 "w": timedelta(weeks=n), "m": timedelta(days=30 * n)}[unit]
        return datetime.now(UTC) - delta
    try:
        return datetime.fromisoformat(value)
    except ValueError as e:
        raise click.BadParameter(f"--since must be ISO date or e.g. '7d': {e}") from None


def _print_result(result, *, json_out: bool) -> None:
    if json_out:
        click.echo(_to_json(result))
        return
    d = asdict(result)
    click.echo(f"flow={d.get('flow')}")
    for k in ("briefs_total", "briefs_persisted", "briefs_deduped",
              "briefs_unknown_competitor", "p0_emails_sent", "p0_teams_sent",
              "p1_digest_sent", "search_count", "snapshots_saved", "digest_sent",
              "competitors_scanned"):
        if k in d:
            click.echo(f"  {k}: {d[k]}")
    if d.get("by_bucket"):
        click.echo(f"  by_bucket: {d['by_bucket']}")
    if d.get("parse_diagnostics"):
        click.echo(f"  parse_diagnostics: {len(d['parse_diagnostics'])} lines unparseable")
    if d.get("errors"):
        for e in d["errors"]:
            click.echo(f"  ERROR: {e}")


def _to_json(result) -> str:
    import json
    return json.dumps(asdict(result), indent=2, default=str)


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Verbose logging.")
@click.option("--config-dir", default=None, help="Override config directory.")
@click.pass_context
def cli(ctx: click.Context, verbose: bool, config_dir: str | None) -> None:
    """SOTI Compete: competitive intelligence pipeline."""
    _setup_logging(verbose)
    ctx.ensure_object(dict)
    ctx.obj["config_dir"] = config_dir


@cli.command()
@click.pass_context
def healthcheck(ctx: click.Context) -> None:
    """Verify integrations: config, Anthropic env, storage, SMTP, Teams, outbox."""
    report = run_healthcheck(ctx.obj.get("config_dir"))
    click.echo(report.format())
    sys.exit(0 if report.ok else 1)


@cli.command()
@click.option("--json", "json_out", is_flag=True, help="Emit JSON result.")
@click.pass_context
def daily(ctx: click.Context, json_out: bool) -> None:
    """Run the 7am daily scan."""
    c = bootstrap(ctx.obj.get("config_dir"))
    result = run_daily_scan(config=c.config, llm=c.llm, storage=c.storage, smtp=c.smtp, teams=c.teams)
    _print_result(result, json_out=json_out)


@cli.command()
@click.option("--json", "json_out", is_flag=True, help="Emit JSON result.")
@click.pass_context
def hourly(ctx: click.Context, json_out: bool) -> None:
    """Run the hourly P0 sweep on direct competitors."""
    c = bootstrap(ctx.obj.get("config_dir"))
    result = run_hourly_sweep(config=c.config, llm=c.llm, storage=c.storage, smtp=c.smtp, teams=c.teams)
    _print_result(result, json_out=json_out)


@cli.command()
@click.option("--file", "-f", type=click.File("r"), help="Read content from file.")
@click.option("--text", "-t", help="Inline text content.")
@click.option("--json", "json_out", is_flag=True, help="Emit JSON result.")
@click.pass_context
def pastein(ctx: click.Context, file, text: str | None, json_out: bool) -> None:
    """Score and route ad hoc text submitted by sales/CSM."""
    if file and text:
        raise click.UsageError("pass --file OR --text, not both")
    if file:
        content = file.read()
    elif text:
        content = text
    else:
        if sys.stdin.isatty():
            raise click.UsageError("pass --file, --text, or pipe content via stdin")
        content = sys.stdin.read()

    c = bootstrap(ctx.obj.get("config_dir"))
    result = run_pastein(content, config=c.config, llm=c.llm, storage=c.storage, smtp=c.smtp, teams=c.teams)
    _print_result(result, json_out=json_out)


@cli.command()
@click.option("--json", "json_out", is_flag=True, help="Emit JSON result.")
@click.pass_context
def sentiment(ctx: click.Context, json_out: bool) -> None:
    """Run the monthly sentiment job."""
    c = bootstrap(ctx.obj.get("config_dir"))
    result = run_sentiment_monthly(config=c.config, llm=c.llm, storage=c.storage, smtp=c.smtp)
    _print_result(result, json_out=json_out)


@cli.command()
@click.option("--since", default=None, help="ISO date or relative ('7d', '1w', '24h').")
@click.option("--bucket", default=None, type=click.Choice(["P0", "P1", "P2", "DROP"]))
@click.option("--competitor", default=None, help="Filter by competitor id.")
@click.option("--flow", default=None, type=click.Choice(["daily", "hourly", "pastein", "sentiment"]))
@click.option("--limit", default=50, type=int)
@click.pass_context
def query(ctx: click.Context, since: str | None, bucket: str | None,
          competitor: str | None, flow: str | None, limit: int) -> None:
    """Query stored briefs."""
    c = bootstrap(ctx.obj.get("config_dir"))
    rows = c.storage.query_briefs(
        since=_parse_since(since),
        bucket=bucket,
        competitor_id=competitor,
        flow=flow,
        limit=limit,
    )
    if not rows:
        click.echo("(no results)")
        return
    for b in rows:
        when = b.created_at.strftime("%Y-%m-%d %H:%M") if b.created_at else "?"
        click.echo(f"[{b.bucket}] {when}  {b.competitor_id or '-':<12}  {b.final_score:5.2f}  {b.title}")


def main() -> None:
    cli(obj={})


if __name__ == "__main__":
    main()
