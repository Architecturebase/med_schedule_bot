from aiogram.dispatcher.filters.state import State, StatesGroup
class UserData(StatesGroup):
    name_surname = State()
    user_id = State()
    user_name_surname_from_rg = State()
    tel_number = State()
    email = State()
    came_at_time = State()
    wanted_time = State()
    service = State()
    # came_from - откуда пользователь узнал про компанию
    came_from = State()

