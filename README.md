# GitHub Trend Bot

Daily Python bot that scrapes GitHub Trending, filters AI/Cybersecurity repos, generates short technical summaries, and posts top results to Telegram while avoiding duplicates.

## Features
- Scrapes GitHub Trending page
- Keyword-based filtering for AI and Cybersecurity
- Short technical explanation generation from repo metadata
- Telegram channel posting via bot API
- Duplicate prevention with local state file
- Daily scheduled run
- Structured logging

## Project Structure
- `app/config.py` - environment-driven settings
- `app/logging_setup.py` - logger configuration
- `app/models.py` - data model for repositories
- `app/scraper.py` - trending scraper
- `app/filtering.py` - domain filtering
- `app/explainer.py` - technical explanation generator
- `app/storage.py` - duplicate tracking
- `app/telegram_client.py` - Telegram sender
- `app/pipeline.py` - end-to-end workflow
- `app/scheduler.py` - daily scheduler
- `main.py` - entrypoint

## Setup
1. Create virtual environment and install dependencies.
2. Export required environment variables (see `.env.example`).
3. Run once:
   ```bash
   python main.py --run-once
   ```
4. Run daily scheduler:
   ```bash
   python main.py
   ```

## Notes
- Keep bot token and channel ID private.
- Trending parsing relies on GitHub page HTML and may need updates if layout changes.
