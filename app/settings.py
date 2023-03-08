"""Application settings."""
import os

from pydantic.env_settings import BaseSettings


class AppSettings(BaseSettings):
    """Application settings class."""

    bot_token: str


app_settings = AppSettings(
    _env_file=os.path.join(os.path.dirname(__file__), '..', '.env'),
)
