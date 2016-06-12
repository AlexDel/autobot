from telegramwrap import Bot
import nlrequestprocess as nl
from fetch import get_part_link
import logging
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
	greeting = 'Привет, автолюбитель! Я помогу тебе искать запчасти. Пиши, что тебе нужно.'
	bot.sendMessage(update.message.chat_id, text=greeting)


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def parse_message(bot, update):
		vendor = nl.parse_request(update.message.text)[0][0][0]
		link = get_part_link(vendor, 'accord', 'TODO')
		bot.sendMessage(update.message.chat_id, text=link)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    bot = Bot(start, help, parse_message, error)

if __name__ == '__main__':
    main()
