import requests
from data.config import DOMAIN
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def select_comp_name(user_id: int = None):
    company_list = requests.get(url=f"{DOMAIN}/companies").json()

    company = InlineKeyboardMarkup(
        inline_keyboard=[]
    )

    buttons = [
        [
            InlineKeyboardButton(text=f"{company.get('name')}", callback_data=f"{company.get('id')}")
        ] for company in company_list
    ]

    for button in buttons:
        company.inline_keyboard.append(button)

    return company
