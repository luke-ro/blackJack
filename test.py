import BlackJack

# for i in range(52):
#     c1 = Card.Card(i+1)
#     c1.flip()
#     c1.flipUp()
#     print(c1.getName()+" "+str(c1.getNum())+" "+str(c1.getOrientation()))
#     #print(c1.getNum())
game = BlackJack.BlackJack()
game.addPlayer(1,"Luke",1000)
# game.addPlayer(2,"Jake",1000)
# game.addPlayer(3,"Zach",1000)
while True:
    print("********************************NEW ROUND********************************")
    game.firstBets()
    game.dealCards()
    game.getDeckInfo()
    game.play()
    game.resetGame()
