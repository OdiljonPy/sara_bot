import requests
from loader import dp
from aiogram import types
from data.config import DOMAIN
from aiogram.dispatcher import FSMContext
from states.register_state import RegisterRu, Lang
from keyboards.inline.web_view import web_button_user
from keyboards.default.select_lang import select_lang
from keyboards.default.select_lang import phone_number_ru
from utils.misc.send_error_notify import send_error_notify_
from utils.misc.validator_number import validate_uz_number, check_actual_number


# from data.config import X_API_KEY, DOMAIN

# headers = {
#     'X-API-KEY': X_API_KEY
# }


@dp.message_handler(state=RegisterRu.fullname)
async def register_phone_ru(message: types.Message, state: FSMContext):
    await state.update_data({'fullname': message.text})
    await message.answer(text="Введите свой номер телефона: +998906556655. !"
                              "\nИли отправить через кнопку «Отправить номер»",
                         reply_markup=phone_number_ru)
    await RegisterRu.phone_n.set()


@dp.message_handler(lambda message: validate_uz_number(message.text), state=RegisterRu.phone_n)
async def register_phone_number_ru(message: types.Message, state: FSMContext):
    data = await state.get_data()
    phone_number = check_actual_number(message.text)

    # save data
    data_obj = {
        'user_id': message.from_user.id,
        'last_name': data.get('fullname'),
        'first_name': f"{message.from_user.first_name} - {message.from_user.last_name}",
        'username': message.from_user.username,
        'phone_number': phone_number,
        'language': data.get('lan')
    }

    result = requests.post(url=f"{DOMAIN}/user_tg/", json=data_obj)
    if result.status_code == 201 and result.json().get('ok'):
        await message.answer(text="Я получил вашу информацию !",
                             reply_markup=types.ReplyKeyboardRemove())

        await message.answer(text="Вы можете использовать веб-просмотр для получения дополнительной информации !",
                             reply_markup=web_button_user(user_id=message.from_user.id))
        await state.finish()

    elif result.json().get('error') is not None and result.json().get('error').get('phone_number') is not None:
        await message.answer(
            text="Этот номер телефона уже зарегистрирован\n"
                 "Пожалуйста, введите другой номер телефона."
        )

    else:
        await message.answer(text=f"Во время регистрации произошла ошибка."
                                  f"\n\nIltimos tilni tanlang !"
                                  f"\nПожалуйста, выберите язык !",
                             reply_markup=select_lang
                             )

        await send_error_notify_(
            message="Sara bot:\n\n"
                    "Request Post so'rovda xatolik yuz berdi.\n"
                    "registration_ru.py  52-qator\n"
                    f"request.status_code: {result.status_code}"
        )
        await Lang.lang.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegisterRu.phone_n)
async def register_phone_contact_ru(message: types.Message, state: FSMContext):
    data = await state.get_data()
    phone_number = check_actual_number(message.contact.phone_number)

    data_obj = {
        'user_id': message.from_user.id,
        'last_name': data.get('fullname'),
        'first_name': f"{message.from_user.first_name} - {message.from_user.last_name}",
        'username': message.from_user.username,
        'phone_number': phone_number,
        'language': data.get('lan')
    }

    result = requests.post(url=f"{DOMAIN}/user_tg/", json=data_obj)
    if result.status_code == 201 and result.json().get('ok'):
        await message.answer(text="Я получил вашу информацию !",
                             reply_markup=types.ReplyKeyboardRemove())

        await message.answer(text="Вы можете использовать веб-просмотр для получения дополнительной информации !",
                             reply_markup=web_button_user(user_id=message.from_user.id))
        await state.finish()

    elif result.json().get('error') is not None and result.json().get('error').get('phone_number') is not None:
        await message.answer(
            text="Этот номер телефона уже зарегистрирован\n"
                 "Пожалуйста, введите другой номер телефона."
        )

    else:
        await message.answer(text=f"Во время регистрации произошла ошибка."
                                  f"\n\nIltimos tilni tanlang !"
                                  f"\nПожалуйста, выберите язык !",
                             reply_markup=select_lang
                             )
        await send_error_notify_(
            message="Sara bot:\n\n"
                    "Request Post so'rovda xatolik yuz berdi.\n"
                    "registration_ru.py  108-qator\n"
                    f"request.status_code: {result.status_code}"
        )

        await Lang.lang.set()


@dp.message_handler(state=RegisterRu.phone_n)
async def error_register_phone_ru(message: types.Message):
    await message.answer(text="Введите свой номер телефона: +998906556655. !"
                              "\nИли отправить через кнопку «Отправить номер»",
                         reply_markup=phone_number_ru)
    await RegisterRu.phone_n.set()
