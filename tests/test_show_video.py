from unittest.mock import AsyncMock

from app.common_handlers import show_video


async def test_show_video_smoke(mocker):
    mock = mocker.patch('app.common_handlers.types.ChatActions.upload_video')

    message_mock = AsyncMock()

    await show_video(message_mock)

    assert True
    assert mock.call_count == 1
