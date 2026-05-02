import argparse

from app.config import load_settings
from app.logging_setup import configure_logging
from app.pipeline import run_daily_pipeline
from app.scheduler import run_scheduler



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GitHub AI/Cybersecurity trend bot")
    parser.add_argument("--run-once", action="store_true", help="Run pipeline once and exit")
    return parser.parse_args()



def main() -> None:
    args = parse_args()
    settings = load_settings()
    configure_logging(settings.log_level)

    if args.run_once:
        run_daily_pipeline(settings)
    else:
        run_scheduler(settings)


if __name__ == "__main__":
    main()
