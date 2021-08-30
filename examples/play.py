from pokertable.playerfactory import PlayerFactory
from pokertable.game import Game 
from pokertable.enums import PlayerType

if __name__ == '__main__':

    playerfactory = PlayerFactory()
    userPlayer1 = playerfactory.newPlayer(PlayerType.USER)
    userPlayer2 = playerfactory.newPlayer(PlayerType.USER)
    userPlayer3 = playerfactory.newPlayer(PlayerType.USER)
    userPlayer4 = playerfactory.newPlayer(PlayerType.USER)
    userPlayer5 = playerfactory.newPlayer(PlayerType.USER)

    game = Game([userPlayer1, userPlayer2, userPlayer3, userPlayer4, userPlayer5])

    game.playAllHands(1)