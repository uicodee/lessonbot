from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


# builder = ReplyKeyboardBuilder()
main_keyboard = ReplyKeyboardBuilder()
# for i in range(1, 17):
#     builder.add(types.KeyboardButton(text=str(i)))
# builder.adjust(4)
# main_keyboard.button(
#     text="🇺🇿 1 chi tugma"
# )
# main_keyboard.button(
#     text="2 chi tugma"
# )
main_keyboard.button(
    text="Telefon raqamini ulashish",
    request_contact=True
)
main_keyboard.button(
    text="Joylashuvni ulashish",
    request_location=True
)
main_keyboard.button(
    text="Viktorina yaratish",
    request_poll=types.KeyboardButtonPollType(type="poll")
)
main_keyboard.button(
    text="Foydalanuvchi tanlash",
    request_user=types.KeyboardButtonRequestUser(
        request_id=1,
        user_is_bot=True
    )
)
main_keyboard.button(
    text="Premium tanlash",
    request_user=types.KeyboardButtonRequestUser(
        request_id=2,
        user_is_premium=True
    )
)
main_keyboard.button(
    text="Gurux tanlash",
    request_chat=types.KeyboardButtonRequestChat(
        request_id=3,
        chat_is_channel=True
    )
)
main_keyboard.adjust(1)


inline_main_keyboard = InlineKeyboardBuilder()
inline_main_keyboard.button(
    text="1 chi tugma",
    callback_data="first"
)
inline_main_keyboard.button(
    text="2 chi tugma",
    callback_data="second"
)
inline_main_keyboard.button(
    text="3 chi tugma",
    callback_data="third"
)
inline_main_keyboard.button(
    text="GitHub",
    url="https://t.me/uicodee"
)
