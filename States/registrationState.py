from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):
    name_team = State()  # Will be represented in storage as 'Welcome:name'
    contact_face = State()  # Will be represented in storage as 'Welcome:institute'
    link_vk = State()
    tel_number = State()
    institute = State()
