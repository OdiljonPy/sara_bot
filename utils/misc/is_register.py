import requests
from data.config import DOMAIN


# from data.config import X_API_KEY

# headers = {
#     'X-API-KEY': X_API_KEY
# }

def is_register(user_id: int = None):
    return True
    # return requests.post(url=f"{DOMAIN}/user_tg/check_user/", params={"user_id": user_id}).json().get("ok")
