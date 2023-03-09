"""Application settings."""
import os

from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    """Application settings class."""

    bot_token: str
    debug: bool = Field(False, description='настройка уровня логирования')

    assets_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'assets'),
    )


app_settings = AppSettings(
    _env_file=os.path.join(os.path.dirname(__file__), '..', '.env'),  # type: ignore
)


