# from msilib.schema import Class
# from pyexpat.errors import messages
import re
# from email import message
from aiogram import Bot, types
from config import BOT_TOKEN
import keyboard as kb


import config
from aiogram import types
from bot import BotDB
from dispatcher import dp

from utils import *

bot = Bot(token=BOT_TOKEN)


@dp.message_handler(commands = "start")
async def start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    # await message.reply("Первая инлайн кнопка", reply_markup=kb.inline_kb1)
    await message.bot.send_message(message.from_user.id, "<b>Welcome!</b> To record an event, use <i>'/event'</i> command", reply_markup=kb.event_kb)
    await state.set_state(States.all()[0])

@dp.message_handler(commands = "start",state=States.STATE_0)
async def start(message: types.Message):

    await message.bot.send_message(message.from_user.id, "The bot is already started. To record an event, use <i>'/event'</i> command")

@dp.message_handler(commands = "help",state=States.STATE_0)
async def start(message: types.Message):
    
    await message.bot.send_message(message.from_user.id, "To record an event, use <i>'/event'</i> command")

@dp.message_handler(commands = ("event"), commands_prefix = "/!",state=States.STATE_0)
async def record_start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    await bot.send_message(message.from_user.id,'Enter the <u><b>name</b></u> of the event:', 'HTML')
    await state.set_state(States.all()[1])

@dp.message_handler(state=States.STATE_1)
async def name(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    global name_
    name_ = message.text
    print (name)

    await message.reply('Enter the <u><b>date</b></u> of the event:', reply=False)
    await state.set_state(States.all()[2])

@dp.message_handler(state=States.STATE_2[0])
async def date(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    global date_
    date_ = message.text
    print (date)

    await message.reply('Enter the <u><b>time</b></u> of the event:', reply=False)
    await state.set_state(States.all()[3])

@dp.message_handler(state=States.STATE_3[0])
async def time(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    global time_
    time_ = message.text
    print (time)

    await message.reply('Enter the <u><b>place</b></u> of the event:', reply=False)
    await state.set_state(States.all()[4])

@dp.message_handler(state=States.STATE_4[0])
async def place(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    place_ = message.text
    print (place_)
    await state.set_state(States.all()[0])

    await message.reply('Record of the <u><b>event</b></u> is added successfully!', reply=False)

    BotDB.add_record(name_, date_, time_, place_)
            
    