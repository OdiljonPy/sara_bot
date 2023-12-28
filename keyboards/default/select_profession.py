from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

select_profession_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Men Doktorman !')
        ],
        [
            KeyboardButton(text='Men Doktor emasman !')
        ]
    ],
    resize_keyboard=True
)

select_profession_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Я врач !')
        ],
        [
            KeyboardButton(text='Я не врач !')
        ]
    ],
    resize_keyboard=True
)
