import requests
from states.register_state import RegisterUz
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.inline.web_view import web_button
from keyboards.default.select_lang import phone_number_uz
from data.config import DOMAIN
from utils.misc.validator_number import validate_uz_number


# from data.config import X_API_KEY, DOMAIN

# headers = {
#     'X-API-KEY': X_API_KEY
# }


@dp.message_handler(state=RegisterUz.fullname)
async def register_name(message: types.Message, state: FSMContext):
    await state.update_data({'fullname': message.text})
    await message.answer(text="Telefon raqamingizni +998906556655 ko'rinishida kiriting"
                              "\nYoki «Raqamni yuborish» tugmasi orqali yuboring !",
                         reply_markup=phone_number_uz)
    await RegisterUz.phone_n.set()


@dp.message_handler(lambda message: validate_uz_number(message.text), state=RegisterUz.phone_n)
async def register_phone_number_uz(message: types.Message, state: FSMContext):
    phone_number = message.text
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    await state.update_data({'phone_number': phone_number})
    await message.answer(text="Malumotlaringizni qabul qildim !",
                         reply_markup=types.ReplyKeyboardRemove())

    await message.answer(text="Ko'proq malumotdan foydalanish uchun web view dan foydalanasiz !",
                         reply_markup=web_button(user_id=message.from_user.id))
    # save data
    data = await state.get_data()
    await state.finish()

    data_obj = {
        'user_id': message.from_user.id,
        'last_name': data.get('fullname'),
        'first_name': message.from_user.first_name,
        'username': message.from_user.username,
        'phone_number': data.get('phone_number'),
        'language': data.get('lan')
    }

    if data.get('doctor') == 'true':
        data_obj['category'] = [1]
        data_obj['main_category'] = 1
        data_obj['company'] = data.get('company_id')

    requests.post(url=f"{DOMAIN}/user_tg/", data=data_obj)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegisterUz.phone_n)
async def register_phone_contact_uz(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    await state.update_data({'phone_number': phone_number})
    await message.answer(text="Malumotlaringizni qabul qildim !",
                         reply_markup=types.ReplyKeyboardRemove())

    await message.answer(text="Ko'proq malumotdan foydalanish uchun web view dan foydalanasiz !",
                         reply_markup=web_button(user_id=message.from_user.id))
    # save data
    data = await state.get_data()
    await state.finish()

    data_obj = {
        'user_id': message.from_user.id,
        'last_name': data.get('fullname'),
        'first_name': message.from_user.first_name,
        'username': message.from_user.username,
        'phone_number': data.get('phone_number'),
        'language': data.get('lan')
    }

    print("Status - ", data.get('doctor') == 'true')

    if data.get('doctor') == 'true':
        data_obj['category'] = [1]
        data_obj['main_category'] = 1
        data_obj['company'] = data.get('company_id')

    print("Data - ", data_obj)

    requests.post(url=f"{DOMAIN}/user_tg/", data=data_obj)


@dp.message_handler(state=RegisterUz.phone_n)
async def error_register_phone_uz(message: types.Message):
    await message.answer(text="Telefon raqamingizni +998906556655 ko'rinishida kiriting !"
                              "\n Yoki «Raqamni yuborish» tugmasi orqali yuboring",
                         reply_markup=phone_number_uz)
    await RegisterUz.phone_n.set()
