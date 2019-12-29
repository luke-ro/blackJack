# BlackJack class
import Card
import Player
import Deal


class BlackJack(object):

    def __init__(game):
        game.deck     = Deal.Deck()
        game.players  = []
        game.roundNum = 0;
        game.dealer   = Player.Dealer()

    def addPlayer(game, number, name, money):
        newPlayer = Player.Player(number, name, money);
        game.players.append(newPlayer)

    def firstBets(game):
        for x in game.players:
            bet = input("Enter Bet: ")
            x.makeBet(bet)

    def dealCards(game):
        for x in game.players:
            game.deck.dealCard(x)
        for x in game.players:
            game.deck.dealCard(x)

        game.deck.dealCard(game.dealer)
        game.deck.dealCard(game.dealer)

    def getPlayers(game):
        print(game.players.getNames())

    def getDeckInfo(game):
        print(game.deck.getDeck())
        print("-----------------")
        print("There are " + str(game.deck.getSize()) + " cards remaining in the deck")
        for x in game.players:
            x.showHand()
        game.dealer.showHand()
