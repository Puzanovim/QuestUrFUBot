from aiogram.dispatcher.filters.state import State, StatesGroup


async def set_defined_state(number: int):
    if number == 1:
        await Quest.Task1.set()
    elif number == 2:
        await Quest.Task2.set()
    elif number == 3:
        await Quest.Task3.set()
    elif number == 4:
        await Quest.Task4.set()
    elif number == 5:
        await Quest.Task5.set()
    elif number == 6:
        await Quest.Task6.set()
    elif number == 7:
        await Quest.Task2.set()
    elif number == 8:
        await Quest.Task8.set()
    elif number == 9:
        await Quest.Task9.set()
    elif number == 10:
        await Quest.Task10.set()
    elif number == 11:
        await Quest.Task11.set()
    elif number == 12:
        await Quest.Task12.set()
    elif number == 13:
        await Quest.Task13.set()
    elif number == 14:
        await Quest.Task14.set()
    elif number == 15:
        await Quest.Task15.set()


class Quest(StatesGroup):
    Task1 = State()
    Task2 = State()
    Task3 = State()
    Task4 = State()
    Task5 = State()
    Task6 = State()
    Task7 = State()
    Task8 = State()
    Task9 = State()
    Task10 = State()
    Task11 = State()
    Task12 = State()
    Task13 = State()
    Task14 = State()
    Task15 = State()
