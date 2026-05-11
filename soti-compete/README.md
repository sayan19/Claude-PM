# SOTI Compete

Automated competitive intelligence for SOTI's PM team. Runs a daily 7am scan
(Toronto time) plus hourly P0 sweeps against a configured list of MDM/UEM
competitors — Jamf, Omnissa, Microsoft Intune, Ivanti, MaaS360, 42Gears,
Hexnode, Scalefusion, Samsung Knox — scores each item across five weighted
dimensions, and routes:

| Bucket | Threshold | Routing |
|---|---|---|
| P0 | final &ge; 7.5 | Email to leadership + PMM **and** Teams alert per item |
| P1 | 5.0–7.49 | Daily digest email to PM team |
| P2 | 2.5–4.99 | Persisted for weekly review |
| DROP | < 2.5 | Dropped |

Sales / CSMs can also paste intel on-demand. A monthly job aggregates Reddit,
Peerspot, and G2 sentiment per competitor.

## Setup

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

cp .env.example .env
# Fill in ANTHROPIC_API_KEY, SMTP_*, TEAMS_WEBHOOK_URL

# Review and edit config/*.yaml — recipients, competitor list, tier-1 domains.
```

## Commands

```bash
soti-compete healthcheck                 # verify integrations
soti-compete daily                       # 7am scan
soti-compete hourly                      # P0 sweep on direct competitors
soti-compete pastein -t "..."            # ad hoc score-and-route (text)
soti-compete pastein -f intel.txt        # ad hoc from file
cat intel.txt | soti-compete pastein     # from stdin
soti-compete sentiment                   # monthly snapshot
soti-compete query --since 7d --bucket P0
soti-compete query --competitor jamf --flow daily
```

Every command honours `SOTI_COMPETE_DRY_RUN=true` (skip SMTP/Teams sends,
write `.eml` and Teams JSON to `data/outbox/` instead). Useful for first runs
and for CI smoke checks.

## Configuration

Five YAML files in `config/`. PMs can edit these without touching Python.

| File | What lives here |
|---|---|
| `competitors.yaml` | competitor IDs, tiers (direct/adjacent), aliases, search hints |
| `scoring.yaml` | dimension weights, recency curves (default + acquisition), confidence multipliers, bucket cutoffs |
| `sources.yaml` | tier-1 press domain whitelist, analyst domains, vendor PR domains, blocked domains, sentiment platforms |
| `routing.yaml` | email recipients per bucket, Teams webhook env var |
| `runtime.yaml` | model id, timezone, storage backend, web_search budgets, dedup window, per-flow lookbacks |

## Scoring

5 dimensions, each 0–10, weighted:

- **Strategic Impact** (30%) — market-position effect on SOTI
- **Sales Signal** (25%) — Phase 1 default 4 unless news describes deal motion (then 6)
- **Roadmap Overlap** (20%) — Phase 1 capped conservatively until Jira is wired
- **Competitor Tier** (15%) — direct=10, adjacent=6 (system-computed)
- **Source Quality** (10%) — SEC/vendor/analyst=10, tier-1 press=8, secondary=5, blog/forum=2

```
raw = Σ(dimension × weight) / 100, capped at 10
final = raw × recency × confidence
```

**Recency** (system-computed from `published_at`):
- Default: 0–7d=1.0, 8–30d=0.7, 31–90d=0.4, 91+=0.2
- Acquisition (slower news cycle): 0–14d=1.0, 15–60d=0.7, 61–180d=0.4, 181+=0.2

**Confidence**: 2+ sources or 1 tier-1 = 1.0, single = 0.8, rumor = 0.5

Source quality is the `max` of the LLM's score and the score derived from the
primary source domain. Catches the case where the model under-rates a known
tier-1 cite.

## Phase 3 stubs

Salesforce, Gong, and Jira/Productboard integrations are stubs that log
`[STUB]` and return placeholder data — so Phase 1 produces usable briefs
today without those systems connected. When you wire them in, only the
function bodies in `soti_compete/stubs/` change.

## Layout

```
config/        YAML configs (PM-editable)
soti_compete/  Python package
  llm/         Anthropic SDK wrapper, prompts, web_search budget
  flows/       daily_scan, hourly_sweep, pastein, sentiment_monthly + shared pipeline
  storage/     Storage interface + SQLite backend
  notify/      SMTP, Teams, brief renderer
  stubs/       Phase 3 wire-in points
tests/         pytest suite (no network, no Anthropic calls)
scripts/       cron + GitHub Actions templates
data/          SQLite DB + outbox (gitignored)
```

## Storage

SQLite by default at `data/soti_compete.db`. Two tables:

- `briefs` — one row per scored item, with dedup fingerprint, dimensions JSON,
  gap analysis JSON, sources JSON, full LLM payload JSON.
- `sentiment_snapshots` — one row per competitor per month.

The `Storage` protocol in `soti_compete/storage/base.py` is the migration
target — Postgres or S3+JSONL backends can drop in without touching flows.

## Scheduling

`scripts/cron-daily.sh` is for VM crontab. `scripts/github-actions.yml.tpl`
is a starter for GitHub-hosted runners — read the DST note at the top before
relying on it. For strict 07:00 America/Toronto year-round, prefer a
self-hosted runner with `TZ=America/Toronto` or AWS EventBridge / GCP Cloud
Scheduler.

## Tests

```bash
pytest tests/ -q          # full suite, ~2s, no network
pytest tests/test_jsonl.py -q
pytest tests/test_scoring.py tests/test_recency.py -q
ruff check soti_compete tests
```

Flow tests inject a `FakeLLM` so the Anthropic API is never reached. The
`tests/test_e2e_smoke.py` drives the CLI end-to-end through Click's
`CliRunner` with a captured JSONL fixture at
`tests/fixtures/daily_response.jsonl` — edit that to reproduce specific
real-world responses.
