from cmath import e
import logging
from datetime import datetime

from telegram import ParseMode, InlineKeyboardMarkup, \
    InlineKeyboardButton
from telegram.ext import InlineQueryHandler, ChosenInlineResultHandler, \
    CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

from objects import card as c #okay
import settings #okay
import simple_commands #okay
from actions import do_pass, do_play_card, do_draw
from config import MIN_PLAYERS
from errors import (NoGameInChatError, LobbyClosedError, AlreadyJoinedError,
                    NotEnoughPlayersError, DeckEmptyError)
from results import (add_gameinfo,
                     add_no_game, add_not_started, add_pass,
                     add_card, add_choose_mode)
from shared_vars import gm, updater, dispatcher
from simple_commands import help_handler
from start_bot import start_bot
from utils import display_name
from utils import send_async, answer_async, error, TIMEOUT, user_is_creator_or_admin, user_is_creator, game_is_running


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def new_game(bot, update):
    """Handler for the /new command"""
    chat_id = update.message.chat_id
    if update.message.chat.type == 'private':
        help_handler(bot, update)
    else:
        game = gm.new_game(update.message.chat)
        game.owner.append(update.message.from_user.id)
        send_async(bot, chat_id,
                   text=("Created a new game! Join the game with /join "
                          "and start the game with /start"))

def kill_game(bot, update):
    """Handler for the /kill command"""
    chat = update.message.chat
    user = update.message.from_user
    games = gm.chatid_games.get(chat.id)

    if update.message.chat.type == 'private':
        help_handler(bot, update)
        return

    if not games:
            send_async(bot, chat.id,
                       text=("There is no running game in this chat."))
            return

    game = games[-1]

    if user_is_creator_or_admin(user, game, bot, chat):

        try:
            gm.end_game(chat, user)
            send_async(bot, chat.id, text=("Game ended!"))

        except NoGameInChatError:
            send_async(bot, chat.id,
                       text=("The game is not started yet. "
                              "Join the game with /join and start the game with /start"),
                       reply_to_message_id=update.message.message_id)

    else:
        send_async(bot, chat.id,
                  text=("Only the game creator ({name}) and admin can do that.")
                  .format(name=game.starter.first_name),
                  reply_to_message_id=update.message.message_id)

def join_game(bot, update):
    """Handler for the /join command"""
    chat = update.message.chat
    if update.message.chat.type == 'private':
        help_handler(bot, update)
        return
    try:
        gm.join_game(update.message.from_user, chat)
    except LobbyClosedError:
        send_async(bot, chat.id, text=("The lobby is closed"))
    except NoGameInChatError:
        send_async(bot, chat.id,
                   text=("No game is running at the moment. "
                          "Create a new game with /new"),
                   reply_to_message_id=update.message.message_id)
    except AlreadyJoinedError:
        send_async(bot, chat.id,
                   text=("You already joined the game. Start the game "
                          "with /start"),
                   reply_to_message_id=update.message.message_id)
    else:
        send_async(bot, chat.id,
                   text=("Joined the game"),
                   reply_to_message_id=update.message.message_id)


def leave_game(bot, update):
    """Handler for the /leave command"""
    chat = update.message.chat
    user = update.message.from_user

    player = gm.player_for_user_in_chat(user, chat)

    if player is None:
        send_async(bot, chat.id, text=("You are not playing in a game in "
                                        "this group."),
                   reply_to_message_id=update.message.message_id)
        return

    game = player.game
    user = update.message.from_user

    try:
        gm.leave_game(user, chat)

    except NoGameInChatError:
        send_async(bot, chat.id, text=("You are not playing in a game in "
                                        "this group."),
                   reply_to_message_id=update.message.message_id)

    except NotEnoughPlayersError:
        gm.end_game(chat, user)
        send_async(bot, chat.id, text=("Game ended!", ))

    else:
        if game.started:
            send_async(bot, chat.id,
                       text=("Okay. Next Player: {name}",
                               ).format(
                           name=display_name(game.current_player.user)),
                       reply_to_message_id=update.message.message_id)
        else:
            send_async(bot, chat.id,
                       text=("{name} left the game before it started.",
                               ).format(
                           name=display_name(user)),
                       reply_to_message_id=update.message.message_id)


def kick_player(bot, update):
    """Handler for the /kick command"""

    if update.message.chat.type == 'private':
        help_handler(bot, update)
        return

    chat = update.message.chat
    user = update.message.from_user

    try:
        game = gm.chatid_games[chat.id][-1]

    except (KeyError, IndexError):
            send_async(bot, chat.id,
                   text=("No game is running at the moment. "
                          "Create a new game with /new"),
                   reply_to_message_id=update.message.message_id)
            return

    if not game.started:
        send_async(bot, chat.id,
                   text=("The game is not started yet. "
                          "Join the game with /join and start the game with /start"),
                   reply_to_message_id=update.message.message_id)
        return

    if user_is_creator_or_admin(user, game, bot, chat):

        if update.message.reply_to_message:
            kicked = update.message.reply_to_message.from_user

            try:
                gm.leave_game(kicked, chat)

            except NoGameInChatError:
                send_async(bot, chat.id, text=("Player {name} is not found in the current game.".format(name=display_name(kicked))),
                                reply_to_message_id=update.message.message_id)
                return

            except NotEnoughPlayersError:
                gm.end_game(chat, user)
                send_async(bot, chat.id,
                                text=("{0} was kicked by {1}".format(display_name(kicked), display_name(user))))
                send_async(bot, chat.id, text=("Game ended!"))
                return

            send_async(bot, chat.id,
                            text=("{0} was kicked by {1}".format(display_name(kicked), display_name(user))))

        else:
            send_async(bot, chat.id,
                text=("Please reply to the person you want to kick and type /kick again."),
                reply_to_message_id=update.message.message_id)
            return

        send_async(bot, chat.id,
                   text=("Okay. Next Player: {name}",
                           ).format(
                       name=display_name(game.current_player.user)),
                   reply_to_message_id=update.message.message_id)

    else:
        send_async(bot, chat.id,
                  text=("Only the game creator ({name}) and admin can do that.")
                  .format(name=game.starter.first_name),
                  reply_to_message_id=update.message.message_id)


def select_game(bot, update):
    """Handler for callback queries to select the current game"""

    chat_id = int(update.callback_query.data)
    user_id = update.callback_query.from_user.id
    players = gm.userid_players[user_id]
    for player in players:
        if player.game.chat.id == chat_id:
            gm.userid_current[user_id] = player
            break
    else:
        send_async(bot,
                   update.callback_query.message.chat_id,
                   text=("Game not found."))
        return

    @run_async
    def selected(bot):
        back = [[InlineKeyboardButton(text=("Back to last group"),
                                      switch_inline_query='')]]
        bot.answerCallbackQuery(update.callback_query.id,
                                text=("Please switch to the group you selected!"),
                                show_alert=False,
                                timeout=TIMEOUT)

        bot.editMessageText(chat_id=update.callback_query.message.chat_id,
                            message_id=update.callback_query.message.message_id,
                            text=("Selected group: {group}\n"
                                   "<b>Make sure that you switch to the correct "
                                   "group!</b>").format(
                                group=gm.userid_current[user_id].game.chat.title),
                            reply_markup=InlineKeyboardMarkup(back),
                            parse_mode=ParseMode.HTML,
                            timeout=TIMEOUT)

    selected(bot)


def status_update(bot, update):
    """Remove player from game if user leaves the group"""
    chat = update.message.chat

    if update.message.left_chat_member:
        user = update.message.left_chat_member

        try:
            gm.leave_game(user, chat)
            game = gm.player_for_user_in_chat(user, chat).game

        except NoGameInChatError:
            pass
        except NotEnoughPlayersError:
            gm.end_game(chat, user)
            send_async(bot, chat.id, text=("Game ended!"))
        else:
            send_async(bot, chat.id, text=("Removing {name} from the game"
                                             )
                       .format(name=display_name(user)))


def start_game(bot, update, args, job_queue):
    """Handler for the /start command"""
    if update.message.chat.type != 'private':
        chat = update.message.chat
        try:
            game = gm.chatid_games[chat.id][-1]
            
        except (KeyError, IndexError):
            send_async(bot, chat.id,
                       text=("There is no game running in this chat. Create "
                              "a new one with /new"))
            return
        if game.started:
            send_async(bot, chat.id, text=("The game has already started"))
        elif len(game.players) < MIN_PLAYERS:
            send_async(bot, chat.id,
                       text=("At least {minplayers} players must /join the game "
                              "before you can start it").format(minplayers=MIN_PLAYERS))
        else:
            game.start()
            for player in game.players:
                player.draw_hand()
                player.look_for_combos()
                if('c_3' in player.cards):
                    game.current_player = player
                    game.starter = game.current_player
            choice = [[InlineKeyboardButton(text=("Make your choice!"), switch_inline_query_current_chat='')]]
            first_message = (
                ("First player: {name}\n").format(name=display_name(game.current_player.user)))
            @run_async
            def move_first():
                bot.sendMessage(chat.id,
                                text=first_message,
                                reply_markup=InlineKeyboardMarkup(choice),
                                timeout=TIMEOUT)

            move_first()

    elif len(args) and args[0] == 'select':
        players = gm.userid_players[update.message.from_user.id]

        groups = list()
        for player in players:
            title = player.game.chat.title

            if player is gm.userid_current[update.message.from_user.id]:
                title = '- %s -' % player.game.chat.title

            groups.append(
                [InlineKeyboardButton(text=title,
                                      callback_data=str(player.game.chat.id))]
            )

        send_async(bot, update.message.chat_id,
                   text=('Please select the group you want to play in.'),
                   reply_markup=InlineKeyboardMarkup(groups))

    else:
        help_handler(bot, update)

def close_game(bot, update):
    """Handler for the /close command"""
    chat = update.message.chat
    user = update.message.from_user
    games = gm.chatid_games.get(chat.id)

    if not games:
        send_async(bot, chat.id,
                   text=("There is no running game in this chat."))
        return

    game = games[-1]

    if user.id in game.owner:
        game.open = False
        send_async(bot, chat.id, text=("Closed the lobby. "
                                        "No more players can join this game."))
        return

    else:
        send_async(bot, chat.id,
                   text=("Only the game creator ({name}) and admin can do that.")
                   .format(name=game.starter.first_name),
                   reply_to_message_id=update.message.message_id)
        return
def open_game(bot, update):
    """Handler for the /open command"""
    chat = update.message.chat
    user = update.message.from_user
    games = gm.chatid_games.get(chat.id)

    if not games:
        send_async(bot, chat.id,
                   text=("There is no running game in this chat."))
        return

    game = games[-1]

    if user.id in game.owner:
        game.open = True
        send_async(bot, chat.id, text=("Opened the lobby. "
                                        "New players may /join the game."))
        return
    else:
        send_async(bot, chat.id,
                   text=("Only the game creator ({name}) and admin can do that.")
                   .format(name=game.starter.first_name),
                   reply_to_message_id=update.message.message_id)
        return
def pass_player(bot, update):
    """Handler for the /skip command"""
    chat = update.message.chat
    user = update.message.from_user

    player = gm.player_for_user_in_chat(user, chat)
    if not player:
        send_async(bot, chat.id,
                   text=("You are not playing in a game in this chat."))
        return

    game = player.game
    skipped_player = game.current_player

    started = skipped_player.turn_started
    now = datetime.now()
    delta = (now - started).seconds

    if delta < skipped_player.waiting_time and player != skipped_player:
        n = skipped_player.waiting_time - delta
        send_async(bot, chat.id,
                   text=("Please wait {time} second",
                          "Please wait {time} seconds",
                          n)
                   .format(time=n),
                   reply_to_message_id=update.message.message_id)
    else:
        do_pass(bot, player)

def reply_to_query(bot, update): #mag popop-up to choose sticker
    """
    Handler for inline queries.
    Builds the result list for inline queries and answers to the client.
    """
    results = list()   
    try:
        user = update.inline_query.from_user
        user_id = user.id
        players = gm.userid_players[user_id]
        player = gm.userid_current[user_id]
        game = player.game
    except KeyError:
        add_no_game(results)
    else:
        # The game has not started.
        # The creator may change the game mode, other users just get a "game has not started" message.
        if not game.started:
            if user_is_creator(user, game):
                game.start()
            else:
                add_not_started(results)

        elif user_id == game.current_player.user.id:
            playable = player.playable_cards()
            if(not game.mode):
                add_choose_mode(results, game.current_player, playable)
                add_pass(results, game)
            elif player.countmode == int(game.mode):
                add_pass(results, game)
            added_ids = list()  # Duplicates are not allowed
            for card in sorted(player.cards):
                add_card(game, card, results,
                        can_play=(card in playable[0] and
                                        str(card) not in added_ids))
                added_ids.append(str(card))
            add_gameinfo(game, results)

        elif user_id != game.current_player.user.id or not game.started:
            for card in sorted(player.cards):
                add_card(game, card, results, can_play=False)
        else:
            add_gameinfo(game, results)

        for result in results:
            result.id += ':%d' % player.anti_cheat

        for i in range(1, len(results)):
            for j in range(i+1, len(results)):
                if results[i] == results[j]:
                    print("DUPLICATE FOUND!")
    
    answer_async(bot, update.inline_query.id, results, cache_time=0)


def process_result(bot, update, job_queue):
    """
    Handler for chosen inline results.
    Checks the players actions and acts accordingly.
    """
    try:
        user = update.chosen_inline_result.from_user
        player = gm.userid_current[user.id]
        game = player.game
        result_id = update.chosen_inline_result.result_id
        chat = game.chat
    except (KeyError, AttributeError):
        return

    logger.debug("Selected result: " + result_id)

    result_id, anti_cheat = result_id.split(':')
    last_anti_cheat = player.anti_cheat
    player.anti_cheat += 1

    if result_id in ('hand', 'gameinfo', 'nogame'):
        return
    elif result_id.startswith('mode_'):
        # First 5 characters are 'mode_', the rest is the gamemode.
        mode = result_id[5:]
        game.set_mode(mode)
        logger.info("Gamemode changed to {mode}".format(mode = mode))
        choice = [[InlineKeyboardButton(text=("Make your choice!"), switch_inline_query_current_chat='')]]
        send_async(bot, chat.id, text=("Gamemode changed to {mode}! You can now drop {mode} cards as a combo consecutively!".format(mode = mode)),
                        reply_markup = InlineKeyboardMarkup(choice))
        return
    elif len(result_id) == 36:  # UUID result
        return
    elif int(anti_cheat) != last_anti_cheat:
        send_async(bot, chat.id,
                   text=("Cheat attempt by {name}")
                   .format(name=display_name(player.user)))
        return
    elif result_id == 'draw':
        do_draw(bot, player)
    elif result_id == 'pass':
        if game.last_card_owner == None:
            game.mode = None
            choice = [[InlineKeyboardButton(text=("Make your choice!"), switch_inline_query_current_chat='')]]
            send_async(bot, chat.id, text = "Can't pass, you have the starting card!", reply_markup = InlineKeyboardMarkup(choice))
            return
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
            game.last_card = c.Card('c', '3')
            game.last_high = None
            game.last_five_rank = None
    else:
        if(game.mode == None):
            choice = [[InlineKeyboardButton(text=("Make your choice!"), switch_inline_query_current_chat='')]]
            send_async(bot, chat.id, text=("Game mode not set! Please choose how many cards you are going to play."),
                            reply_markup = InlineKeyboardMarkup(choice))
            return
        if(game.last_card.value == '0' and result_id != 'c_3'):
            choice = [[InlineKeyboardButton(text=("Make your choice!"), switch_inline_query_current_chat='')]]
            send_async(bot, chat.id, text=("3 of Clubs must be dropped first to start the game!"),
                            reply_markup = InlineKeyboardMarkup(choice))
            return
        do_play_card(bot, player, result_id)

    if game_is_running(game):
        combo = '\n'
        if len(game.current_combo) > 0:    
            combo += "Combo so far:" + str(game.current_combo) 
        nextplayer_message = (
            ("Next player: {name}" + combo)
            .format(name=display_name(game.current_player.user)))
        choice = [[InlineKeyboardButton(text=("Make your choice!"), switch_inline_query_current_chat='')]]
        send_async(bot, chat.id,
                        text=nextplayer_message,
                        reply_markup=InlineKeyboardMarkup(choice))



dispatcher.add_handler(InlineQueryHandler(reply_to_query))
dispatcher.add_handler(ChosenInlineResultHandler(process_result, pass_job_queue=True))
dispatcher.add_handler(CallbackQueryHandler(select_game))
dispatcher.add_handler(CommandHandler('start', start_game, pass_args=True, pass_job_queue=True))
dispatcher.add_handler(CommandHandler('new', new_game))
dispatcher.add_handler(CommandHandler('kill', kill_game))
dispatcher.add_handler(CommandHandler('join', join_game))
dispatcher.add_handler(CommandHandler('leave', leave_game))
dispatcher.add_handler(CommandHandler('kick', kick_player))
dispatcher.add_handler(CommandHandler('open', open_game))
dispatcher.add_handler(CommandHandler('close', close_game))
dispatcher.add_handler(CommandHandler('skip', pass_player))
simple_commands.register()
settings.register()
dispatcher.add_handler(MessageHandler(Filters.status_update, status_update))
dispatcher.add_error_handler(error)

start_bot(updater)
updater.idle()
