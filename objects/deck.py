from random import shuffle
import logging

from objects import card as c
from objects.card import Card
from errors import DeckEmptyError


class Deck(object):
    """ This class represents a deck of cards """

    def __init__(self):
        self.cards = list()
        self.graveyard = list()
        self.logger = logging.getLogger(__name__)
        self.logger.debug(self.cards)

    def shuffle(self):
        """Shuffles the deck"""
        self.logger.debug("Shuffling Deck")
        shuffle(self.cards)

    def draw(self):
        """Draws a card from this deck"""
        try:
            card = self.cards.pop()
            self.logger.debug("Drawing card " + str(card))
            return card
        except IndexError:
            self.logger.debug("No more cards from deck")

    def dismiss(self, card):
        """Returns a card to the deck"""
        self.graveyard.append(card)

    def _fill__(self):
        self.cards.clear()
        for suit in c.SUITS_VALUES.keys():
            for value in c.VALUE_VALUES.keys():
                self.cards.append(Card(suit, value))
        self.shuffle()