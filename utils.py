import logging
from telegram.ext.dispatcher import run_async
from mwt import MWT
from shared_vars import gm

logger = logging.getLogger(__name__)

TIMEOUT = 2.5


def list_subtract(list1, list2):
    """ Helper function to subtract two lists and return the sorted result """
    list1 = list1.copy()

    for x in list2:
        list1.remove(x)

    return list(sorted(list1))


def display_name(user):
    """ Get the current players name including their username, if possible """
    user_name = user.first_name
    if user.username:
        user_name += ' (@' + user.username + ')'
    return user_name


def display_suit(suit):
    """ Convert a color code to actual color name """
    if suit == "d":
        return ("{emoji} Diamonds").format(emoji='♦')
    if suit == "s":
        return ("{emoji} Spades").format(emoji='♠')
    if suit == "h":
        return ("{emoji} Hearts").format(emoji='♥')
    if suit == "c":
        return ("{emoji} Clubs").format(emoji='♣')

def error(bot, update, error):
    """Simple error handler"""
    logger.exception(error)


@run_async
def send_async(bot, *args, **kwargs):
    """Send a message asynchronously"""
    if 'timeout' not in kwargs:
        kwargs['timeout'] = TIMEOUT
    try:
        bot.sendMessage(*args, **kwargs)
    except Exception as e:
        error(None, None, e)

@run_async
def answer_async(bot, *args, **kwargs):
    """Answer an inline query asynchronously"""
    if 'timeout' not in kwargs:
        kwargs['timeout'] = TIMEOUT
    try:
        bot.answerInlineQuery(*args, **kwargs)
    except Exception as e:
        error(None, None, e)


def game_is_running(game):
    return game in gm.chatid_games.get(game.chat.id, list())


def user_is_creator(user, game):
    return user.id in game.owner


def user_is_admin(user, bot, chat):
    return user.id in get_admin_ids(bot, chat.id)


def user_is_creator_or_admin(user, game, bot, chat):
    return user_is_creator(user, game) or user_is_admin(user, bot, chat)


@MWT(timeout=60*60)
def get_admin_ids(bot, chat_id):
    """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]
