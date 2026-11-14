import os
import telebot
from flask import Flask
import threading

# 1-қадамда алған токенді мына жерге жазасыз:
TOKEN = '9221861288:AAF9TeXCQtZ8dFl3obeyKJnH6w6ghKrGyg8'
bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Саламатсыз ба! Бот сәтті жұмыс істей бастады.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Сіз жаздыңыз: {message.text}")

@server.route('/')
def index():
    return "Bot is running!", 200

def run_bot():
    bot.infinity_polling(none_stop=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()

    server.run(host='0.0.0.0', port=port)