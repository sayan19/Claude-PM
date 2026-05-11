# SOTI Compete

Automated competitive intelligence pipeline for SOTI's PM team.

Runs a daily 7am scan plus hourly P0 sweeps against a configured list of MDM/UEM
competitors (Jamf, Omnissa, Microsoft Intune, Ivanti, MaaS360, 42Gears, Hexnode,
Scalefusion, Samsung Knox), scores each item, and routes results:

- **P0 (>=7.5)** -> email to leadership + PMM, Teams alert
- **P1 (5.0-7.49)** -> daily digest email to PM team
- **P2 (2.5-4.99)** -> persisted for weekly review
- **<2.5** -> dropped

A monthly job aggregates public sentiment across Reddit, Peerspot, and G2 for
each tracked competitor.

## Setup

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

cp .env.example .env
# Fill in ANTHROPIC_API_KEY, SMTP_*, TEAMS_WEBHOOK_URL

# Review and edit config/*.yaml
```

## Commands

```bash
soti-compete healthcheck                 # verify integrations
soti-compete daily                       # 7am scan
soti-compete hourly                      # P0 sweep on direct competitors
soti-compete pastein --file intel.txt    # ad hoc score-and-route
soti-compete sentiment                   # monthly snapshot
soti-compete query --since 7d --bucket P0
```

All commands accept `--dry-run` to skip outbound email/Teams calls.

## Layout

```
config/        YAML configs (competitors, scoring, sources, routing, runtime)
soti_compete/  Python package
tests/         pytest suite (no network)
scripts/       cron + GitHub Actions templates
data/          SQLite DB + outbox (gitignored)
```

## Status

Phase 1 in progress. Phase 3 integrations (Salesforce, Gong, Jira) are stubs
that log `[STUB]` and return placeholder data.
