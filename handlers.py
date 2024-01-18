from aiogram import Router, types, Bot, F
from aiogram.filters import CommandStart, Command
from keyboards import main_keyboard, inline_main_keyboard

router = Router()


@router.message(CommandStart())
async def on_start(message: types.Message, bot: Bot) -> None:
    await message.answer(
        text="Salom",
        reply_markup=inline_main_keyboard.as_markup()
    )
    # users = [99211407, 547187822]
    # for user in users:
    #     await bot.send_message(
    #         chat_id=user,
    #         text="Foydalanuvchilarga xabar"
    #     )
    # await message.answer(text=f"Salom, {message.from_user.full_name}")
    # await message.reply(text=f"Salom, {message.from_user.full_name}")
    # dice = await message.answer_dice(
    #     emoji="🎲"
    # )
    # await message.answer(
    #     text=f"Sizga {dice.dice.value} tushdi"
    # )
    # await message.answer_contact(
    #     phone_number="+998338371703",
    #     first_name="Abduxalil"
    # )
    # await message.answer_location(
    #     latitude=41.2971425,
    #     longitude=69.2755733
    # )
    # await message.answer_poll(
    #     question="Savol",
    #     is_anonymous=False,
    #     type="quiz",
    #     options=[
    #         "Variant 1",
    #         "Variant 2",
    #         "Variant 3",
    #         "Variant 4",
    #     ],
    #     correct_option_id=3,
    #     explanation="Tabriklaymiz"
    # )
    # await message.answer_document(
    #     document=
    # )


@router.message(F.text == "🇺🇿 1 chi tugma")
async def on_btn_click(message: types.Message) -> None:
    await message.answer(
        text="Siz 1 chi tugmani bosdingiz"
    )


@router.message(F.text == "2 chi tugma")
async def on_btn_click(message: types.Message) -> None:
    await message.answer(
        text="Siz 2 chi tugmani bosdingiz"
    )


@router.callback_query(F.data == "first")
async def on_first_button(callback: types.CallbackQuery):
    # await callback.answer()
    await callback.answer(
        text="1 chi tugma bosildi",
        show_alert=True
    )


@router.message(F.contact)
async def get_contact(message: types.Message) -> None:
    await message.answer(
        text=f"Sizning raqamingiz {message.contact.phone_number}"
    )

# Reply knopkalar


@router.message(F.location)
async def get_location(message: types.Message) -> None:
    await message.answer(
        text=f"Sizning joylashuvingiz {message.location.latitude} {message.location.longitude}"
    )
# @router.message(F.photo | F.text | F.video | F.sticker | F.animation)
# async def get_photo(message: types.Message) -> None:
#     await message.answer(
#         text="Siz photo yoki text yubordingiz"
#     )


@router.message(Command(commands=['help', 'settings']))
async def on_help(message: types.Message) -> None:
    await message.answer(
        text="Qanday yordam kerak?"
    )