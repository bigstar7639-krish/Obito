import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Yo! I'm Obito 🔥\nReady to rock da!")

@bot.message_handler(func=lambda m: True)
def all_msg(message):
    bot.reply_to(message, f"Obito here: {message.text}")

print("Obito Running...")
bot.infinity_polling()
