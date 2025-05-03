import telebot
import random
from config import token

# main.py
print(f"Token: {token}")
bot = telebot.TeleBot(token)
jokes = [
    "Почему утка перешла дорогу? Чтобы доказать, что она не курица!",
    "Я бы рассказал шутку про строительную работу, но я все еще над ней тружусь.",
    "Компьютер был холодным, потому что он открыл окна!",
    "Почему книга по математике грустила? Потому что у неё было слишком много проблем."
]

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke = random.choice(jokes)
    bot.reply_to(message, joke)
# Новый обработчик фотографий
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Wow, nice photo!")

# Старый обработчик текста
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
