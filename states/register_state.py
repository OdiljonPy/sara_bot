from aiogram.dispatcher.filters.state import State, StatesGroup


class Lang(StatesGroup):
    lang = State()
    select_profession = State()
    select_company = State()


class RegisterRu(StatesGroup):
    fullname = State()
    phone_n = State()


class RegisterUz(StatesGroup):
    fullname = State()
    phone_n = State()
