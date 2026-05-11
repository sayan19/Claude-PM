#!/usr/bin/env bash
# Example crontab entry:
#   0 7 * * *  /opt/soti-compete/scripts/cron-daily.sh >> /var/log/soti-compete/daily.log 2>&1
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ -f .env ]]; then
    set -a; source .env; set +a
fi

exec ./.venv/bin/soti-compete daily
