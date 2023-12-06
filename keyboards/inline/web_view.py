from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from data.config import DOMAIN


def web_button(user_id: int = None):
    web_view = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Web - view",
                    web_app=WebAppInfo(url=f"https://www.google.com/")),
                # web_app=WebAppInfo(url=f"https://168.119.110.233:5003/api/v1/messages/8/"), )
            ]
        ],
    )

    return web_view
