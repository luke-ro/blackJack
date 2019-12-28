

"""Black Jack 21

Deck Class

    Initialization Function
    Call Card 52 times and fill deckOrder in order 1-52

    Instance Variables
    deckOrder 1 - 52 list (1-13 Heart, 14-26 Diamond, 27-39 is clubs, 40-52 is spades, 1 is ace, 11 jack, 12 queen, 13 king)

    Functions
    shuffle(none) Randomly arrange all cards in deck
    deal(player instance variable, number of cards, faceup or facedown) Move the number of cards indicated to player faceup or down """


from Card import *
from random import seed
from random import random
from time import clock

# seed random number generator

seed(clock)

def rand(arg):
    pass
    return random()

class Deck(object):
    
    def __init__(self):
        self.myDeck=[None]*52

        for count, ele in enumerate(self.myDeck):
            self.myDeck[count] = Card(count)

        self.shuffle()

        #self.myDeck=[str(i) for i in range(52)]

    def shuffle(self):
        self.myDeck.sort(key=rand)

    def getDeck(self):
        self.cardNames=[i.getName() for i in dck.myDeck]  
        return(self.cardNames)

    def __removeCard(self):
        return self.myDeck.pop(0)

    def dealCard(self, player):
        player.takeCard(self.__removeCard())

# dck=Deck()
# print("\n"*4)
# print(dck.myDeck)
# print("\n"*4)
# dck.shuffle()
# print("\n"*4)
# dck.getDeck()
# print("\n"*4)
