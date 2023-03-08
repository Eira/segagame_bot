"""Bot runner."""
import logging

from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from app import common_handlers
from app.settings import app_settings

bot = Bot(token=app_settings.bot_token)


def main() -> None:
    """Telegram bot app runner."""
    router = Dispatcher(bot)
    router.register_message_handler(common_handlers.send_welcome, commands=['start', 'help'])

    executor.start_polling(router, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
