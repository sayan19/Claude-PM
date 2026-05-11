# Template: drop into .github/workflows/soti-compete.yml to schedule on GitHub-hosted runners.
#
# GitHub cron is UTC-only and ignores timezones. The schedule below fires at:
#   - 11:00 UTC daily = 07:00 EDT (Mar–Nov) / 06:00 EST (Nov–Mar)
#   - top of every hour for the P0 sweep
#
# If you need strict 07:00 America/Toronto year-round, use a self-hosted runner with
# crontab and TZ=America/Toronto, or a cloud scheduler that honours IANA timezones
# (AWS EventBridge, GCP Cloud Scheduler, Azure Logic Apps).
#
# IMPORTANT: this template uploads data/ as a build artifact for inspection, but artifacts
# do NOT persist between runs. Cross-run dedup needs durable storage — point
# runtime.yaml at S3+JSONL or Postgres before relying on the dedup window in CI.
name: soti-compete

on:
  schedule:
    - cron: "0 11 * * *"   # daily (see DST note above)
    - cron: "0 * * * *"    # hourly P0 sweep
  workflow_dispatch:
    inputs:
      flow:
        description: "Which flow to run"
        type: choice
        options: [daily, hourly, sentiment, healthcheck]
        default: healthcheck

jobs:
  scan:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    defaults:
      run:
        working-directory: soti-compete
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -e .
      - name: Pick flow
        id: pick
        run: |
          if [[ "${{ github.event_name }}" == "workflow_dispatch" ]]; then
            echo "flow=${{ inputs.flow }}" >> "$GITHUB_OUTPUT"
          elif [[ "${{ github.event.schedule }}" == "0 * * * *" ]]; then
            echo "flow=hourly" >> "$GITHUB_OUTPUT"
          else
            echo "flow=daily" >> "$GITHUB_OUTPUT"
          fi
      - name: Run flow
        run: soti-compete "${{ steps.pick.outputs.flow }}"
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          SMTP_HOST: ${{ secrets.SMTP_HOST }}
          SMTP_PORT: ${{ secrets.SMTP_PORT }}
          SMTP_USERNAME: ${{ secrets.SMTP_USERNAME }}
          SMTP_PASSWORD: ${{ secrets.SMTP_PASSWORD }}
          SMTP_FROM: ${{ secrets.SMTP_FROM }}
          TEAMS_WEBHOOK_URL: ${{ secrets.TEAMS_WEBHOOK_URL }}
      - name: Upload data artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: data-${{ steps.pick.outputs.flow }}-${{ github.run_id }}
          path: soti-compete/data/
          retention-days: 14
