import logging
from typing import List

from app.config import Settings
from app.explainer import generate_technical_explanation
from app.filtering import filter_ai_and_cybersecurity
from app.models import Repo
from app.scraper import fetch_trending_repos
from app.storage import load_posted_repos, save_posted_repos
from app.telegram_client import TelegramClient

logger = logging.getLogger(__name__)



def format_message(repo: Repo, explanation: str) -> str:
    return (
        f"📌 {repo.name}\n"
        f"🔗 {repo.url}\n"
        f"💻 Language: {repo.language}\n"
        f"⭐ {repo.stars_today}\n"
        f"🧠 {explanation}"
    )



def run_daily_pipeline(settings: Settings) -> None:
    logger.info("Running daily pipeline")

    all_repos = fetch_trending_repos()
    candidate_repos = filter_ai_and_cybersecurity(all_repos)
    posted = load_posted_repos(settings.state_file)

    new_repos: List[Repo] = [repo for repo in candidate_repos if repo.url not in posted]
    selected = new_repos[: settings.max_repos_per_day]

    if not selected:
        logger.info("No new AI/Cybersecurity repositories to post today")
        return

    telegram = TelegramClient(settings.telegram_bot_token, settings.telegram_channel_id)

    posted_count = 0

    for repo in selected:
        explanation = generate_technical_explanation(repo)
        telegram.send_message(format_message(repo, explanation))
        posted.add(repo.url)
        save_posted_repos(settings.state_file, posted)
        posted_count += 1
        logger.info("Posted repository: %s", repo.name)

    logger.info("Daily pipeline completed. Posted %d repositories", posted_count)
