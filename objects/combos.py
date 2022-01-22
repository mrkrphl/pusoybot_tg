def check_combo(card, cards): #function to get all possible combos listed in a dictionary of lists 
    combos = {'1':[card], '4': [], '5':{'0':[], '1':[], '2':[], '3':[], '4':[]}}
    fours = []
    sorted_cards = sorted(cards)
    #up to three-of-a-kind
    index = sorted_cards.index(card)
    num = len(sorted_cards)
    for i in range(1,4):
        if i != 3:
            if index+i >= num:
                break
            if sorted_cards[index+i].value == card.value:
                combos[str(i+1)] = [card for card in combos[str(i)]]
                combos[str(i+1)].append(sorted_cards[index+i])
        else: #quads
            if index+i >= num:
                break
            if sorted_cards[index+i].value == card.value:
                fours = [card for card in combos['3']]
                fours.append(sorted_cards[index+i])
            combos['4'] =  fours

    #Straight and straight flush
    for i in range(index+1, num):
        for j in range(i+1, num):
                for k in range(j+1, num):
                        for l in range(k+1, num):
                                if (sorted_cards[i].get_numval() - sorted_cards[index].get_numval() == 1 and #1,2 
                                    sorted_cards[j].get_numval() - sorted_cards[i].get_numval() == 1 and # 2,3
                                    sorted_cards[k].get_numval() - sorted_cards[j].get_numval() == 1 and #3,4
                                    sorted_cards[l].get_numval() - sorted_cards[k].get_numval() == 1): #4,5
                                    combo = [sorted_cards[index],sorted_cards[i],sorted_cards[j],sorted_cards[k],sorted_cards[l]]
                                    if (combo[0].suit == combo[1].suit and
                                        combo[0].suit == combo[2].suit and
                                        combo[0].suit == combo[3].suit and
                                        combo[0].suit == combo[4].suit):
                                        combos['5']['4'].append(combo)
                                    else:
                                        combos['5']['0'].append(combo)
                                elif(sorted_cards[i].suit == sorted_cards[j].suit == sorted_cards[k].suit == sorted_cards[l].suit == sorted_cards[index].suit):
                                    flush = []
                                    flush.append(sorted_cards[index]) #FLUSH
                                    flush.append(sorted_cards[i])
                                    flush.append(sorted_cards[j])
                                    flush.append(sorted_cards[k])
                                    flush.append(sorted_cards[l])
                                    combos['5']['1'].append(flush)
    return combos
