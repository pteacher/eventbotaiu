from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button = KeyboardButton('/event')

event_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button)