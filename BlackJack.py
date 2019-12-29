# BlackJack class
import Card
import Player
import Deal


class BlackJack(object):

    def __init__(game):
        game.deck     = Deal.Deck()
        game.players  = []
        game.roundNum = 0;
        game.dealer   = Player.DealerBJ()
        game.netHouseMoney = 0

    def addPlayer(game, number, name, money):
        newPlayer = Player.PlayerBJ(number, name, money);
        game.players.append(newPlayer)

    def firstBets(game):
        for x in game.players:
            x.makeBet()

    def dealCards(game):
        for x in game.players:
            game.deck.dealCardFaceUp(x)

        for x in game.players:
            game.deck.dealCardFaceUp(x)

        game.deck.dealCard(game.dealer)
        game.deck.dealCardFaceUp(game.dealer)

    def getPlayers(game):
        print(game.players.getNames())

    def getDeckInfo(game):
        print(game.deck.getDeck())
        print("-----------------")
        print("There are " + str(game.deck.getSize()) + " cards remaining in the deck")
        for x in game.players:
            x.showHand()
        game.dealer.showHand()

    def play(game):
        for player in game.players:
            game.playTurn(player)
        game.dealerTurn()

        # Plays the turn for a sinlge player
    def playTurn(game, player):
        playing = True

        print(player.getName() + "'s Turn")
        player.showHand()
        print("-----------------")
        while playing:
            print("Enter the number of what you would like to do")
            choice = int(input("1. Hit\n2. Stand\n3. Double Down\n4. Split Hand\n5. Surrender\n"))
            if choice == 1:
                game.deck.dealCardFaceUp(player)
                player.showHand()
                if player.isBust():
                    print("You have bust and lost your wager. Bummer")
                    game.netHouseMoney += player.resetBet()
                    print("Ending turn...")
                    playing = False
                    break
                else:
                    while True:
                        print("Enter the number of what you would like to do")
                        choice = int(input("1. Hit\n2. Stand\n"))
                        if choice == 1:
                            game.deck.dealCardFaceUp(player)
                            player.showHand()
                            if player.isBust():
                                print("You have bust and lost your wager. Bummer")
                                game.netHouseMoney += player.resetBet()
                                print("Ending turn...")
                                playing = False
                                break
                        elif choice == 2:
                            print("Ending turn...")
                            playing = False
                            break


            elif choice == 2: # stand
                print("Ending turn")
                playing = False


            elif choice == 3: # double down
                if player.doubleBet():
                    game.deck.dealCardFaceUp(player)
                    player.showHand()
                    if player.isBust():
                        print("You have bust and lost your wager. Bummer")
                        game.netHouseMoney += player.resetBet()

                    print("Ending turn...")
                    playing = False
                else:
                    print("Cannot Double Down. Choose another option.")
            # Split
            elif choice == 4:
                if player.splitHand():
                    pass
                else:
                    print("Cannot Split. Choose another option.")
                #first hand
                print("-_-_-_-_-_-_-_- SPLIT HAND #1 -_-_-_-_-_-_-_-")
                game.deck.dealCardFaceUp(player)
                game.playTurn(player)
                player.switchHandsAndBets()
                print("-_-_-_-_-_-_-_- SPLIT HAND #2 -_-_-_-_-_-_-_-")
                game.deck.dealCardFaceUp(player)
                game.playTurn(player)
                print("-_-_-_-_-_-_-_- End of Split hands -_-_-_-_-_-_-_-")

                print("Ending turn...")
                playing = False
            # Surrender
            elif choice == 5:
                player.surrender()
                playing = False
            else:
                print("Invalid Entry. Try again")

    def dealerTurn(game):
        game.dealer.showHand()
        value = game.dealer.getHandValue()
        if value[0] == value[1]
            while value[0] < 17:
                game.deck.dealCardFaceUp(dealer)
                game.dealer.showHand()
                if game.dealer.isBust():
                    print("The dealer has bust")
                    game.dealer.bust = True
