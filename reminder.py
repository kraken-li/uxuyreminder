import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
import time

# Your bot token
TOKEN = '7530138826:AAFlcQzkzIwxCOtqy5LMtY9WsvynNSSWkRI'

# Function to send reminder messages
def send_reminder(context: CallbackContext):
    chat_id = '1299645802'
    context.bot.send_message(chat_id=chat_id, text="Don't forget to open @UXUYbot!")

# Function to start the bot and set up the hourly reminders
def start(update, context):
    context.job_queue.run_repeating(send_reminder, interval=3600, first=0)
    update.message.reply_text('Reminder set!')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
