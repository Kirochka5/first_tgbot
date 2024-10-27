import telebot
from password import *
# Замени '7613391452:AAGBqGV3e2bGxnB6m2sa9wszTQnE7h8mptU' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=['password'])  
def pas_gen(message): 
    bot.reply_to(message, password_gen())

@bot.message_handler(commands= ['emoje'])
def emgen_emodji(message):
    bot.reply_to(message, gen_emodji())

@bot.message_handler(commands= ['coin'])
def flip_coi(message):
    bot.reply_to(message, flip_coin())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()