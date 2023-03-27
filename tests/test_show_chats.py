from unittest.mock import AsyncMock

from app.common_handlers import show_chats


async def test_show_chats_smoke():
    message_mock = AsyncMock()

    await show_chats(message_mock)

    assert message_mock.answer.call_count == 1
