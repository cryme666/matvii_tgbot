import telebot,os
from dotenv import load_dotenv

load_dotenv()

BOT_API = os.getenv('BOT_API')

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! I am a bot that can help you with various tasks. Just send me a message and I will do my best to assist you!')

@bot.message_handler(func= lambda message: True)
def echo_all(message):
    # bot.reply_to(message, 'Unknonw command. Please use /start or /help to see the available commands.')
    bot.send_animation(
        message.chat.id, 
        'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGRjaHU0MTd3c3Y5bGJ0eW5vajE1bndxeTh5bjVjeDhuODd4YTZ4byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hxERQNWQudqSF1iDnr/giphy.gif', 
        caption='Unknonw command. Please use /start or /help to see the available commands.')
    


bot.polling(none_stop=True)