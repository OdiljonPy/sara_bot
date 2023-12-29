from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from data.config import DOMAIN


def web_button_user(user_id: int):
    web_view = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Web - view",
                    web_app=WebAppInfo(url=f"https://sara-client.netlify.app/{user_id}")),
                # web_app=WebAppInfo(url=f"https://168.119.110.233:5003/api/v1/messages/8/"), )
            ]
        ],
    )

    return web_view


def web_button_admin(user_id: int):
    web_view = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Web - view",
                    web_app=WebAppInfo(url=f"https://inspiring-stroopwafel-ada3d4.netlify.app/{user_id}")),
                # web_app=WebAppInfo(url=f"https://168.119.110.233:5003/api/v1/messages/8/"), )
            ]
        ],
    )

    return web_view
