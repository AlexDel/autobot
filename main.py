from telegramwrap import Bot
import nlrequestprocess as nl
import logging
import random

LATIN_QUOTES = [
    "CAESAR NON SUPRA GRAMMATICOS",
    "CARPE NOCTEM",
    "CARTHAGO DELENDA EST",
    "CASTIGAT RIDENDO MORES",
    "CORVUS OCULUM CORVI NON ERUIT",
    "CUI BONO?",
    "ET IN ARCADIA EGO",
    "EX NIHILO NIHIL FIT",
    "FELIX CULPA",
    "HANNIBAL AD PORTAS",
    "HIC MANEBIMUS OPTIME",
    "HOMO SUM HUMANI A ME NIHIL ALIENUM PUTO",
    "IGNOTUM PER IGNOTIUS",
    "IMPERIUM IN IMPERIO",
    "PANEM ET CIRCENSES",
    "VELOCIUS QUAM ASPARAGI COQUANTUR",
    "VOX NIHILI",
]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def parse_message(bot, update):
    bot.sendMessage(update.message.chat_id, text=str(nl.parse_request(update.message.text)))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    bot = Bot(start, help, parse_message, error)

if __name__ == '__main__':
    main()
