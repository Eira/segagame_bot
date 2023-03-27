from unittest.mock import AsyncMock

from app.common_handlers import buy_token


async def test_buy_token_smoke(mocker):
    mock = mocker.patch('app.common_handlers.bot.send_photo')
    message_mock = AsyncMock()

    await buy_token(message_mock)

    assert mock.call_count == 1
