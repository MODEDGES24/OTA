from telegram.ext import Updater, CommandHandler

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Hello! I am your OTA bot.')

# Define a function to handle the /update command
def update(update, context):
    update.message.reply_text('New update is available! Download it from [update_link].')

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("7161001999:AAFebqCSgsfFZ8aOHx1bg_1NRn-OdtoKOQs")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /start command handler
    dp.add_handler(CommandHandler("start", start))

    # Register the /update command handler
    dp.add_handler(CommandHandler("update", update))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
