"""Defines helper functions to build the inline result list"""

from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, \
    InlineQueryResultCachedSticker as Sticker

from objects import card as c
from utils import display_suit, display_name



def player_list(game):
    """Generate list of player strings"""
    return ["{name} ({number} card)"
            .format(name=player.user.first_name, number=len(player.cards))
            for player in game.players]


def add_no_game(results):
    """Add text result if user is not playing"""
    results.append(
        InlineQueryResultArticle(
            "nogame",
            title=("You are not playing"),
            input_message_content=
            InputTextMessageContent(('Not playing right now. Use /new to '
                                      'start a game or /join to join the '
                                      'current game in this group'))
        )
    )

def add_choose_mode(results, player):
    """Add option which combo cards to drop"""
    if(len(player.playable_cards()) > 0):
        results.append(Sticker("singles", sticker_file_id='C:\\Users\\markr\\Desktop\\pony\\images\\webp\\singles.webp'))
        if player.combos_playable():
            for combo in player.combos_playable():
                results.append(Sticker(str(combo), sticker_file_id='C:\\Users\\markr\\Desktop\\pony\\images\\webp\\' + str(combo)))
    else:
        results.append(
            Sticker(
                "pass", sticker_file_id=c.STICKERS['option_pass'],
                input_message_content=InputTextMessageContent(
                    ('Pass')
                )
            )
        )
        
def add_not_started(results):
    """Add text result if the game has not yet started"""
    results.append(
        InlineQueryResultArticle(
            "nogame",
            title=("The game wasn't started yet"),
            input_message_content=
            InputTextMessageContent(('Start the game with /start'))
        )
    )


def add_gameinfo(game, results):
    """Add option to show game info"""

    results.append(
        Sticker(
            "gameinfo",
            sticker_file_id=c.STICKERS['option_info'],
            input_message_content=game_info(game)
        )
    )


def add_pass(results, game):
    """Add option to pass"""
    results.append(
        Sticker(
            "pass", sticker_file_id=c.STICKERS['option_pass'],
            input_message_content=InputTextMessageContent(
                ('Pass')
            )
        )
    )

def add_card(game, card, results, can_play):
    """Add an option that represents a card"""
    if can_play:
        results.append(
            Sticker(str(card), sticker_file_id='C:\\Users\\markr\\Desktop\\pony\\images\\webp\\'+str(card))
        )
    else:
        results.append(
            Sticker(str(uuid4()), sticker_file_id='C:\\Users\\markr\\Desktop\\pony\\images\\webp-lowsat\\'+str(card),
                    input_message_content=game_info(game))
        )


def game_info(game):
    players = player_list(game)
    return InputTextMessageContent(
        ("Current player: {name}")
        .format(name=display_name(game.current_player.user)) +
        "\n" +
        ("Last card: {card}").format(card=repr(game.last_card)) +
        "\n" +
        ("Players: {player_list}"
        .format(player_list=" -> ".join(players)))
    )
