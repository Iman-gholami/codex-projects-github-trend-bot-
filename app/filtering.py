from typing import List

from app.models import Repo

AI_KEYWORDS = {
    "ai",
    "llm",
    "ml",
    "machine learning",
    "deep learning",
    "neural",
    "genai",
    "gpt",
    "transformer",
    "rag",
}

CYBER_KEYWORDS = {
    "cyber",
    "security",
    "pentest",
    "malware",
    "exploit",
    "forensics",
    "threat",
    "vulnerability",
    "ctf",
    "siem",
}



def _repo_blob(repo: Repo) -> str:
    return f"{repo.name} {repo.description}".lower()



def filter_ai_and_cybersecurity(repos: List[Repo]) -> List[Repo]:
    filtered: List[Repo] = []
    for repo in repos:
        blob = _repo_blob(repo)
        if any(k in blob for k in AI_KEYWORDS) or any(k in blob for k in CYBER_KEYWORDS):
            filtered.append(repo)
    return filtered
