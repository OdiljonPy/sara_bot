from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.select_profession import select_profession_ru, select_profession_uz
from keyboards.inline.select_company_name import select_comp_name
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


@dp.message_handler(lambda message: message.text == "🇺🇿 O'zbekcha", state=Lang.lang)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text="Siz Doktormisiz ?", reply_markup=select_profession_uz)
    await state.update_data({'lan': 'uz'})
    await Lang.select_profession.set()


@dp.message_handler(lambda message: message.text == "Men Doktorman !", state=Lang.select_profession)
async def bot_start(message: types.Message):
    await message.answer("Kompaniya tanlang !", reply_markup=select_comp_name())
    await Lang.select_company.set()


@dp.callback_query_handler(state=Lang.select_company)
async def bot_start(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data.get('lan') == 'uz':
        await call.message.answer(text=f"Ismingizni kiriting !",
                                  reply_markup=types.ReplyKeyboardRemove())
        await RegisterUz.fullname.set()
    else:
        await call.message.answer(text=f"\nВведите ваше имя !",
                                  reply_markup=types.ReplyKeyboardRemove())
        await RegisterRu.fullname.set()
    await state.update_data({'doctor': 'true', 'company_id': call.data})


@dp.message_handler(lambda message: message.text == "Men Doktor emasman !", state=Lang.select_profession)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"Ismingizni kiriting !",
                         reply_markup=types.ReplyKeyboardRemove())
    await RegisterUz.fullname.set()


@dp.message_handler(lambda message: message.text == '🇷🇺 Русский', state=Lang.lang)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text="Вы доктор ?", reply_markup=select_profession_ru)
    await state.update_data({'lan': 'ru'})
    await Lang.select_profession.set()


@dp.message_handler(lambda message: message.text == 'Я врач !', state=Lang.select_profession)
async def bot_start(message: types.Message):
    await message.answer("Выбирайте компанию!", reply_markup=select_comp_name())
    await Lang.select_company.set()


@dp.message_handler(lambda message: message.text == 'Я не врач !', state=Lang.select_profession)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text=f"\nВведите ваше имя !",
                         reply_markup=types.ReplyKeyboardRemove())
    await RegisterRu.fullname.set()


@dp.message_handler(state=Lang.lang)
async def bot_start(message: types.Message):
    await message.answer(text=f"Assalomu alaykum! Botimizga xush kelibsiz 🙂"
                              f"\nFoydalanish uchun ro'yxatdan o'tishingiz kerak\n"
                              f"\n\nIltimos tilni tanlang!"
                              f"\nПожалуйста, выберите язык!",
                         reply_markup=select_lang
                         )
    await Lang.lang.set()
