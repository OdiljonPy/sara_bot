from states.register_state import RegisterRu
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.inline.web_view import web_button
from keyboards.default.select_lang import phone_number_ru


# from data.config import X_API_KEY, DOMAIN

# headers = {
#     'X-API-KEY': X_API_KEY
# }


@dp.message_handler(state=RegisterRu.fullname)
async def register_name(message: types.Message, state: FSMContext):
    await state.update_data({'fullname': message.text})
    await message.answer(text="Введите свой номер телефона: 901234567. !"
                              "\nИли отправить через кнопку «Отправить номер»",
                         reply_markup=phone_number_ru)
    await RegisterRu.phone_n.set()


@dp.message_handler(lambda message: len(message.text) == 12, state=RegisterRu.phone_n)
async def register_name(message: types.Message, state: FSMContext):
    phone_number = message.text
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    await state.update_data({'phone_number': phone_number})
    await message.answer(text="Я получил вашу информацию !",
                         reply_markup=types.ReplyKeyboardRemove())

    await message.answer(text="Вы можете использовать веб-просмотр для получения дополнительной информации !",
                         reply_markup=web_button())
    # save data
    data = await state.get_data()
    await message.answer(
        text=f"Name - {data.get('fullname')}"
             f"\nPhone n. - {data.get('phone_number')}"
             f"\nLan - {data.get('lan')}"
    )
    await state.finish()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegisterRu.phone_n)
async def register_name(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    await state.update_data({'phone_number': phone_number})
    await message.answer(text="Я получил вашу информацию !",
                         reply_markup=types.ReplyKeyboardRemove())

    await message.answer(text="Вы можете использовать веб-просмотр для получения дополнительной информации !",
                         reply_markup=web_button())
    # save data
    data = await state.get_data()
    await message.answer(
        text=f"Name - {data.get('fullname')}"
             f"\nPhone n. - {data.get('phone_number')}"
             f"\nLan - {data.get('lan')}"
    )
    await state.finish()


@dp.message_handler(state=RegisterRu.phone_n)
async def register_name(message: types.Message):
    await message.answer(text="Введите свой номер телефона: 901234567. !"
                              "\nИли отправить через кнопку «Отправить номер»",
                         reply_markup=phone_number_ru)
    await RegisterRu.phone_n.set()
