"""SOTI Compete command-line entry point.

Stage 1 only wires `healthcheck`. The other subcommands are stubbed with
placeholder messages so the CLI surface is visible end-to-end.
"""

from __future__ import annotations

import logging
import sys

import click

from soti_compete.healthcheck import run_healthcheck


def _setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


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
def daily() -> None:
    """Run the 7am daily scan. (Stage 3 — not yet implemented.)"""
    click.echo("daily: not yet implemented (Stage 3)")
    sys.exit(2)


@cli.command()
def hourly() -> None:
    """Run the hourly P0 sweep. (Stage 3 — not yet implemented.)"""
    click.echo("hourly: not yet implemented (Stage 3)")
    sys.exit(2)


@cli.command()
@click.option("--file", "-f", type=click.Path(exists=True, dir_okay=False))
def pastein(file: str | None) -> None:
    """Score and route ad hoc text. (Stage 3 — not yet implemented.)"""
    click.echo("pastein: not yet implemented (Stage 3)")
    sys.exit(2)


@cli.command()
def sentiment() -> None:
    """Run the monthly sentiment job. (Stage 3 — not yet implemented.)"""
    click.echo("sentiment: not yet implemented (Stage 3)")
    sys.exit(2)


@cli.command()
@click.option("--since", default=None, help="ISO date or relative (e.g. '7d').")
@click.option("--bucket", default=None, help="Filter by bucket (P0/P1/P2).")
@click.option("--competitor", default=None, help="Filter by competitor id.")
def query(since: str | None, bucket: str | None, competitor: str | None) -> None:
    """Query stored briefs. (Stage 4 — not yet implemented.)"""
    click.echo("query: not yet implemented (Stage 4)")
    sys.exit(2)


def main() -> None:
    cli(obj={})


if __name__ == "__main__":
    main()
