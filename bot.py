from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN
from messages import MESSAGES, questions, institutes
from States.registrationState import Registration
from States.questState import Quest, set_defined_state
from db import Db


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Db()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await Registration.name_team.set()
    await message.reply(MESSAGES['start'], reply=False)
    await message.reply(MESSAGES['name_team'], reply=False)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'], reply=False)


@dp.message_handler(state=Registration.name_team)
async def process_name_team(message: types.Message, state: FSMContext):
    """
    Process name_team
    """
    async with state.proxy() as data:
        data['name'] = message.text

    db.create_team(message.from_user.id, message.text)
    await Registration.next()
    await message.reply(MESSAGES['contact_face'], reply=False)


@dp.message_handler(state=Registration.contact_face)
async def process_contact_face(message: types.Message, state: FSMContext):
    """
    Process user name
    """
    async with state.proxy() as data:
        data['name'] = message.text

    db.add_contact_face(message.from_user.id, message.text)
    await Registration.next()
    await message.reply(MESSAGES['link_vk'], reply=False)


@dp.message_handler(state=Registration.link_vk)
async def process_link_vk(message: types.Message, state: FSMContext):
    """
    Process link_vk
    """
    async with state.proxy() as data:
        data['link_vk'] = message.text

    db.add_link_vk(message.from_user.id, message.text)
    await Registration.next()
    await message.reply(MESSAGES['tel_number'], reply=False)


@dp.message_handler(state=Registration.tel_number)
async def process_tel_number(message: types.Message, state: FSMContext):
    """
    Process tel_number
    """
    async with state.proxy() as data:
        data['tel_number'] = message.text

    db.add_tel_number(message.from_user.id, message.text)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for institut in institutes.keys():
        institut_btn = KeyboardButton(institut)
        markup.add(institut_btn)
    await Registration.next()
    await message.reply(MESSAGES['institute'], reply_markup=markup, reply=False)


@dp.message_handler(state=Registration.institute)
async def process_institute(message: types.Message, state: FSMContext):
    """
    Process institute
    """
    async with state.proxy() as data:
        data['institute'] = message.text

    # добавляем институт в БД
    db.add_institute(message.from_user.id, message.text)
    await state.finish()
    await message.reply(MESSAGES['end_reg'], reply=False)


@dp.message_handler(commands=['start_Quest'])
async def start_quest(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    current_question = db.get_current_question(user_id=message.from_user.id)
    if current_question > len(questions):
        text = MESSAGES['you are finished']
        markup = ReplyKeyboardRemove()
        await message.reply(text, reply_markup=markup, reply=False)
    else:
        if current_question > 0:
            current_question -= 1
            await set_defined_state(current_question)
        else:
            db.increment_current_question(message.from_user.id, 0)
            current_question = 1
            await Quest.Task1.set()
        question = questions[current_question]
        await message.reply(question["Place"], reply_markup=markup, reply=False)
        text = question['Question']

        # markup
        if len(question['Choices']) > 1:
            for choice in question['Choices']:
                choice_btn = KeyboardButton(choice)
                markup.add(choice_btn)
        else:
            markup = ReplyKeyboardRemove()
        # send question
        if text != "":
            await message.reply(text, reply_markup=markup, reply=False)
        # add photo
        if question["Photo"]:
            try:
                img = "yura.png"
                await bot.send_photo(message.from_user.id, photo=open(img, 'rb'), caption=MESSAGES["duck"])
            except Exception as e:
                print(e)
        # add duck task
        if question["Duck"]:
            try:
                img = str(current_question) + ".png"
                await bot.send_photo(message.from_user.id, photo=open(img, 'rb'))
                await bot.send_photo(message.from_user.id, photo=open("duck.png", 'rb'), caption=MESSAGES["duck"])
            except Exception as e:
                print(e)
                await message.reply(MESSAGES["duck"] + MESSAGES["error_photo"], reply_markup=markup, reply=False)
        if current_question == 9:
            db.increment_current_question(message.from_user.id, current_question)
            text = question["Move"] + MESSAGES["go"]
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            go_btn = KeyboardButton("Поехали!")
            markup.add(go_btn)
            await Quest.next()
            await message.reply(text, reply_markup=markup, reply=False)


@dp.message_handler(state=Quest)
async def work_func(message: types.Message, state: FSMContext):
    user_answer = message.text.lower()
    user_id: int = message.from_user.id
    current_question: int = db.get_current_question(user_id)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    async with state.proxy() as data:
        data[current_question] = message.text

    if current_question > len(questions):
        text = MESSAGES['you are finished']
        markup = ReplyKeyboardRemove()
        await message.reply(text, reply_markup=markup, reply=False)

    if user_answer == "поехали!":  # задаем следующий вопрос
        question = questions[current_question]
        await message.reply(question["Place"], reply=False)
        text = question['Question']

        # markup
        if len(question['Choices']) > 1:
            for choice in question['Choices']:
                choice_btn = KeyboardButton(choice)
                markup.add(choice_btn)
        else:
            markup = ReplyKeyboardRemove()

        # add photo
        if question["Photo"]:
            try:
                img = "yura.png"
                await bot.send_photo(message.from_user.id, photo=open(img, 'rb'),
                                     caption=text, reply_markup=markup)
            except Exception as e:
                print(e)
                await message.reply(text, reply_markup=markup, reply=False)
        elif text != "":
            # send question
            await message.reply(text, reply_markup=markup, reply=False)
        # add duck task
        if question["Duck"]:
            try:
                img = str(current_question) + ".png"
                await bot.send_photo(message.from_user.id, photo=open(img, 'rb'))
                await bot.send_photo(message.from_user.id, photo=open("duck.png", 'rb'), caption=MESSAGES["duck"])
            except Exception as e:
                print(e)
                await message.reply(MESSAGES["duck"] + MESSAGES["error_photo"], reply_markup=markup, reply=False)
        if current_question == 9:
            db.increment_current_question(user_id, current_question)
            text = question["Move"] + MESSAGES["go"]
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            go_btn = KeyboardButton("Поехали!")
            markup.add(go_btn)
            await Quest.next()
            await message.reply(text, reply_markup=markup, reply=False)
    else:
        # if user_answer[0] != ".":  # проверяем текущий вопрос
        question = questions[current_question]
        true_answer = question['Answer'].lower()

        if user_answer == true_answer:
            db.set_point(user_id, current_question)

        if current_question == len(questions):
            db.increment_current_question(user_id, current_question)
            text = MESSAGES['the_end']
            markup = ReplyKeyboardRemove()
            await state.finish()
        else:
            db.increment_current_question(user_id, current_question)
            text = question["Move"] + MESSAGES["go"]
            go_btn = KeyboardButton("Поехали!")
            markup.add(go_btn)
            await Quest.next()
        await message.reply(text, reply_markup=markup, reply=False)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text in MESSAGES.keys():
        text = MESSAGES[message.text]
    else:
        text = MESSAGES['unknown']
    await message.reply(text, reply=False)


executor.start_polling(dp, skip_updates=True)
