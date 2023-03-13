"""Common bot handlers."""

from aiogram import types

from app.bot_setup import bot
from app.buttons import BUY_TOKEN_BUTTON, SHOW_CHATS_BUTTON, SHOW_INFO_BUTTON, SHOW_VIDEO_BUTTON
from app.settings import app_settings


async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text = 'Добро пожаловать в сообщество SegaGameClub!'

    await message.answer(answer_text, reply_markup=_get_keyboard())


async def show_info(message: types.Message) -> None:
    """Show main info."""
    answer_text = """
*SegaGameClub* — это игровое сообщество, объединившее в себе игровое комьюнити и разработчиков игр Play2Earn, в одну экосистему.
Наша бизнес-модель создает мощную синергию между вами, сообществом и партнерами сообщества.

*Конечная цель* - стать крупнейшим и самым быстрорастущим игровым сообществом в мире.

Главные ссылки *SegaGameClub*:
🗺 [Главный документ и карта развития](https://segagame.io/whitepaper.pdf).
🎮 [Как начать играть?](https://telegra.ph/Kak-nachat-igrat-v-SegaGameClub-02-21)
💵 [Как добавить сеть Binance Smart Chain в MetaMask](https://telegra.ph/Instrukciya-kak-dobavit-Binance-Smart-Chain-BSC-v-koshelek-MetaMask-02-02-2)?
🪙 [Способы заработка в SegaGameClub](https://telegra.ph/Kak-nachat-zarabatyvat-v-SegaGameClub-01-25).
❔ [Как купить SegaToken на бирже Pancake Swap](https://telegra.ph/Kak-kupit-SegaToken-na-birzhe-Pancake-Swap-01-30-3).

*Ссылки на социальные сети:*
🌍 [Website](https://segagame.io/)
✅ [Twitter](https://twitter.com/SegaGameClub)
📸 [Instagram](https://instagram.com/segagame.io?igshid=MjkzY2Y1YTY=)
✅ [Telegram EN](https://t.me/segagameclub_official)
✅ [Telegram RU](https://t.me/segagameclub_channel_ru)
    """

    await message.answer(
        answer_text,
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=_get_keyboard(),
    )


async def buy_token(message: types.Message) -> None:
    """Show info about buying token."""
    answer_text = """
📈 [DEX Tools](https://www.dextools.io/app/ru/bnb/pair-explorer/0x26d7b2c715ed42adbeb0e0fd989eadacf5167ead) (для просмотра графика токена).
🐰 [Pancake Swap](https://pancakeswap.finance/swap?outputCurrency=0xCfc9854c77dC73C39F94E597371712Ba15de6eD2&inputCurrency=BNB) (для покупки и обмена токена).
📃 [Как купить SegaToken на бирже Pancake Swap](https://telegra.ph/Kak-kupit-SegaToken-na-birzhe-Pancake-Swap-01-30-3).


Официальный контракт *SegaToken*:

0xcfc9854c77dc73c39f94e597371712ba15de6ed2
    """

    photo = types.InputFile(f'{app_settings.assets_path}/token_logo.jpg')

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=answer_text,
        parse_mode='Markdown',
        reply_markup=_get_keyboard(),
    )


async def show_video(message: types.Message) -> None:
    """Show video."""
    answer_text = '*Долгожданные видео инструкции SegaGameClub!*'

    await types.ChatActions.upload_video()
    media = types.MediaGroup()

    media.attach_video(
        types.InputFile(f'{app_settings.assets_path}/video_1.MP4'),
        caption=answer_text,
        parse_mode='markdown',
    )
    media.attach_video(
        types.InputFile(f'{app_settings.assets_path}/video_2.MP4'),
    )
    media.attach_video(
        types.InputFile(f'{app_settings.assets_path}/video_3.MP4'),
    )
    media.attach_video(
        types.InputFile(f'{app_settings.assets_path}/video_4.MP4'),
    )
    media.attach_video(
        types.InputFile(f'{app_settings.assets_path}/video_5.MP4'),
    )
    media.attach_video(
        types.InputFile(f'{app_settings.assets_path}/video_6.MP4'),
    )

    await message.answer_media_group(media=media)


async def show_chats(message: types.Message) -> None:
    """Show links to other chats."""
    answer_text = """
*Наши Telegram чаты*

🆘 [Support Sega](https://t.me/+SMnigZKMGLEwMzA0)
🇷🇺 [Telegram Chanel_RU](https://t.me/segagameclub_channel_ru)
🇷🇺 [Telegram Chat_RU](https://t.me/segagameclubchat)
🇺🇸 [Telegram Chanel_EN](https://t.me/segagameclub_official)
🇺🇸 [Telegram Chat_EN](https://t.me/segagameclubchat_en)
🇰🇿 [Telegram Chat_KZ](https://t.me/segagamekz)
    """

    await message.answer(
        answer_text,
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=_get_keyboard(),
    )


async def show_draw(message: types.Message) -> None:
    """Show conditions of draw."""
    answer_text = """
 нужно чтобы человек подписывался на соц сети, нажимал "готово" и ему за это падал приз
    """

    await message.answer(
        answer_text,
        reply_markup=_get_keyboard(),
    )


def _get_keyboard() -> types.ReplyKeyboardMarkup:
    """Return the keyboard markup."""
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).row(
        types.KeyboardButton(SHOW_INFO_BUTTON),
        types.KeyboardButton(BUY_TOKEN_BUTTON),
    ).row(
        types.KeyboardButton(SHOW_VIDEO_BUTTON),
        types.KeyboardButton(SHOW_CHATS_BUTTON),
    )
