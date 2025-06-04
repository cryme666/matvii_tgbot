import telebot,os
from telebot import types
from dotenv import load_dotenv
from gif_search import get_gif_url 
from img_search import get_photo_url

load_dotenv()

BOT_API = os.getenv('BOT_API')

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! I am a bot that can help you with various tasks. Just send me a message and I will do my best to assist you!')


@bot.message_handler(func =lambda message: True)
def echo_all(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    gif_btn = types.InlineKeyboardButton('GIF', callback_data=f'gif_{message.text}')
    img_btn = types.InlineKeyboardButton('Image', callback_data=f'img_{message.text}')
    markup.add(gif_btn, img_btn)
    bot.send_message(message.chat.id, 'Choose what you want to search:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    call_data = call.data.split('_')[0]
    query = call.data.split('_')[1]

    if call_data == 'gif':
        gif_url = get_gif_url(query)
        if gif_url:
            bot.send_animation(call.message.chat.id, gif_url)
        else:
            bot.send_message(call.message.chat.id, 'No GIF found for your query.')
    elif call_data == 'img':
        img_url = get_photo_url(query)
        if img_url:
            bot.send_photo(call.message.chat.id, img_url)
        else:
            bot.send_message(call.message.chat.id, 'No image found for your query.')
    
    
print("Bot is running...")    
bot.polling(none_stop=True)
