
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os

my_token = '623831699:AAF3bHHFnyQYWzcoH9O9Q1yC2m0-SFZ25ZA'
print('Start telegram chat bot')
dir_now = os.path.dirname(os.path.abspath(__file__))

def get_message(bot, update):
    update.message.reply_text("Got text")
    update.message.reply_text(update.message.text)

def help_command(bot, update):
    update.message.reply_text("What Can I help you?")

def get_photo(bot, update):
    file_name = 'from_telegram.png'
    file_path = os.path.join(dir_now, file_name)
    photo_id = update.message.photo[-1].file_id
    photo_file = bot.getFile(photo_id)
    photo_file.download(file_path)
    update.message.reply_text("Photo Saved")

def get_file(bot, update):
    file_id_short = update.message.document.file_id
    file_url = os.path.join(dir_now, update.message.document.file_name)
    bot.getFile(file_id_short).download(file_url)
    update.message.reply_text('File Saved')

updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler('help', help_command)
updater.dispatcher.add_handler(help_handler)

photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()

#import telegram
#my_token = '623831699:AAF3bHHFnyQYWzcoH9O9Q1yC2m0-SFZ25ZA'
#bot = telegram.Bot(token=my_token)
#id_channel = bot.sendMessage(chat_id = '@behindtest', text='MyStar2').chat_id
#print(id_channel)
#bot.sendMessage(chat_id = id_channel, text='MyStar3')