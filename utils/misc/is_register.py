import requests
from data.config import DOMAIN


# from data.config import X_API_KEY, DOMAIN

# headers = {
#     'X-API-KEY': X_API_KEY
# }

def is_register(user_id: int):
    result = requests.post(
        url=f"{DOMAIN}/user_tg/check_user/",
        json={'user_id': user_id}
    )
    if result.status_code == 200 and result.json().get('ok'):
        return True
    return False
