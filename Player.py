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
                total[0] += 11
                total[1] += 11
            else:
                total[0] += i.idNum % 13
                total[1] += i.idNum % 13

        return total

# class NPCPlayer(Player):

    # def makeBet(self, pot, roundNum):
    #     handValue = self.getHandValue()
    #     if handValue[0] > 21 or handValue[1] > 21:
    #         return 0
    #     elif
