from random import seed
from random import random
from time import clock

seed(clock)

class Player:

    def __init__(self, number, name, money):
        self.number = number
        self.name   = name
        self.money  = money
        self.hand   = []

    def takeCard(self, card):
        self.hand.append(card)

    def changeMoney(self,amount):
        self.money+=amount

    def showHand(self):
        for i in self.hand:
            print(i.getName() + " ")

    def showFaceUpCard(self):
        for i in self.hand:
            if i.getOrientation() == False:
                print(i.getName() + " ")

    def getHandValue(self):
        """ returns two values of the hand, one with Aces low
                and the second with Aces high
            - Aces = 11 or 1
            - Face cards = 11
            - Other cards have the value of their number
        """
        total = [0,0]
        for i in self.hand:
            if i.idNum % 13 == 1:
                total[0] += 1
                total[1] += 11
            elif i.idNum % 13 in [0,11,12]:
                total[0] += 10
                total[1] += 10
            else:
                total[0] += i.idNum % 13
                total[1] += i.idNum % 13

        return total

class Dealer(Player):

    def __init__(self, risk=None):
        self.hand   = []
        if risk is None:
            self.risk = gauss(0.5,0.3);
        else
            self.risk = risk

    def hitMe(self, pot, roundNum):
        handValue = self.getHandValue()

        if handValue[0] > 21 or handValue[1] > 21:
            return False
        elif handValue[0] == handValue[1]: # no Aces
            if handValue < 11:
                return True
            elif handValue < 13+2*risk+(2*(random()-.5)):
