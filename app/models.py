from dataclasses import dataclass


@dataclass(frozen=True)
class Repo:
    name: str
    url: str
    description: str
    language: str
    stars_today: str
