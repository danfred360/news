from functools import lru_cache
from typing import Final, final

from pydantic_settings import BaseSettings, SettingsConfigDict


@lru_cache()
def get_config():
    """Get the configuration for the application. This is cached for performance."""
    return Config()


@final
class Config(BaseSettings):
    app_name: str = "news"
    news_api_key: Final[str]
    postgres_user: Final[str]
    postgres_password: Final[str]
    postgres_db: Final[str]
    database_url: Final[str]

    model_config = SettingsConfigDict(env_file=".env")
