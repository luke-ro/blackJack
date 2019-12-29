class Card:

    def __init__(self, idNum):
        self.idNum = idNum
        self.faceDown = True;

        # returns the name of the card
    def getName(self):
        """Returns the name of the card as a string"""
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

    def getNum(self):
        """returs the number of the card"""
        return self.idNum

    def getOrientation(self):
        """Returns True if the card is facedown"""
        return self.faceDown

    # def flip(self):
    #     """flips the card"""
    #     self.faceDown = self.faceDown != self.faceDown;

    def flipUp(self):
        """turns the card face up"""
        self.faceDown = False

    def flipDown(self):
        """turns the card face down"""
        self.faceDown = True
