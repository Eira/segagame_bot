"""bot token."""

from aiogram import Bot

from app.settings import app_settings

bot = Bot(token=app_settings.bot_token)
