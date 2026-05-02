import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    telegram_bot_token: str
    telegram_channel_id: str
    run_time_utc: str = "09:00"
    state_file: str = ".posted_repos.json"
    log_level: str = "INFO"
    max_repos_per_day: int = 5



def load_settings() -> Settings:
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    channel_id = os.getenv("TELEGRAM_CHANNEL_ID", "").strip()
    if not token or not channel_id:
        raise ValueError("TELEGRAM_BOT_TOKEN and TELEGRAM_CHANNEL_ID must be set")

    return Settings(
        telegram_bot_token=token,
        telegram_channel_id=channel_id,
        run_time_utc=os.getenv("RUN_TIME_UTC", "09:00"),
        state_file=os.getenv("STATE_FILE", ".posted_repos.json"),
        log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
    )
