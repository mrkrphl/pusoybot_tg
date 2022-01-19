from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, RegexHandler

from utils import send_async
from entities.entity import usersettings
from shared_vars import dispatcher

UserSetting = usersettings
def show_settings(bot, update):
    chat = update.message.chat
    if update.message.chat.type != 'private':
        send_async(bot, chat.id,
                   text=("Please edit your settings in a private chat with "
                          "the bot."))
        return

    us = UserSetting.get(id=update.message.from_user.id)
    
    if not us:
        us = UserSetting(id=update.message.from_user.id)

    if not us.stats:
        stats = '📊' + ' ' + ("Enable statistics")
    else:
        stats = '❌' + ' ' + ("Delete all statistics")

    kb = [[stats], ['🌍' + ' ' + ("Language")]]
    send_async(bot, chat.id, text='🔧' + ' ' + ("Settings"),
               reply_markup=ReplyKeyboardMarkup(keyboard=kb,
                                                one_time_keyboard=True))

def kb_select(bot, update, groups):
    chat = update.message.chat
    user = update.message.from_user
    option = groups[0]

    if option == '📊':
        us = UserSetting.get(id=user.id)
        us.stats = True
        send_async(bot, chat.id, text=("Enabled statistics!"))

    elif option == '❌':
        us = UserSetting.get(id=user.id)
        us.stats = False
        us.first_places = 0
        us.games_played = 0
        us.cards_played = 0
        send_async(bot, chat.id, text=("Deleted and disabled statistics!"))


def register():
    dispatcher.add_handler(CommandHandler('settings', show_settings))
    dispatcher.add_handler(RegexHandler('^([' + '📊' +
                                        '🌍' +
                                        '❌' + ']) .+$',
                                        kb_select, pass_groups=True))

