from states.register_state import RegisterUz
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.inline.web_view import web_button
from keyboards.default.select_lang import phone_number_uz


# from data.config import X_API_KEY, DOMAIN

# headers = {
#     'X-API-KEY': X_API_KEY
# }


@dp.message_handler(state=RegisterUz.fullname)
async def register_name(message: types.Message, state: FSMContext):
    await state.update_data({'fullname': message.text})
    await message.answer(text="Telefon raqamingizni 901234567 ko'rinishida kiriting"
                              "\nYoki «Raqamni yuborish» tugmasi orqali yuboring !",
                         reply_markup=phone_number_uz)
    await RegisterUz.phone_n.set()


@dp.message_handler(lambda message: len(message.text) == 12, state=RegisterUz.phone_n)
async def register_name(message: types.Message, state: FSMContext):
    phone_number = message.text
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    await state.update_data({'phone_number': phone_number})
    await message.answer(text="Malumotlaringizni qabul qildim !",
                         reply_markup=types.ReplyKeyboardRemove())

    await message.answer(text="Ko'proq malumotdan foydalanish uchun web view dan foydalanasiz !",
                         reply_markup=web_button())
    # save data
    data = await state.get_data()
    await message.answer(
        text=f"Name - {data.get('fullname')}"
             f"\nPhone n. - {data.get('phone_number')}"
             f"\nLan - {data.get('lan')}"
    )
    await state.finish()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegisterUz.phone_n)
async def register_name(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    await state.update_data({'phone_number': phone_number})
    await message.answer(text="Malumotlaringizni qabul qildim !",
                         reply_markup=types.ReplyKeyboardRemove())

    await message.answer(text="Ko'proq malumotdan foydalanish uchun web view dan foydalanasiz !",
                         reply_markup=web_button())
    # save data
    data = await state.get_data()

    await message.answer(
        text=f"Name - {data.get('fullname')}"
             f"\nPhone n. - {data.get('phone_number')}"
             f"\nLan - {data.get('lan')}"
    )
    await state.finish()


@dp.message_handler(state=RegisterUz.phone_n)
async def register_name(message: types.Message):
    await message.answer(text="Telefon raqamingizni 901234567 ko'rinishida kiriting !"
                              "\n Yoki «Raqamni yuborish» tugmasi orqali yuboring",
                         reply_markup=phone_number_uz)
    await RegisterUz.phone_n.set()
