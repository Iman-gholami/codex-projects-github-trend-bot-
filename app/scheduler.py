import logging
import time

import schedule

from app.config import Settings
from app.pipeline import run_daily_pipeline

logger = logging.getLogger(__name__)



def run_scheduler(settings: Settings) -> None:
    schedule.every().day.at(settings.run_time_utc).do(run_daily_pipeline, settings=settings)
    logger.info("Scheduler started. Job set for %s UTC daily", settings.run_time_utc)

    while True:
        schedule.run_pending()
        time.sleep(1)
