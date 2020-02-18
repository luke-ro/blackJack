from random import seed
from random import random
from random import gauss
from time import clock

seed(clock)

class Player:

    instances = []

    def __init__(self, number, name, money):
        self.number = number
        self.name   = name
        self.money  = money
        self.hand   = []
        Player.bet  = 0
        Player.instances.append(self.name)

    def takeCard(self, card):
        self.hand.append(card)

    def returnCards(self, deck):
        for x in range(0,len(self.hand)):
            deck.takeCard(self.hand.pop(0))


    def changeMoney(self,amount):
        self.money+=amount

    def showHand(self):
        print("-----------------")
        print(self.name + " has ", end="", flush=True)
        for i in self.hand:
            print(i.getName() + " ", end="", flush=True)
        print()

    def showFaceUpCards(self):
        print("-----------------")
        print(self.name + " has ", end="", flush=True)
        for i in self.hand:
            if i.getOrientation() == False:
                print(i.getName() + " ")
        print()

    def getName(self):
        return self.name

    def getNames(self):
        return instances

    def makeBet(self):
        print(self.getName() + " has " + str(self.money))

        while True:
            amount = int(input(" Enter Bet: "))
            if amount > self.money:
                print("Not Enough Money. ")
            else:
                self.money -= amount
                self.bet   += amount
                break

    def resetBet(self):
        temp = self.bet
        self.bet = 0
        return temp



# Black Jack player
class PlayerBJ(Player):
    def __init__(self, number, name, money):
        self.acesHigh = None
        self.secondHand = []
        self.secondBet = 0
        self.isSplit = False
        super().__init__(number, name, money)

    def getHandValue(self):
        """ returns two values of the hand, one with Aces low
                and the second with Aces high
            - Aces = 11 or 1
            - Face cards = 10
            - Other cards have the value of their number
        """
        total = [0,0]
        for i in self.hand:
            if i.idNum % 13 == 1:
                total[0] += 11
                total[1] += 1
            elif i.idNum % 13 in [0,11,12]:
                total[0] += 10
                total[1] += 10
            else:
                total[0] += i.idNum % 13
                total[1] += i.idNum % 13

        return total

    def getSecondHandValue(self):
        """ returns two values of the hand, one with Aces low
                and the second with Aces high
            - Aces = 11 or 1
            - Face cards = 10
            - Other cards have the value of their number
        """
        total = [0,0]
        for i in self.secondHand:
            if i.idNum % 13 == 1:
                total[0] += 11
                total[1] += 1
            elif i.idNum % 13 in [0,11,12]:
                total[0] += 10
                total[1] += 10
            else:
                total[0] += i.idNum % 13
                total[1] += i.idNum % 13

        return total

    def isBust(self):
        value = self.getHandValue()
        if value[0] > 21 and value[1] > 21:
            return True
        else:
            return False

    def showHand(self):
        value = self.getHandValue()
        if value[0] == value[1]:
            print("-----------------")
            print(self.name + " has ", end="", flush=True)
            for i in self.hand:
                print(i.getName(), end=" ", flush=True)
            print("With a value of " + str(value[0]))
        else:
            print("-----------------")
            print(self.name + " has ", end="", flush=True)
            for i in self.hand:
                print(i.getName(), end=" ", flush=True)
            print("\nWith a value of " + str(value[0]) + " with Aces high or ")
            print("With a value of " + str(value[1]) + " with Aces low")

    # Returns True if the player can double down and doubles down.
    # Returns False if not enough $$$
    def doubleBet(self):
        print(str(self.bet) + " " + str(self.money))
        if self.bet < self.money:
            self.money -= self.bet
            self.bet   += self.bet
            return True
        else:
            return False

    def splitHand(self):
        if self.bet < self.money and not self.isSplit:
            self.secondHand.append(self.hand.pop(1))
            self.money -= self.bet
            self.secondBet  = self.bet
            self.isSplit = True
            return True
        else:
            return False

    def returnCards(self, deck):
        for x in range(0,len(self.hand)):
            deck.takeCard(self.hand.pop(0))
        for x in range(0,len(self.secondHand)):
            deck.takeCard(self.secondHand.pop(0))

    def switchHandsAndBets(self):
        temp = self.hand
        self.hand = self.secondHand
        self.secondHand = temp

        temp2 = self.bet
        self.bet = self.secondBet
        self.secondBet = temp2

    def showHandsAndBets(self):
        print("The split hands and bets are as follows:")
        print("First Hand: $" + str(self.bet))
        value = self.getHandValue()
        if value[0] == value[1]:
            print("-----------------")
            print(self.name + " has ", end="", flush=True)
            for i in self.hand:
                print(i.getName(), end=" ", flush=True)
            print("With a value of " + str(value[0]))
        else:
            print("-----------------")
            print(self.name + " has ", end="", flush=True)
            for i in self.hand:
                print(i.getName(), end=" ", flush=True)
            print("\nWith a value of " + str(value[0]) + " with Aces high or ")
            print("With a value of " + str(value[1]) + " with Aces low")

        print("Second Hand: $" + str(self.secondBet))
        value = self.getSecondHandValue()
        if value[0] == value[1]:
            print("-----------------")
            print(self.name + " has ", end="", flush=True)
            for i in self.secondHand:
                print(i.getName(), end=" ", flush=True)
            print("With a value of " + str(value[0]))
        else:
            print("-----------------")
            print(self.name + " has ", end="", flush=True)
            for i in self.secondHand:
                print(i.getName(), end=" ", flush=True)
            print("\nWith a value of " + str(value[0]) + " with Aces high or ")
            print("With a value of " + str(value[1]) + " with Aces low")


    def surrender(self):
        self.money += self.bet/2


    def wash(self):
        self.money += self.bet


    def twoToOne(self):
        self.money += self.bet*2


    def newRound(self):
        self.isSplit = False
        self.resetBet()

class DealerBJ(PlayerBJ):

    def __init__(self):
        self.hand   = []
        self.bust = False
        self.name = "Dealer"

    def returnCards(self, deck):
        for x in range(0,len(self.hand)):
            deck.takeCard(self.hand.pop(0))
