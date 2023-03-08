"""Common bot handlers."""

from aiogram import types

CREATE_INFO_BUTTON = 'Info'


async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text = 'Hi!'

    button_create_search = types.KeyboardButton(CREATE_INFO_BUTTON)
    start_search_kb = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
    ).add(button_create_search)

    await message.answer(answer_text, reply_markup=start_search_kb)
