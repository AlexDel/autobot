from telegramwrap import Bot
import nlrequestprocess as nl
from fetch import get_part_link
import logging
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PROFANITY_ANSWERS = [
	"Чтобы я работал быстрее, купите премиум подписку. Бе.",
	"И не надейся, тест Тьюринга я пока не прохожу.",
	"С такими фразочками тебе к Яндексу."
]

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
	greeting = 'Привет, автолюбитель! Я помогу тебе искать запчасти. Пиши, что тебе нужно.'
	bot.sendMessage(update.message.chat_id, text=greeting)


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def parse_message(bot, update):
		request = nl.parse_request(update.message.text)
		if (request['profanity']):
			bot.sendMessage(update.message.chat_id, text=random.choice(PROFANITY_ANSWERS))
		link = get_part_link(request['vendor'], request['model'], request['part_name'])
		bot.sendMessage(update.message.chat_id, text=link)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    bot = Bot(start, help, parse_message, error)

if __name__ == '__main__':
    main()
