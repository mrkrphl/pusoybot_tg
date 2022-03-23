import logging
from datetime import datetime
from statistics import mode

from errors import DeckEmptyError
from gamethings.game import SINGLE
from objects.card import Card
from objects.combos import check_combo, check_trio


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
        self.countmode = None
        self.combos = {'1':[], '2':[], '3':[], '4':[], '5':{'0':[], '1':[], '2':[], '3':[], '4':[]}}
        self.to_remove = []

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
        self.game.play_card(card, self)

    def first_player(self):
        if self.game.last_card.value != '0':
            return False
        return True

    def sort_cards(self):
        self.cards = sorted(self.cards)

    def look_for_combos(self):
        sorted_cards = sorted(self.cards)
        for card in sorted_cards:
            combos = check_combo(card=card, cards=sorted_cards)
            for combo in combos.keys():
                if(combo != '5'):
                    for bination in combos[combo]:
                        if bination not in self.combos[combo]:
                            self.combos[combo].append(bination)
                else:
                    for k in combos[combo].keys():
                        for deal in combos[combo][k]:
                            self.combos[combo][k].append(deal)
        if(len(self.combos['2']) > 0 and len(self.combos['3']) > 0):
            for pair in self.combos['2']:    
                for trio in self.combos['3']:
                    if len(pair) > 0 and len(trio) > 0:
                        if pair[0] not in trio and pair[1] not in trio:
                            self.combos['5']['2'].append(pair + trio)
        
        #four-of-a-kind plus singit
        if(len(self.combos['4']) > 0):
            for quads in self.combos['4']:
                if len(quads) > 0:
                    for singles in self.combos['1']:
                        if singles[0] not in quads:
                            self.combos['5']['3'].append(quads + singles)
        print(self.combos)
        

    def playable_cards(self):
        """Returns a list of the cards this player can play right now"""
        playable = list()
        combos = {'1':[], '2':[], '3':[], '5':[]}
        if self.game.mode == None:    
            if self.first_player():
                lowest = Card('c','3')
                if(lowest in self.cards):
                    playable.append(lowest)
                    for num in self.combos.keys():
                        if num == '4':
                            continue
                        if num != '5':
                            for comboes in self.combos[num]:
                                if lowest in comboes:
                                    combos[num].append(comboes)
                                    for card in comboes:
                                        if card not in playable:
                                            playable.append(card)
                        else:
                            for rank in self.combos[num]:
                                for comboes in self.combos[num][rank]:
                                    if lowest in comboes:
                                        combos[num].append(comboes)
                                        for card in comboes:
                                            if card not in playable:
                                                playable.append(card)
                    return playable, combos
        else:
            if self.first_player():
                lowest = Card('c','3')
                if(lowest in self.cards):
                    playable.append(lowest)
                    for num in self.combos.keys():
                        if self.game.mode != num:
                            continue
                        if num != '5':
                            for comboes in self.combos[num]:
                                if lowest in comboes:
                                    combos[num].append(comboes)
                                    for card in comboes:
                                        if card not in playable:
                                            playable.append(card)
                        else:
                            for rank in self.combos[num]:
                                for comboes in self.combos[num][rank]:
                                    if lowest in comboes:
                                        combos[num].append(comboes)
                                        for card in comboes:
                                            if card not in playable:
                                                playable.append(card)
                    return playable, combos

        if not self.game.mode:
            for card in self.cards:
                playable.append(card)
            return playable, self.combos

        last = self.game.last_card
        mode = self.game.mode
        if(self.countmode != 0 and self.countmode < int(self.game.mode)): #magbababa pa
            last = self.game.last_card
            if mode != '5':
                for combo in self.combos[str(mode)]:
                    if last in combo and len(combo) == self.countmode+1:
                        to_remove_list = {'MR':mode, 'Index':self.combos[mode].index(combo), 'Card': last}
                        combos[str(mode)].append([card for card in combo if card != last])
                        self.to_remove.append(to_remove_list)
                    
                for combo in combos[str(mode)]:
                    for card in combo:
                        if card not in playable:
                            playable.append(card)
                return playable, combos
            else:

                for rank in self.combos['5'].keys():
                    print(self.combos['5'][rank])
                    print("done")
                    for combo in self.combos['5'][rank]:
                        if last in combo and len(combo) == self.countmode+1:
                            print("Possible combos from dropped card: " + str(combo)) 
                            if self.game.last_five_rank == None or int(self.game.last_five_rank) < int(rank):  
                                print("No rank or less rank!")
                                to_remove_list = {'MR':rank, 'Index':self.combos['5'][rank].index(combo), 'Card': last}
                                combos[str(mode)].append([card for card in combo if card != last])
                                self.to_remove.append(to_remove_list)
                            elif rank == self.game.last_five_rank:
                                print("Equal Rank")
                                high = self.game.last_high
                                if len(combo) > 2:
                                    print("HERE")
                                    card = self.game.check_last_high(combo, rank)
                                    print(card)
                                    if high < card:
                                        to_remove_list = {'MR':rank, 'Index':self.combos['5'][rank].index(combo), 'Card': last}
                                        combos[str(mode)].append([card for card in combo if card != last])
                                        self.to_remove.append(to_remove_list)
                                    else:
                                        print("MEH")
                                else:
                                    card = combo[0]
                                    print(card)
                                    to_remove_list = {'MR':rank, 'Index':self.combos['5'][rank].index(combo), 'Card': last}
                                    combos[str(mode)].append([card for card in combo if card != last])
                                    self.to_remove.append(to_remove_list)                  
                for combo in combos[str(mode)]:
                    for card in combo:
                        if card not in playable:
                            playable.append(card)
                return playable, combos


        #eto ibang player na sasagot
        print("NEXT PLAYER START A COMBO")
        if mode != '5':
            for combo in self.combos[str(mode)]: 
                for card in combo:
                    if last < card:
                        combos[str(mode)].append(combo)
                        continue
            for combo in combos[str(mode)]:
                for card in combo:
                    if card not in playable:
                        playable.append(card)
        else:
            for rank in self.combos[str(mode)].keys():
                if self.game.last_five_rank != None:
                    print("Previous combo's rank was " + self.game.last_five_rank)
                    if int(rank) == int(self.game.last_five_rank):
                        for combis in self.combos['5'][rank]:
                                if self.game.last_high < self.game.check_last_high(combis, rank):
                                    combos[str(mode)].append(combis)
                                    continue
                    elif int(rank) > int(self.game.last_five_rank): 
                        for combo in self.combos['5'][rank]:
                                combos[str(mode)].append(combo)
                else:
                    print("You just started a new mode!")
                    for combo in self.combos['5'][rank]:
                        for card in combo:
                            combos[str(mode)].append(combo)
                            break
            for combo in combos[str(mode)]:
                for card in combo:
                    if card not in playable:
                        playable.append(card)
        return playable, combos