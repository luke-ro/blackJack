class Card:

    def __init__(self, idNum):
        self.idNum = idNum
        self.faceDown = True;

        # returns the name of the card
    def getName(self):
        if self.idNum < 14 and self.idNum > 0:
            if self.idNum % 13 == 1:
                return "Ace of Hearts"
            elif self.idNum % 13 == 11:
                return "Jack of Hearts"
            elif self.idNum % 13 == 12:
                return "Queen of Hearts"
            elif self.idNum % 13 == 0:
                return "King of Hearts"
            else:
                return str(self.idNum) + " of Hearts"

        elif self.idNum <27:
            if self.idNum % 13 == 1:
                return "Ace of Diamonds"
            elif self.idNum % 13 == 11:
                return "Jack of Diamonds"
            elif self.idNum % 13 == 12:
                return "Queen of Diamonds"
            elif self.idNum % 13 == 0:
                return "King of Diamonds"
            else:
                return str(self.idNum % 13) + " of Diamonds"

        elif self.idNum <40:
            if self.idNum % 13 == 1:
                return "Ace of Clubs"
            elif self.idNum % 13 == 11:
                return "Jack of Clubs"
            elif self.idNum % 13 == 12:
                return "Queen of Clubs"
            elif self.idNum % 13 == 0:
                return "King of Clubs"
            else:
                return str(self.idNum % 13) + " of Clubs"

        elif self.idNum <53:
            if self.idNum % 13 == 1:
                return "Ace of Spades"
            elif self.idNum % 13 == 11:
                return "Jack of Spades"
            elif self.idNum % 13 == 12:
                return "Queen of Spades"
            elif self.idNum % 13 == 0:
                return "King of Spades"
            else:
                return str(self.idNum % 13) + " of Spades"
        else:
            return "Not a valid card"

        # returs the number of the card
    def getNum(self):
        return self.idNum

    def getOrientation(self):
        return self.faceDown

        # "flips" the card
    def flip(self):
        self.faceDown = self.faceDown != self.faceDown;

        # turns the card face up
    def flipUp(self):
        self.faceDown = False

        # turns the card face down
    def flipDown(self):
        self.faceDown = True
