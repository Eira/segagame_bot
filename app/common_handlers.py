"""Common bot handlers."""

from aiogram import types
from aiogram.utils.markdown import link

from app.buttons import SHOW_INFO_BUTTON, BUY_TOKEN_BUTTON, SHOW_VIDEO_BUTTON, SHOW_CHATS_BUTTON, DRAW_BUTTON


async def send_welcome(message: types.Message) -> None:
    """Greeting user when user sends `/start` or `/help` command."""
    answer_text = 'Hi!'

    button_show_info = types.KeyboardButton(SHOW_INFO_BUTTON)
    button_buy_token = types.KeyboardButton(BUY_TOKEN_BUTTON)
    button_video = types.KeyboardButton(SHOW_VIDEO_BUTTON)
    button_chats = types.KeyboardButton(SHOW_CHATS_BUTTON)
    button_draw = types.KeyboardButton(DRAW_BUTTON)

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
    ).row(
        button_show_info, button_buy_token,
    ).row(
        button_video, button_chats,
    ).add(
        button_draw,
    )

    await message.answer(answer_text, reply_markup=markup)


async def show_info(message: types.Message) -> None:
    """Show main info."""
    answer_text = """
🗺 [Главный документ и карта развития](https://segagame.io/whitepaper.pdf).
🎮 [Как начать играть?](https://telegra.ph/Kak-nachat-igrat-v-SegaGameClub-02-21)
🔶 [Как добавить сеть Binance Smart Chain в MetaMask](https://telegra.ph/Instrukciya-kak-dobavit-Binance-Smart-Chain-BSC-v-koshelek-MetaMask-02-02-2)?
🪙 [Способы заработка в SegaGameClub](https://telegra.ph/Kak-nachat-zarabatyvat-v-SegaGameClub-01-25).

*Ссылки на социальные сети:*
🌍 [Website](https://segagame.io/)
✅ [Twitter](https://twitter.com/SegaGameClub)
📸 [Instagram](https://instagram.com/segagame.io?igshid=MjkzY2Y1YTY=)
✅ [Telegram EN](https://t.me/segagameclub_official)
✅ [Telegram RU](https://t.me/segagameclub_channel_ru)
    """

    await message.answer(answer_text, parse_mode='Markdown', disable_web_page_preview=True)


async def buy_token(message: types.Message) -> None:
    answer_text = """
📈 [DEX Tools](https://www.dextools.io/app/ru/bnb/pair-explorer/0x26d7b2c715ed42adbeb0e0fd989eadacf5167ead) (для просмотра графика токена).
🐰 [Pancake Swap](https://pancakeswap.finance/swap?outputCurrency=0xCfc9854c77dC73C39F94E597371712Ba15de6eD2&inputCurrency=BNB) (для покупки и обмена токена).
❔ [Как купить SegaToken на бирже Pancake Swap](https://telegra.ph/Kak-kupit-SegaToken-na-birzhe-Pancake-Swap-01-30-3).
    """

    await message.answer(answer_text, parse_mode='Markdown', disable_web_page_preview=True)


async def show_video(message: types.Message) -> None:
    answer_text = """
     видео обучающие
    """

    await message.answer(answer_text, parse_mode='Markdown', disable_web_page_preview=True)


async def show_chats(message: types.Message) -> None:
    answer_text = """
        чатами и каналами в тг
    """

    await message.answer(answer_text, parse_mode='Markdown', disable_web_page_preview=True)


async def show_draw(message: types.Message) -> None:
    answer_text = """
 нужно чтобы человек подписывался на соц сети, нажимал "готово" и ему за это падал приз
    """

    await message.answer(answer_text)
