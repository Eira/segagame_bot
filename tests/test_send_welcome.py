from unittest.mock import AsyncMock

from app.common_handlers import send_welcome, _get_keyboard


async def test_bot_send_welcome_happy_path():
    expected_answer = 'Добро пожаловать в сообщество SegaGameClub!'
    message_mock = AsyncMock()

    await send_welcome(message=message_mock)

    assert message_mock.answer.await_args.args[0] == expected_answer
    assert message_mock.answer.await_args.kwargs.get('reply_markup') == _get_keyboard()
