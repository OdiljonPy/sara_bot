from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

phone_number_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='«Raqamni yuborish»', request_contact=True)
        ]
    ],
    resize_keyboard=True
)

phone_number_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='«Отправить номер»', request_contact=True)
        ]
    ],
    resize_keyboard=True
)

select_lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbekcha")
        ],
        [
            KeyboardButton(text="🇷🇺 Русский")
        ]
    ],
    resize_keyboard=True
)
