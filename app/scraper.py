import logging
from typing import List

import requests
from bs4 import BeautifulSoup

from app.models import Repo

TRENDING_URL = "https://github.com/trending"

logger = logging.getLogger(__name__)



def fetch_trending_repos() -> List[Repo]:
    logger.info("Fetching GitHub trending repositories")
    response = requests.get(TRENDING_URL, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select("article.Box-row")
    repos: List[Repo] = []

    for article in articles:
        title_el = article.select_one("h2 a")
        if not title_el:
            continue

        raw_name = " ".join(title_el.get_text(strip=True).split())
        name = raw_name.replace(" / ", "/")
        url = f"https://github.com{title_el['href']}"

        desc_el = article.select_one("p")
        lang_el = article.select_one("span[itemprop='programmingLanguage']")
        stars_today_el = article.select_one("span.d-inline-block.float-sm-right")

        repos.append(
            Repo(
                name=name,
                url=url,
                description=desc_el.get_text(" ", strip=True) if desc_el else "",
                language=lang_el.get_text(strip=True) if lang_el else "Unknown",
                stars_today=stars_today_el.get_text(" ", strip=True) if stars_today_el else "N/A",
            )
        )

    logger.info("Fetched %d trending repositories", len(repos))
    return repos
