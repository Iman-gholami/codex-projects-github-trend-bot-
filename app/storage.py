import json
import os
from typing import Set



def load_posted_repos(path: str) -> Set[str]:
    if not os.path.exists(path):
        return set()

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return set(data if isinstance(data, list) else [])



def save_posted_repos(path: str, posted: Set[str]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sorted(posted), f, indent=2)
