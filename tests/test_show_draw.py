from unittest.mock import AsyncMock

from app.common_handlers import show_draw


async def test_show_draw_smoke():
    message_mock = AsyncMock()

    await show_draw(message_mock)

    assert True
