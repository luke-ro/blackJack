class Card:

    def __init__(self, idNum):
        self.idNum = idNum
        self.faceDown = True;

        # returns the name of the card
    def getName(self):
        if self.idNum < 14 & self.idNum > 0:
            return string(self.idNum + " of Hearts")
        elif self.idnNum <27:
            return string(self.idNum + " of Diamond")
        elif self.idnNum <40:
            return string(self.idNum + " of Clubs")
        elif self.idnNum <53:
            return string(self.idNum + " of Spades")
        else:
            return string("Not a valid card")

        # returs the number of the card
    def getNum(self):
        return self.idNum

        # "flips" the card
    def flip(self):
        self.faceDown = self.faceDown != self.faceDown;

        # turns the card face up
    def flipUp(self):
        self.faceDown = 0

        # turns the card face down
    def flipDown(self):
        self.faceDown = 1
