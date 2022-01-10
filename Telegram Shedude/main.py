from telebot import types
import telebot

import data, database, week_count
from h_token import token

bot = telebot.TeleBot(token)

db = database.DB()

@bot.message_handler(commands = ['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton("Понедельник",callback_data="Понедельник")
    bt_2 = types.InlineKeyboardButton("Вторник",callback_data="Вторник")
    bt_3 = types.InlineKeyboardButton("Среда",callback_data="Среда")
    bt_4 = types.InlineKeyboardButton("Четверг",callback_data="Четверг")
    bt_5 = types.InlineKeyboardButton("Пятница",callback_data="Пятница")
    bt_6 = types.InlineKeyboardButton("Суббота",callback_data="Суббота")
    bt_7 = types.InlineKeyboardButton("Расписание на текущую неделю",callback_data="Расписание на текущую неделю")
    bt_8 = types.InlineKeyboardButton("Расписание на следующую неделю",callback_data="Расписание на следующую неделю")
    keyboard.row(bt_1)
    keyboard.row(bt_2)
    keyboard.row(bt_3)
    keyboard.row(bt_4)
    keyboard.row(bt_5)
    keyboard.row(bt_6)
    keyboard.row(bt_7)
    keyboard.row(bt_8)
    bot.send_message(message.chat.id, 'started',reply_markup=keyboard)


@bot.message_handler(commands = ['week']) 
def week(message):
    week = week_count.get_week()
    if week == 0:
        output = 'Нижняя'
    else:
        output = 'Верхняя'
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands = ['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'Сайт МТУСИ - https://mtuci.ru/')


@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id, data.inf)


@bot.message_handler(content_types = ['text'])
def answer(message):
    if message.text.lower() == 'понедельник':
        day = 'mon'
    elif message.text.lower() == 'вторник':
        day = 'tue'
    elif message.text.lower() == 'среда':
        day = 'wed'
    elif message.text.lower() == 'четверг':
        day = 'thu'
    elif message.text.lower() == 'пятница':
        day = 'fri'
    elif message.text.lower() == 'суббота':
        day = 'sat'
    elif message.text.lower() == 'расписание на текущую неделю':
        day = 'current_week'
    elif message.text.lower() == 'расписание на следующую неделю':
        day = 'next_week'
    else:
        day = 'null'
    if day != 'null':
        reply = db.get_timetable(day=day)
    else:
        reply = 'Извините, я вас не понимаю.'
    bot.send_message(message.chat.id,reply)

bot.polling()