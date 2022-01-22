import logging
from config import ADMIN_LIST, OPEN_LOBBY
from datetime import datetime
from objects.combos import check_combo

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
    mode = None
    current_combo = []

    def __init__(self, chat):
        self.chat = chat
        self.last_card = c.Card('c','0')
        self.last_card_owner = None
        self.deck = Deck()
        self.logger = logging.getLogger(__name__)
        self.last_five_rank = None
        self.last_high = None

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
        self.open = False
        self.deck._fill__()
        self.started = True
        self.mode = None
        self.starter = None
        
    def check_last_high(self, cur_com):
        high = cur_com[0]
        for card in cur_com:
            if high < card:
                high = card
        return high

    def turn(self):
        """Marks the turn as over and change the current player"""
        self.logger.debug("Next Player")
        self.current_player = self.current_player.next
        self.current_player.turn_started = datetime.now()

    def rank_check(self, cur_combo):
        rank_c = {'1':[], '2':[], '3':[], '4':[], '5':{'0':[], '1':[], '2':[], '3':[], '4':[]}}
        for card in cur_combo:
            combos = check_combo(card=card, cards=cur_combo)
            for combo in combos.keys():
                if(combo != '5'):
                    rank_c[combo].append(combos[combo])
                else:
                    for k in combos[combo].keys():
                        for deal in combos[combo][k]:
                            rank_c[combo][k].append(deal)
        if(len(rank_c['2']) > 0 and len(rank_c['3']) > 0):
            for pair in rank_c['2']:    
                for trio in rank_c['3']:
                    if pair[0] not in trio:
                        rank_c['5']['2'].append(pair + trio)
        #four-of-a-kind plus singit
        if(len(rank_c['4']) > 0):
            for quads in rank_c['4']:
                if len(quads) > 0:
                    for singles in rank_c['1']:
                            if singles[0] not in quads:
                                rank_c['5']['3'].append(quads + singles)

        for rank in rank_c['5'].keys():
            for comboess in rank_c['5'][rank]:
                if sorted(cur_combo) == sorted(comboess):
                    return rank

    def play_card(self, card, player): #for single cards
        """
        Plays a card and triggers its effects.
        Should be called only from Player.play or on game start to play the
        first card
        """
        self.deck.dismiss(self.last_card)
        self.current_combo.append(card)

        self.last_card = card
        
        self.last_card_owner = player
        print("Last Card Owner: " + str(self.last_card_owner))
        self.logger.info("Playing card " + repr(card))
        print("Playing card " + repr(card))
        print("Last Card: " + str(self.last_card))

        player.countmode -= 1
        if len(player.to_remove) > 0:
            print(len(player.to_remove))
            if self.mode == '5':
                for removing in player.to_remove:
                    if(removing['Card'] in player.combos['5'][removing['MR']][removing['Index']]):
                        player.combos['5'][removing['MR']][removing['Index']].remove(removing['Card'])     
            else:
                for removing in player.to_remove:
                    if(removing['Card'] in player.combos[removing['MR']][removing['Index']]):
                        player.combos[removing['MR']][removing['Index']].remove(removing['Card'])
            player.to_remove = []
        print("Moves Left: " + str(player.countmode))
        if(player.countmode == 0):
            if self.mode == '5':
                self.last_five_rank = self.rank_check(self.current_combo)
                self.last_high = self.check_last_high(self.current_combo)
                print("Last Rank of Combo: " + str(self.last_five_rank))
                print("Highest card form Last Combo: " + str(self.last_high))
            self.current_combo.clear()
            player.countmode = int(self.mode)
            for player in self.players:
                for num in player.combos.keys():
                    if num != '5':
                        player.combos[num] = []
                    else:
                        for r in player.combos[num].keys():
                            player.combos[num][r] = []
                player.look_for_combos()
            self.turn()
    
    def set_mode(self, mode):
        self.mode = mode
        for player in self.players:
            player.countmode = int(mode)

