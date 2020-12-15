from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

# from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep

from config import TOKEN
from messages import MESSAGES, questions, institutes
from States.registrationState import Registration
from States.questState import Quest
from db import Db

from glob import glob
from random import choice


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Db()


# @dp.message_handler(commands=['get_gifts_all'])
# async def send_cert(message: types.Message):
#     users = db.get_users()
#     for user in users:
#         try:
#             name = user['name']
#             user_id = user['user_id']
#
#             image = Image.open("./certs/cert.png")
#             draw = ImageDraw.Draw(image)
#
#             W = 2480
#             style = ImageFont.truetype('11528.ttf', size=120)
#
#             w, h = style.getsize(name)
#             draw.text(((W-w)/2, 1550), name, font=style, fill="#fff")
#
#             name_cert = name + ".png"
#             image.save(name_cert, "PNG")
#
#             text = MESSAGES['gift']
#             img = name_cert
#             await bot.send_photo(user_id, photo=open(img, 'rb'), caption=text)
#             print(f"Gift to {name} with id={user_id} sent!")
#             await sleep(1)
#         except Exception as e:
#             print(e)


# @dp.message_handler(commands=['get_name_alert_all'])
# async def send_cert(message: types.Message):
#     users = db.get_users()
#     for user in users:
#         try:
#             name = user['name']
#             user_id = user['user_id']
#             text = MESSAGES['alert_change_name'] + name
#             await bot.send_message(user_id, text)
#             print(f"Alert to {name} with id={user_id} sent!")
#             await sleep(1)
#         except Exception as e:
#             print(e)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await Registration.name_team.set()
    await message.reply(MESSAGES['start'], reply=False)
    await message.reply(MESSAGES['name_team'], reply=False)


@dp.message_handler(commands=['help'])  # TODO rewrite answer text
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'], reply=False)


@dp.message_handler(commands=['result'])  # TODO rewrite
async def result(message: types.Message):
    my_result = db.get_result(message.from_user.id)
    text = MESSAGES['result'] + str(my_result)
    images = glob("img/*")
    img = choice(images)
    await bot.send_photo(message.from_user.id, photo=open(img, 'rb'), caption=text)


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


@dp.message_handler(commands=['start_Quiz'])
async def start_quiz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if db.get_current_question(user_id=message.from_user.id) > 14:
        text = MESSAGES['you are finished']
        markup = ReplyKeyboardRemove()
        await message.reply(text["Place"], reply_markup=markup, reply=False)
    else:
        await Quest.Task1.set()
        db.increment_current_question(message.from_user.id, 0)
        current_question = 1
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
                await bot.send_photo(message.from_user.id, photo=open(img, 'rb'), caption=MESSAGES["duck"])
            except Exception as e:
                print(e)
                await message.reply(MESSAGES["duck"] + MESSAGES["error_photo"], reply_markup=markup, reply=False)


# @dp.message_handler(state=Quest)
# async def questions_step_by_step(message: types.Message, state: FSMContext):
#     """
#     Функция квиза
#     :param state:
#     :param message: сообщение пользователя
#     :return: отправляем следующий вопрос
#     """
#     user_id: int = message.from_user.id
#     current_question: int = db.get_current_question(user_id)
#
#     async with state.proxy() as data:
#         data[current_question] = message.text
#
#     right_answer = False
#     if current_question > 30:
#         text = MESSAGES['you are finished']
#         markup = ReplyKeyboardRemove()
#     else:
#         question = questions[current_question]
#         markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#         user_answer = message.text.lower()
#         true_answer = questions[current_question]['Answer'].lower()
#
#         if user_answer == true_answer:
#             right_answer = True
#             db.set_point(user_id, current_question)
#
#         have_hint = db.have_hints(user_id)
#         if current_question + 1 > 20:
#             markup = ReplyKeyboardRemove()
#             #  here open questions
#             if not right_answer and not have_hint:
#                 # даем подсказку
#                 text = MESSAGES['hint'] + question['Choices'][0]
#                 db.set_hint(user_id)
#             else:
#                 # он дал верный ответ или уже была одна подсказка
#                 db.delete_hint(user_id)
#                 db.increment_current_question(user_id, current_question)
#                 if current_question == 30:
#                     text = MESSAGES['the_end']
#                     await state.finish()
#                 else:
#                     question = questions[current_question + 1]
#                     text = question['Question']
#                     await Quest.next()
#         else:
#             #  here quiz questions
#             db.increment_current_question(user_id, current_question)
#             question = questions[current_question + 1]
#             text = question['Question']
#             for choice in question['Choices']:
#                 choice_btn = KeyboardButton(choice)
#                 markup.add(choice_btn)
#             await Quest.next()
#     await message.reply(text, reply_markup=markup, reply=False)


@dp.message_handler(state=Quest)
async def work_func(message: types.Message, state: FSMContext):
    user_answer = message.text.lower()
    user_id: int = message.from_user.id
    current_question: int = db.get_current_question(user_id)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    async with state.proxy() as data:
        data[current_question] = message.text

    if current_question > 14:
        text = MESSAGES['you are finished']
        markup = ReplyKeyboardRemove()
        await message.reply(text, reply_markup=markup, reply=False)

    if user_answer == "поехали!":  # задаем следующий вопрос
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
                await bot.send_photo(message.from_user.id, photo=open(img, 'rb'), caption=MESSAGES["duck"])
            except Exception as e:
                print(e)
                await message.reply(MESSAGES["duck"] + MESSAGES["error_photo"], reply_markup=markup, reply=False)
    else:
        # if user_answer[0] != ".":  # проверяем текущий вопрос
        question = questions[current_question]
        true_answer = question['Answer'].lower()

        if user_answer == true_answer:
            db.set_point(user_id, current_question)

        if current_question == 14:
            db.increment_current_question(user_id, current_question)
            text = MESSAGES['the_end']
            await state.finish()
        else:
            db.increment_current_question(user_id, current_question)
            text = question["move"] + MESSAGES["go"]
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
