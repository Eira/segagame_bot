# segagame_bot

[![linters](https://github.com/Eira/segagame_bot/actions/workflows/linters.yml/badge.svg?branch=main)](https://github.com/Eira/segagame_bot/actions/workflows/linters.yml)

Simple bot for the project SegaGame.

### Links
[Stage bot](t.me/SegaGame_stage_bot)

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

### Local run linters
```
poetry run flake8 app/

poetry run mypy app/
```
