"""Bot runner."""
import logging

from aiogram import Dispatcher, filters
from aiogram.utils import executor

from app import buttons, common_handlers
from app.bot_setup import bot
from app.settings import app_settings


def main() -> None:
    """Telegram bot app runner."""
    router = Dispatcher(bot)
    router.register_message_handler(common_handlers.send_welcome, commands=['start', 'help'])

    router.register_message_handler(
        common_handlers.show_info,
        filters.Text(equals=buttons.SHOW_INFO_BUTTON, ignore_case=True),
    )
    router.register_message_handler(
        common_handlers.buy_token,
        filters.Text(equals=buttons.BUY_TOKEN_BUTTON, ignore_case=True),
    )
    router.register_message_handler(
        common_handlers.show_video,
        filters.Text(equals=buttons.SHOW_VIDEO_BUTTON, ignore_case=True),
    )
    router.register_message_handler(
        common_handlers.show_chats,
        filters.Text(equals=buttons.SHOW_CHATS_BUTTON, ignore_case=True),
    )
    router.register_message_handler(
        common_handlers.show_draw,
        filters.Text(equals=buttons.DRAW_BUTTON, ignore_case=True),
    )

    executor.start_polling(router, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
