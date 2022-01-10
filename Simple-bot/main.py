import telebot
from telebot import types
from h_token import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help","Хочу","Не хочу")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:' +  
        '\n/echo - возвращает введённую строку' + 
        '\n/what_is - статья из википедии по запросу'+
        '\n/google - ищет в google информацию по запросу')


@bot.message_handler(commands=['echo'])
def echo(message):
    bot.send_message(message.chat.id, message.text[5:])


@bot.message_handler(commands=['what_is'])
def what_is(message):
    bot.send_message(message.chat.id, 'https://ru.wikipedia.org/wiki/' + message.text[9:])


@bot.message_handler(commands=['google'])
def google(message):
    bot.send_message(message.chat.id, 'https://www.google.com/search?q=' + message.text[8:])


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == 'не хочу':
        bot.send_message(message.chat.id, 'Тебе всё равно сюда – https://mtuci.ru/')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')


bot.polling(none_stop=True, interval=0)