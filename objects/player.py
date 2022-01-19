import logging
from datetime import datetime

from errors import DeckEmptyError
from gamethings.game import SINGLE
from objects.card import Card
from objects.combos import check_doubles, check_fives, check_quad, check_trio


class Player(object):
    """
    This class represents a player.
    It is basically a doubly-linked ring list with the option to reverse the
    direction. On initialization, it will connect itself to a game and its
    other players by placing itself behind the current player.
    """

    def __init__(self, game, user):
        self.cards = list()
        self.game = game
        self.user = user
        self.logger = logging.getLogger(__name__)

        # Check if this player is the first player in this game.
        if game.current_player:
            self.next = game.current_player
            self.prev = game.current_player.prev
            game.current_player.prev.next = self
            game.current_player.prev = self
        else:
            self._next = self
            self._prev = self
            game.current_player = self

        self.anti_cheat = 0
        self.turn_started = datetime.now()

    def draw_hand(self):
        try:
            for _ in range(int(52/len(self.game.players))):
                drew = self.game.deck.draw()
                
                self.cards.append(drew)
        except DeckEmptyError:
            self.logger.debug("NOT ENOUGH CARDS FROM DECK!")

            raise

    def leave(self):
        """Removes player from the game and closes the gap in the list"""
        if self.next is self:
            return

        self.next.prev = self.prev
        self.prev.next = self.next
        self.next = None
        self.prev = None

        for card in self.cards:
            self.game.deck.dismiss(card)

        self.cards = list()

    def __repr__(self):
        return repr(self.user)

    def __str__(self):
        return str(self.user)

    @property
    def next(self):
        return self._next 

    @next.setter
    def next(self, player):
        self._next = player

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, player):
        self._next = player

    def play(self, card): #single card
        """Plays a card and removes it from hand"""
        self.cards.remove(card)
        self.game.play_card(card)

    def playable_cards(self):
        """Returns a list of the cards this player can play right now"""

        playable = list()
        last = self.game.last_card

        self.logger.debug("Last card was " + str(last))

        cards = self.cards

        for card in cards:
            print(card)
            print(last)
            if self._card_playable(card):
                self.logger.debug("Matching!")
                playable.append(card)

        return playable

    def combos_playable(self):
        combos = []
        #doubles
        if check_doubles(self):
            combos.append('pair')
        if check_trio(self):
            combos.append('trio')
        if check_quad(self):
            combos.append('quad')
        if check_fives(self):
            combos.append('fives')
        return combos
        

    def _card_playable(self, card):

        is_playable = True
        last = self.game.last_card
        self.logger.debug("Checking card " + str(card))
        if(not last):
            last = Card('c', '0')
        if (card.value < last.value):
            self.logger.debug("Card is lower in value") 
            is_playable = False
        elif(card.value == last.value):
            if(not card.compare_suit(card, last)):
                is_playable = False
        return is_playable
