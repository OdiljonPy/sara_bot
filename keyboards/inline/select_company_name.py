from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from data.config import DOMAIN


def select_comp_name(user_id: int = None):
    company = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Company name", callback_data="company_id")
            ]
        ],
    )

    return company
