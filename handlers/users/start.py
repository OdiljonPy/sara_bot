from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.register_state import Lang, RegisterRu, RegisterUz
from utils.misc.is_admin import is_admin
from utils.misc.is_register import is_register
from aiogram.dispatcher import FSMContext
from keyboards.default.select_lang import select_lang
from loader import dp


@dp.message_handler(CommandStart(), lambda message: is_admin(user_id=message.from_user.id))
async def bot_start(message: types.Message):
    await message.answer(f"Salom Admin, {message.from_user.full_name}")


@dp.message_handler(CommandStart(), lambda message: is_register(user_id=message.from_user.id))
async def bot_start(message: types.Message):
    await message.answer(text=f"Assalomu alaykum. Botimizga xush kelibsiz☺"
                              f"\nFoydalanish uchun ro'yxatdan o'tishingiz kerak\n"
                              f"\n\nIltimos tilni tanlang !"
                              f"\nПожалуйста, выберите язык !",
                         reply_markup=select_lang
                         )
    await Lang.lang.set()


@dp.message_handler(lambda message: message.text == 'Uzb', state=Lang.lang)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Ismingizni kiriting !",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.update_data({'lan': 'uz'})
    await RegisterUz.fullname.set()


@dp.message_handler(lambda message: message.text == 'Rus', state=Lang.lang)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"\nВведите ваше имя !",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.update_data({'lan': 'ru'})
    await RegisterRu.fullname.set()


@dp.message_handler(state=Lang.lang)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Assalomu alaykum. Botimizga xush kelibsiz☺"
                              f"\nFoydalanish uchun ro'yxatdan o'tishingiz kerak\n"
                              f"\n\nIltimos tilni tanlang !"
                              f"\nПожалуйста, выберите язык !",
                         reply_markup=select_lang
                         )
    await Lang.lang.set()
