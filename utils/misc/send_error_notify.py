import requests
from data.config import ERROR_NOTIFY_BOT_TOKEN, ERROR_NOTIFY_CHANNEL_ID


async def send_error_notify_(message: str) -> None:
    requests.post(
            url=f'https://api.telegram.org/bot{ERROR_NOTIFY_BOT_TOKEN}/sendMessage',
            data={'chat_id': ERROR_NOTIFY_CHANNEL_ID, 'text': message}
        )
