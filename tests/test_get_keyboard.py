from app.common_handlers import _get_keyboard


def test_get_keyboard_smoke():

    res = _get_keyboard()

    assert [b.text for b in res.keyboard[0]] == ['Инфо', 'Купить токен']
    assert [kb.text for kb in res.keyboard[1]] == ['Видео', 'Чаты']
