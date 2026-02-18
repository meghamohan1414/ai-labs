import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Settings:
    app_name: str
    log_level: str
    env: str


def get_settings() -> Settings:
    load_dotenv()  # loads .env into environment variables
    return Settings(
        app_name=os.getenv("APP_NAME", "ai-labs"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        env=os.getenv("ENV", "dev"),
    )
