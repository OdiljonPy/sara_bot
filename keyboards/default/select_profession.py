from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

profession_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Men doktorman!')
        ],
        [
            KeyboardButton(text='Men doktor emasman!')
        ]
    ],
    resize_keyboard=True
)

profession_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Я врач!')
        ],
        [
            KeyboardButton(text='Я не врач!')
        ]
    ],
    resize_keyboard=True
)
