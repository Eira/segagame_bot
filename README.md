# segagame_bot

[![linters](https://github.com/Eira/segagame_bot/actions/workflows/linters.yml/badge.svg?branch=main)](https://github.com/Eira/segagame_bot/actions/workflows/linters.yml)
[![tests](https://github.com/Eira/segagame_bot/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Eira/segagame_bot/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/Eira/segagame_bot/branch/main/graph/badge.svg?token=VBFPMKSW3L)](https://codecov.io/gh/Eira/segagame_bot)

Information bot for the project SegaGame.

### Links
[Stage bot](https://t.me/SegaGame_stage_bot)

### Local setup
```shell
$ git clone git@github.com:Eira/segagame_bot.git
$ cd segagame_bot
$ python3.11 -m venv venv
$ source venv/bin/activate
$ pip install -U poetry
$ poetry install
```

### Local run Telegram bot
```
python -m app.bot_runner
```

### Local run tests
```shell
$ python -m pytest
```

### Local run linters
```
poetry run flake8 app/

poetry run mypy app/
```
