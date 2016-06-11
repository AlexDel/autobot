from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class Bot:
    def __init__(self, start, help, handler, error):
        # Create the EventHandler and pass it your bot's token.
        updater = Updater("215227616:AAEUAcjs4sh3GYCNX3_YdBVKMNuLhKmuf9c")
        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler([Filters.text], handler))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()