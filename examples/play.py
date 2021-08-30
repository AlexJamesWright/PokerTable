from pokertable.playerfactory import PlayerFactory
from pokertable.game import Game 
from pokertable.enums import PlayerType

if __name__ == '__main__':

    playerfactory = PlayerFactory()
    userPlayer1 = playerfactory.newPlayer(PlayerType.USER)
    userPlayer2 = playerfactory.newPlayer(PlayerType.USER)

    game = Game([userPlayer1, userPlayer2])

    game.playAllHands(1)