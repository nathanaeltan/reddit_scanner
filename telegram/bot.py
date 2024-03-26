import telebot
import os
import requests, threading
from dotenv import load_dotenv

from utils import generate_html

load_dotenv()
import time

bot = telebot.TeleBot(os.getenv('TELEGRAM_MEME_TOKEN'))
API_URL = os.getenv('API_URL') or 'http://127.0.0.1:8000/'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello and welcome to meme bot, send /memes to get the latest memes')


@bot.message_handler(commands=['memes'])
def get_memes(message):
    bot.send_chat_action(message.chat.id, 'typing')
    memes = requests.post(f'{API_URL}api/memes', {}).json()
    file_path = "meme_data.html"
    with open(file_path, 'w') as html_file:
        html_content = generate_html(memes)
        html_file.write(html_content)

    # Send the file as a document
    with open(file_path, 'rb') as file:
        bot.send_document(message.chat.id, file)

    # Delete the temporary file
    os.unlink(file_path)

    bot.reply_to(message, 'Here are the latest memes')


if __name__ == '__main__':
    print('Bot started!')
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        time.sleep(1)
