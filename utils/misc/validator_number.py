import re


def validate_uz_number(value):
    if re.match(pattern='^\+998\d{9}$', string=value):
        return True
    else:
        return False
