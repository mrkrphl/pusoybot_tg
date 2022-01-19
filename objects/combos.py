def check_doubles(player):
    for card1 in player.cards:
        for card2 in player.cards:
            if card2 == card1:
                continue
            if card1.value == card2.value:
                return True
    return False

def check_trio(player):
    for card1 in player.cards:
        for card2 in player.cards:
            if card2 == card1:
                continue
            for card3 in player.cards:
                if card3 == card2:
                    continue
                if card1.value == card2.value == card3.value:
                    return True
    return False

def check_quad(player):
    for card1 in player.cards:
        for card2 in player.cards:
            if card2 == card1:
                continue
            for card3 in player.cards:
                if card3 == card2:
                    continue
                for card4 in player.cards:
                    if card4 == card3:
                        continue
                    if card1.value == card2.value == card3.value:
                        return True
    return False

def check_fives(player):
    #straight
    for card1 in player.cards:
        for card2 in player.cards:
            if int(card2.get_numval()) - int(card1.get_numval()) == 1:
                for card3 in player.cards:
                    if int(card3.get_numval()) - int(card2.get_numval()) == 1:
                        for card4 in player.cards:
                            if int(card4.get_numval()) - int(card3.get_numval()) == 1:
                                for card5 in player.cards:
                                    if int(card5.get_numval()) - int(card4.get_numval()) == 1:
                                        return True
    #full house
    if(check_doubles(player) and check_trio(player)):
        return True
    #flush
    count = {'d':0, 's':0, 'h':0, 'c':0}
    for card in player.cards:
        for suit in count.keys:
            if suit in str(card):
                count[suit] += 1
    for num in count.values:
        if num == 5: 
            return True
    
    return False
