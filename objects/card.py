#Suits
DIAMONDS = 'd'
SPADES = 's'
HEARTS = 'h'
CLUBS = 'c'

SUITS = (DIAMONDS, SPADES, HEARTS, CLUBS)
SUIT_ICONS = {
    DIAMONDS:'♦',
    SPADES:'♠',
    HEARTS: '♥',
    CLUBS: '♣'
}

tao = {'A':'1', 'J':'11', 'Q':'12', 'K':'13'}

# Values
ACE = 'A'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
TEN = '10'
JACK = 'J'
QUEEN = 'Q'
KING = 'K'

VALUES = (ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN,
          JACK, QUEEN, KING)

STICKERS = {
    'd_A': 'BQADBAAD2QEAAl9XmQAB--inQsYcLTsC',
    'd_1': 'BQADBAAD2wEAAl9XmQABBzh4U-rFicEC',
    'd_2': 'BQADBAAD3QEAAl9XmQABo3l6TT0MzKwC',
    'd_3': 'BQADBAAD3wEAAl9XmQAB2y-3TSapRtIC',
    'd_4': 'BQADBAAD4QEAAl9XmQABT6nhOuolqKYC',
    'd_5': 'BQADBAAD4wEAAl9XmQABwRfmekGnpn0C',
    'd_6': 'BQADBAAD5QEAAl9XmQABQITgUsEsqxsC',
    'd_7': 'BQADBAAD5wEAAl9XmQABVhPF6EcfWjEC',
    'd_8': 'BQADBAAD6QEAAl9XmQABP6baig0pIvYC',
    'd_9': 'BQADBAAD6wEAAl9XmQAB0CQdsQs_pXIC',
    'd_10': 'BQADBAAD7QEAAl9XmQAB00Wii7R3gDUC',
    'd_J': 'BQADBAAD8QEAAl9XmQAB_RJHYKqlc-wC',
    'd_Q': 'BQADBAAD7wEAAl9XmQABo7D0B9NUPmYC',
    'd_K': 'BQADBAAD9wEAAl9XmQABb8CaxxsQ-Y8C',
    's_A': 'BQADBAAD2QEAAl9XmQAB--inQsYcLTsC',
    's_1': 'BQADBAAD2wEAAl9XmQABBzh4U-rFicEC',
    's_2': 'BQADBAAD3QEAAl9XmQABo3l6TT0MzKwC',
    's_3': 'BQADBAAD3wEAAl9XmQAB2y-3TSapRtIC',
    's_4': 'BQADBAAD4QEAAl9XmQABT6nhOuolqKYC',
    's_5': 'BQADBAAD4wEAAl9XmQABwRfmekGnpn0C',
    's_6': 'BQADBAAD5QEAAl9XmQABQITgUsEsqxsC',
    's_7': 'BQADBAAD5wEAAl9XmQABVhPF6EcfWjEC',
    's_8': 'BQADBAAD6QEAAl9XmQABP6baig0pIvYC',
    's_9': 'BQADBAAD6wEAAl9XmQAB0CQdsQs_pXIC',
    's_10': 'BQADBAAD7QEAAl9XmQAB00Wii7R3gDUC',
    's_J': 'BQADBAAD8QEAAl9XmQAB_RJHYKqlc-wC',
    's_Q': 'BQADBAAD7wEAAl9XmQABo7D0B9NUPmYC',
    's_K': 'BQADBAAD9wEAAl9XmQABb8CaxxsQ-Y8C',
    'h_A': 'BQADBAAD2QEAAl9XmQAB--inQsYcLTsC',
    'h_1': 'BQADBAAD2wEAAl9XmQABBzh4U-rFicEC',
    'h_2': 'BQADBAAD3QEAAl9XmQABo3l6TT0MzKwC',
    'h_3': 'BQADBAAD3wEAAl9XmQAB2y-3TSapRtIC',
    'h_4': 'BQADBAAD4QEAAl9XmQABT6nhOuolqKYC',
    'h_5': 'BQADBAAD4wEAAl9XmQABwRfmekGnpn0C',
    'h_6': 'BQADBAAD5QEAAl9XmQABQITgUsEsqxsC',
    'h_7': 'BQADBAAD5wEAAl9XmQABVhPF6EcfWjEC',
    'h_8': 'BQADBAAD6QEAAl9XmQABP6baig0pIvYC',
    'h_9': 'BQADBAAD6wEAAl9XmQAB0CQdsQs_pXIC',
    'h_10': 'BQADBAAD7QEAAl9XmQAB00Wii7R3gDUC',
    'h_J': 'BQADBAAD8QEAAl9XmQAB_RJHYKqlc-wC',
    'h_Q': 'BQADBAAD7wEAAl9XmQABo7D0B9NUPmYC',
    'h_K': 'BQADBAAD9wEAAl9XmQABb8CaxxsQ-Y8C',
    'c_A': 'BQADBAAD2QEAAl9XmQAB--inQsYcLTsC',
    'c_1': 'BQADBAAD2wEAAl9XmQABBzh4U-rFicEC',
    'c_2': 'BQADBAAD3QEAAl9XmQABo3l6TT0MzKwC',
    'c_3': 'BQADBAAD3wEAAl9XmQAB2y-3TSapRtIC',
    'c_4': 'BQADBAAD4QEAAl9XmQABT6nhOuolqKYC',
    'c_5': 'BQADBAAD4wEAAl9XmQABwRfmekGnpn0C',
    'c_6': 'BQADBAAD5QEAAl9XmQABQITgUsEsqxsC',
    'c_7': 'BQADBAAD5wEAAl9XmQABVhPF6EcfWjEC',
    'c_8': 'BQADBAAD6QEAAl9XmQABP6baig0pIvYC',
    'c_9': 'BQADBAAD6wEAAl9XmQAB0CQdsQs_pXIC',
    'c_10': 'BQADBAAD7QEAAl9XmQAB00Wii7R3gDUC',
    'c_J': 'BQADBAAD8QEAAl9XmQAB_RJHYKqlc-wC',
    'c_Q': 'BQADBAAD7wEAAl9XmQABo7D0B9NUPmYC',
    'c_K': 'BQADBAAD9wEAAl9XmQABb8CaxxsQ-Y8C',
    'option_info': 'BQADBAADxAIAAl9XmQABC5v3Z77VLfEC',
    'option_pass': 'BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg'
}
STICKERS_GRAY = {
    'd_A': 'BQADBAAD2QEAAl9XmQAB--inQsYcLTsC',
    'd_1': 'BQADBAAD2wEAAl9XmQABBzh4U-rFicEC',
    'd_2': 'BQADBAAD3QEAAl9XmQABo3l6TT0MzKwC',
    'd_3': 'BQADBAAD3wEAAl9XmQAB2y-3TSapRtIC',
    'd_4': 'BQADBAAD4QEAAl9XmQABT6nhOuolqKYC',
    'd_5': 'BQADBAAD4wEAAl9XmQABwRfmekGnpn0C',
    'd_6': 'BQADBAAD5QEAAl9XmQABQITgUsEsqxsC',
    'd_7': 'BQADBAAD5wEAAl9XmQABVhPF6EcfWjEC',
    'd_8': 'BQADBAAD6QEAAl9XmQABP6baig0pIvYC',
    'd_9': 'BQADBAAD6wEAAl9XmQAB0CQdsQs_pXIC',
    'd_10': 'BQADBAAD7QEAAl9XmQAB00Wii7R3gDUC',
    'd_J': 'BQADBAAD8QEAAl9XmQAB_RJHYKqlc-wC',
    'd_Q': 'BQADBAAD7wEAAl9XmQABo7D0B9NUPmYC',
    'd_K': 'BQADBAAD9wEAAl9XmQABb8CaxxsQ-Y8C',
    's_A': 'BQADBAAD2QEAAl9XmQAB--inQsYcLTsC',
    's_1': 'BQADBAAD2wEAAl9XmQABBzh4U-rFicEC',
    's_2': 'BQADBAAD3QEAAl9XmQABo3l6TT0MzKwC',
    's_3': 'BQADBAAD3wEAAl9XmQAB2y-3TSapRtIC',
    's_4': 'BQADBAAD4QEAAl9XmQABT6nhOuolqKYC',
    's_5': 'BQADBAAD4wEAAl9XmQABwRfmekGnpn0C',
    's_6': 'BQADBAAD5QEAAl9XmQABQITgUsEsqxsC',
    's_7': 'BQADBAAD5wEAAl9XmQABVhPF6EcfWjEC',
    's_8': 'BQADBAAD6QEAAl9XmQABP6baig0pIvYC',
    's_9': 'BQADBAAD6wEAAl9XmQAB0CQdsQs_pXIC',
    's_10': 'BQADBAAD7QEAAl9XmQAB00Wii7R3gDUC',
    's_J': 'BQADBAAD8QEAAl9XmQAB_RJHYKqlc-wC',
    's_Q': 'BQADBAAD7wEAAl9XmQABo7D0B9NUPmYC',
    's_K': 'BQADBAAD9wEAAl9XmQABb8CaxxsQ-Y8C',
    'h_A': 'BQADBAAD2QEAAl9XmQAB--inQsYcLTsC',
    'h_1': 'BQADBAAD2wEAAl9XmQABBzh4U-rFicEC',
    'h_2': 'BQADBAAD3QEAAl9XmQABo3l6TT0MzKwC',
    'h_3': 'BQADBAAD3wEAAl9XmQAB2y-3TSapRtIC',
    'h_4': 'BQADBAAD4QEAAl9XmQABT6nhOuolqKYC',
    'h_5': 'BQADBAAD4wEAAl9XmQABwRfmekGnpn0C',
    'h_6': 'BQADBAAD5QEAAl9XmQABQITgUsEsqxsC',
    'h_7': 'BQADBAAD5wEAAl9XmQABVhPF6EcfWjEC',
    'h_8': 'BQADBAAD6QEAAl9XmQABP6baig0pIvYC',
    'h_9': 'BQADBAAD6wEAAl9XmQAB0CQdsQs_pXIC',
    'h_10': 'BQADBAAD7QEAAl9XmQAB00Wii7R3gDUC',
    'h_J': 'BQADBAAD8QEAAl9XmQAB_RJHYKqlc-wC',
    'h_Q': 'BQADBAAD7wEAAl9XmQABo7D0B9NUPmYC',
    'h_K': 'BQADBAAD9wEAAl9XmQABb8CaxxsQ-Y8C',
    'c_A': 'BQADBAAD2QEAAl9XmQAB--inQsYcLTsC',
    'c_1': 'BQADBAAD2wEAAl9XmQABBzh4U-rFicEC',
    'c_2': 'BQADBAAD3QEAAl9XmQABo3l6TT0MzKwC',
    'c_3': 'BQADBAAD3wEAAl9XmQAB2y-3TSapRtIC',
    'c_4': 'BQADBAAD4QEAAl9XmQABT6nhOuolqKYC',
    'c_5': 'BQADBAAD4wEAAl9XmQABwRfmekGnpn0C',
    'c_6': 'BQADBAAD5QEAAl9XmQABQITgUsEsqxsC',
    'c_7': 'BQADBAAD5wEAAl9XmQABVhPF6EcfWjEC',
    'c_8': 'BQADBAAD6QEAAl9XmQABP6baig0pIvYC',
    'c_9': 'BQADBAAD6wEAAl9XmQAB0CQdsQs_pXIC',
    'c_10': 'BQADBAAD7QEAAl9XmQAB00Wii7R3gDUC',
    'c_J': 'BQADBAAD8QEAAl9XmQAB_RJHYKqlc-wC',
    'c_Q': 'BQADBAAD7wEAAl9XmQABo7D0B9NUPmYC',
    'c_K': 'BQADBAAD9wEAAl9XmQABb8CaxxsQ-Y8C',
}


class Card(object):
    """This class represents a card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '%s_%s' % (self.suit, self.value)

    def __repr__(self):
        return '%s%s' % (SUIT_ICONS[self.suit], self.value.capitalize())

    def __eq__(self, other):
        """Needed for sorting the cards"""
        return str(self) == str(other)

    def __lt__(self, other):
        """Needed for sorting the cards"""
        return str(self) < str(other)

    def compare_suit(self,other):
        """Needed for comparing suits"""
        #True if higher; False if lower
        if(self.suit == 'd'):
            return True
        if(self.suit == 's'):
            if(other.suit == 'd'):
                return False
        if(self.suit == 'h'):
            if(other.suit == 'd' or other.suit == 's'):
                return False
        if(self.suit == 'c'):
            return False
        return True

    def get_numval(self):
        if self.value not in tao:
            return self.value
        else:
            return tao[self.value]

def from_str(string):
    """Decodes a Card object from a string"""
    suit, value = string.split('_')
    return Card(suit, value)
