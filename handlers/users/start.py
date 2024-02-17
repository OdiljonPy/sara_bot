from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from utils.misc.is_register import is_register
from keyboards.default.select_lang import select_lang
from aiogram.dispatcher.filters.builtin import CommandStart
from states.register_state import Lang, RegisterRu, RegisterUz
from keyboards.inline.select_company_name import select_comp_name
from aiogram.utils.exceptions import MessageCantBeEdited, MessageToEditNotFound
from keyboards.default.select_profession import profession_ru_button, profession_uz_button


# @dp.message_handler(CommandStart())
# async def start(message: types.Message):
#     photo = await message.bot.get_user_profile_photos(user_id=message.from_user.id)
#     print(photo)
#     file = await message.bot.get_file(photo.photos[0][0].file_id)
#     print(f"{file=}")
    # await message.answer_document(document=types.InputFile(file.get_file())


@dp.message_handler(CommandStart(), lambda message: not is_register(user_id=message.from_user.id))
async def bot_start(message: types.Message):
    await message.answer(
        text=f"Assalomu alaykum. Botimizga xush kelibsiz\n"
             f"Foydalanish uchun ro'yxatdan o'tishingiz kerak.\n\n"
             f"Привет. Добро пожаловать в наш бот"
             f"Вы должны зарегистрироваться, чтобы использовать.",
    )
    await message.answer(
        text=f"Iltimos tilni tanlang\n"
             f"Пожалуйста, выберите язык",
        reply_markup=select_lang
    )
    await Lang.lang.set()


@dp.message_handler(lambda message: message.text == "🇺🇿 O'zbekcha", state=Lang.lang)
async def select_lang_uz(message: types.Message, state: FSMContext):
    await message.answer(text=f"Ism familiyangizni kiriting.",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.update_data({'lan': 'uz'})
    await RegisterUz.fullname.set()
    # await message.answer(text="Siz doktormisiz ?", reply_markup=profession_uz_button)
    # await state.update_data({'lan': 'uz'})
    # await Lang.select_profession.set()


@dp.message_handler(lambda message: message.text == '🇷🇺 Русский', state=Lang.lang)
async def select_lang_ru(message: types.Message, state: FSMContext):
    await message.answer(text=f"\nВведите свое имя и фамилию.",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.update_data({'lan': 'uz'})
    await RegisterRu.fullname.set()


@dp.message_handler(state=Lang.lang)
async def error_select_lang(message: types.Message):
    await message.answer(text=f"Iltimos savollarga etiborli bo'ling !"
                              f"\nFoydalanish uchun ro'yxatdan o'tishingiz kerak 📝"
                              f"\n\nIltimos tilni tanlang!"
                              f"\nПожалуйста, выберите язык!",
                         reply_markup=select_lang
                         )
    await Lang.lang.set()

# @dp.message_handler(lambda message: message.text == "Men doktorman!", state=Lang.select_profession)
# async def select_profession(message: types.Message):
#     await message.answer("Kompaniya nomini tanlang !", reply_markup=await select_comp_name())
#     await Lang.select_company.set()


# @dp.callback_query_handler(state=Lang.select_company)
# async def select_company(call: types.CallbackQuery, state: FSMContext):
#     await state.update_data({'doctor': 'true', 'company_id': call.data})
#     data = await state.get_data()
#     if data.get('lan') == 'uz':
#         await call.message.delete()
#         await call.message.answer(text=f"Ism familiyangizni  kiriting.",
#                                   reply_markup=types.ReplyKeyboardRemove())
#         await RegisterUz.fullname.set()
#     else:
#         await call.message.delete()
#         await call.message.answer(text=f"\nВведите свое имя и фамилию.",
#                                   reply_markup=types.ReplyKeyboardRemove())
#         await RegisterRu.fullname.set()


# @dp.message_handler(lambda message: message.text == "Men doktor emasman!", state=Lang.select_profession)
# async def select_profession2(message: types.Message, state: FSMContext):
#     await message.answer(text=f"Ism familiyangizni  kiriting.",
#                          reply_markup=types.ReplyKeyboardRemove())
#     await RegisterUz.fullname.set()


# @dp.message_handler(lambda message: message.text == '🇷🇺 Русский', state=Lang.lang)
# async def select_lang_ru(message: types.Message):
#     await message.answer(text=f"\nВведите свое имя и фамилию.",
#                          reply_markup=types.ReplyKeyboardRemove())
#     await RegisterRu.fullname.set()


# @dp.message_handler(lambda message: message.text == 'Я врач!', state=Lang.select_profession)
# async def select_profession_ru(message: types.Message):
#     await message.answer("Выбирайте компанию!", reply_markup=await select_comp_name())
#     await Lang.select_company.set()
#
#
# @dp.message_handler(lambda message: message.text == 'Я не врач!', state=Lang.select_profession)
# async def select_profession_ru2(message: types.Message, state: FSMContext):
#     await message.answer(text=f"\nВведите свое имя и фамилию.",
#                          reply_markup=types.ReplyKeyboardRemove())
#     await RegisterRu.fullname.set()


# @dp.message_handler(state=Lang.select_company)
# async def error_select_company(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     if data.get('lan') == 'uz':
#         try:
#             await bot.edit_message_text(
#                 text="Iltimos kompaniya nomini tanlang !",
#                 chat_id=message.chat.id,
#                 message_id=int(message.message_id) - 1,
#                 reply_markup=await select_comp_name()
#             )
#             await bot.delete_message(message.chat.id, message_id=message.message_id)
#         except MessageCantBeEdited:
#             pass
#         except MessageToEditNotFound:
#             await bot.delete_message(message.chat.id, message_id=message.message_id)
#
#         await Lang.select_company.set()
#
#     else:
#         try:
#             await bot.edit_message_text(
#                 text="Пожалуйста, выберите название компании!",
#                 chat_id=message.chat.id,
#                 message_id=int(message.message_id) - 1,
#                 reply_markup=await select_comp_name()
#             )
#             await bot.delete_message(message.chat.id, message_id=message.message_id)
#         except MessageCantBeEdited:
#             pass
#         except MessageToEditNotFound:
#             await bot.delete_message(message.chat.id, message_id=message)
#
#         await Lang.select_company.set()


# @dp.message_handler(state=Lang.select_profession)
# async def error_select_profession(message: types.Message):
#     await message.delete()
