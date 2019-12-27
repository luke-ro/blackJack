import Card

class Player:


    def __init__(self, number, money):
        self.number = number
        self.money = money
        self.hand = []

    def takeCard(self, card):
        self.hand.append(card)

    def changeMoney(self,amount):
        self.money+=amount
