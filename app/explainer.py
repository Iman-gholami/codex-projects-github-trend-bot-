from app.models import Repo



def generate_technical_explanation(repo: Repo) -> str:
    base_desc = repo.description or "No description provided."
    return (
        f"{repo.name} is a {repo.language} project currently trending on GitHub. "
        f"It appears focused on: {base_desc} "
        f"Signal: {repo.stars_today}."
    )
