import telebot,os
from dotenv import load_dotenv
from random import randint
load_dotenv()

BOT_API = os.getenv('bot_api')
bot = telebot.TeleBot(BOT_API)
number = randint(1,10)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здоров, попробуй вгадати число від 1 до 10')

@bot.message_handler(func=lambda message: message.text.isdigit())
def guess_number(message):
    global number
    if int(message.text) == number:
        bot.send_message(message.chat.id, 'Ти виграв!')
        number = randint(1,10)
    else:
        bot.send_message(message.chat.id, 'Ти програв')


bot.polling(none_stop=True)