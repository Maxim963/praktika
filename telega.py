import telebot
#from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-
#from telegram.ext import CommandHandler
bot = telebot.TeleBot("847470738:AAHJVmbUM0-ihXeBWZmz6FtLYkbd72UcfmI")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop = True)
