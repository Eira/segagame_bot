"""Bot runner."""
import logging

from aiogram import Bot

from app.settings import app_settings

bot = Bot(token=app_settings.bot_token)


def main() -> None:
    """Telegram bot app runner."""


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
