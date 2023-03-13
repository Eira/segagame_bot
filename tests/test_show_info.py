from unittest.mock import AsyncMock

from app.common_handlers import show_info


async def test_show_info_smoke():
    message_mock = AsyncMock()

    await show_info(message_mock)

    assert True
