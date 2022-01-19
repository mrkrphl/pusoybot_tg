import logging
from config import ADMIN_LIST, OPEN_LOBBY
from datetime import datetime

from objects.deck import Deck
from objects import card as c

SINGLE = 'ones'
PAIR = 'twos'
TRIO = 'threes'
QUADS= 'fours'
FIVES = 'fives'

MODES = (SINGLE, PAIR, TRIO, QUADS, FIVES)

class Game(object):
    """ This class represents a game of PUSOY DOS """
    current_player = None
    started = False
    players_won = 0
    starter = None
    job = None
    owner = ADMIN_LIST
    open = OPEN_LOBBY

    def __init__(self, chat):
        self.chat = chat
        self.last_card = None
        self.deck = Deck()
        self.logger = logging.getLogger(__name__)

    @property
    def players(self):
        """Returns a list of all players in this game"""
        players = list()
        if not self.current_player:
            return players

        current_player = self.current_player
        itplayer = current_player.next
        players.append(current_player)
        while itplayer and itplayer is not current_player:
            players.append(itplayer)
            itplayer = itplayer.next
        return players

    def start(self):
        self.deck._fill__()
        self.started = True
        self.mode = None
        self.starter = None

    def turn(self):
        """Marks the turn as over and change the current player"""
        self.logger.debug("Next Player")
        self.current_player = self.current_player.next
        self.current_player.turn_started = datetime.now()

    def play_card(self, card): #for single cards
        """
        Plays a card and triggers its effects.
        Should be called only from Player.play or on game start to play the
        first card
        """
        self.deck.dismiss(self.last_card)
        self.last_card = card

        self.logger.info("Playing card " + repr(card))

