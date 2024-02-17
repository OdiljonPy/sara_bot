import re


def validate_uz_number(value):
    if re.match(pattern='^\+998\d{9}$', string=value):
        return True
    else:
        return False


def check_actual_number(phone_number):
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number
    return phone_number
