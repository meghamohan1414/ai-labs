import logging

from config import get_settings
from logging_utils import setup_logging


def run() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)

    logger = logging.getLogger("ai-labs")
    logger.info("App starting", extra={"app_name": settings.app_name, "env": settings.env})
    logger.info("Loaded config: app_name=%s env=%s", settings.app_name, settings.env)


if __name__ == "__main__":
    run()
