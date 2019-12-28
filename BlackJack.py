# BlackJack class
import Card
import Player
import Deal


class BlackJack(object):

    def __init__(game):
        game.deck     = deck
        game.players  = []
        game.pot      = 0;
        game.roundNum = 0;

    def addPlayer(game, number, name, money):
        game.players.append(Player.Player(number, name, money))

    def dealCards(game)
        for x in game.players:
            game.dealCard(x)
