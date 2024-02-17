import requests
from data.config import DOMAIN
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def select_comp_name():
    company_list = requests.get(url=f"{DOMAIN}/companies").json()
    if not company_list:
        company_list = []

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
