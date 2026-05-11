# Template: drop into .github/workflows/ to schedule on GitHub-hosted runners.
name: soti-compete

on:
  schedule:
    - cron: "0 11 * * *"   # 07:00 America/Toronto during DST (EDT = UTC-4)
    - cron: "0 12 * * *"   # 07:00 America/Toronto during EST (UTC-5); GitHub doesn't honor tz
    - cron: "0 * * * *"    # hourly P0 sweep
  workflow_dispatch:

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -e .
      - name: Daily scan
        if: github.event.schedule != '0 * * * *'
        run: soti-compete daily
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          SMTP_HOST: ${{ secrets.SMTP_HOST }}
          SMTP_PORT: ${{ secrets.SMTP_PORT }}
          SMTP_USERNAME: ${{ secrets.SMTP_USERNAME }}
          SMTP_PASSWORD: ${{ secrets.SMTP_PASSWORD }}
          SMTP_FROM: ${{ secrets.SMTP_FROM }}
          TEAMS_WEBHOOK_URL: ${{ secrets.TEAMS_WEBHOOK_URL }}
      - name: Hourly sweep
        if: github.event.schedule == '0 * * * *'
        run: soti-compete hourly
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          TEAMS_WEBHOOK_URL: ${{ secrets.TEAMS_WEBHOOK_URL }}
      - name: Upload data
        uses: actions/upload-artifact@v4
        with:
          name: data
          path: data/
