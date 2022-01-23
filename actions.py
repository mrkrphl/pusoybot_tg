import random
import logging
from objects import card as c
from datetime import datetime
from telegram import Message, Chat
from errors import DeckEmptyError, NotEnoughPlayersError
from shared_vars import gm
from entities.entity import usersettings as UserSetting
from utils import send_async, display_name, game_is_running

logger = logging.getLogger(__name__)

def do_play_card(bot, player, result_id):
    """Plays the selected card and sends an update to the group if needed"""
    card = c.from_str(result_id)
    player.play(card)
    game = player.game
    chat = game.chat
    user = player.user

    if len(player.cards) == 1:
        send_async(bot, chat.id, text="UNO!")

    if len(player.cards) == 0:
        send_async(bot, chat.id,
                   text=("{name} won!")
                   .format(name=user.first_name))

        game.players_won += 1

        try:
            gm.leave_game(user, chat)
        except NotEnoughPlayersError:
            send_async(bot, chat.id,
                       text=("Game ended!"))

            gm.end_game(chat, user)

