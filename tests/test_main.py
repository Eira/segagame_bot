from app.bot_runner import main


def test_main_smoke():
    # todo ask how to do it
    res = main()

    assert res is None
