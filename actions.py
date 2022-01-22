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

class Countdown(object):
    player = None
    job_queue = None

    def __init__(self, player, job_queue):
        self.player = player
        self.job_queue = job_queue

def do_pass(bot, player, job_queue=None):
    game = player.game
    chat = game.chat
    skipped_player = game.current_player
    next_player = game.current_player.next

    n = skipped_player.waiting_time
    send_async(bot, chat.id,
               text=("Waiting time to skip this player has "
                    "been reduced to {time} seconds.\n"
                    "Next player: {name}")
               .format(time=n,
                       name=display_name(next_player.user))
    )
    logger.info("{player} was skipped! "
                .format(player=display_name(player.user)))
    if game.mode != None:
        if len(game.current_combo) > 0:
            send_async(bot, chat.id,
               text=("Can't pass when a combo has started!")
            )
            return
        game.mode = None
    game.turn()
    if game.current_player.user == game.last_card_owner.user:
        game.mode = None

def do_play_card(bot, player, result_id):
    """Plays the selected card and sends an update to the group if needed"""
    card = c.from_str(result_id)
    player.play(card)
    game = player.game
    chat = game.chat
    user = player.user

    """     us = UserSetting.get(id=user.id)
    if not us:
        us = UserSetting(id=user.id)

    if us.stats:
        us.cards_played += 1 """
        
    if len(player.cards) == 1:
        send_async(bot, chat.id, text="UNO!")

    if len(player.cards) == 0:
        send_async(bot, chat.id,
                   text=("{name} won!")
                   .format(name=user.first_name))

        """         if us.stats:
            us.games_played += 1

            if game.players_won == 0:
                us.first_places += 1 """

        game.players_won += 1

        try:
            gm.leave_game(user, chat)
        except NotEnoughPlayersError:
            send_async(bot, chat.id,
                       text=("Game ended!"))

            gm.end_game(chat, user)


def do_draw(bot, player):
    """Does the drawing"""
    game = player.game
    draw_counter_before = game.draw_counter

    try:
        player.draw()
    except DeckEmptyError:
        send_async(bot, player.game.chat.id,
                   text=("There are no more cards in the deck."
                           ))

    if (game.last_card.value == c.DRAW_TWO or
        game.last_card.special == c.DRAW_FOUR) and \
            draw_counter_before > 0:
        game.turn()

def skip_job(bot, job):
    player = job.context.player
    game = player.game
    if game_is_running(game):
        job_queue = job.context.job_queue
        do_pass(bot, player, job_queue)
