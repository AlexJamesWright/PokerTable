from pokertable.playerfactory import PlayerFactory
from pokertable.enums import PlayerType
from pokertable.round import Round
from pokertable.cards import Cards
from pokertable.game import Game
import unittest 

class TestGame(unittest.TestCase):
    
    def setUp(self):

        # Game goes as, 
        # Preflop:
        #   p3 raise to 4
        #   p4 call
        #   p0, p1, p2 fold
        # Flop:
        #   p3 check 
        #   p4 bet 3 
        #   p3 call
        # Turn:
        #   p3 bet 3 
        #   p4 fold

        playerfactory = PlayerFactory()
        self.playerList = [playerfactory.newPlayer(PlayerType.SETTER).setBets([0]),
                           playerfactory.newPlayer(PlayerType.SETTER).setBets([0]),
                           playerfactory.newPlayer(PlayerType.SETTER).setBets([0]),
                           playerfactory.newPlayer(PlayerType.SETTER).setBets([4, 0, 3, 3]),
                           playerfactory.newPlayer(PlayerType.SETTER).setBets([4, 3, 0])]

        self.game = Game(self.playerList)
        self.game.roundCards = Cards.setUpDecks(1, len(self.playerList))[0] # Yuck

    def test_preflop(self):

        round = Round(self.playerList, 0)
        self.game._preflopBetting(round)

        self.assertEqual(round.pots.size, 11)
        self.assertEqual(len(round.pots), 3)

        self.assertEqual(round.pots[0].size, 4)
        self.assertEqual(list(round.pots[0].playersDict.keys()), [1, 2, 3, 4])
        self.assertEqual(round.pots[1].size, 3)
        self.assertEqual(list(round.pots[1].playersDict.keys()), [2, 3, 4])
        self.assertEqual(round.pots[2].size, 4)
        self.assertEqual(list(round.pots[2].playersDict.keys()), [3, 4])

        self.assertEqual(round.players[0].stack, 10)
        self.assertEqual(round.players[1].stack, 9)
        self.assertEqual(round.players[2].stack, 8)
        self.assertEqual(round.players[3].stack, 6)
        self.assertEqual(round.players[4].stack, 6)
        

    def test_flop(self):

        round = Round(self.playerList, 0)
        self.game._preflopBetting(round)
        self.game._flopBetting(round)

        self.assertEqual(round.pots.size, 17)
        self.assertEqual(len(round.pots), 3)

        self.assertEqual(round.pots[0].size, 4)
        self.assertEqual(list(round.pots[0].playersDict.keys()), [1, 2, 3, 4])
        self.assertEqual(round.pots[1].size, 3)
        self.assertEqual(list(round.pots[1].playersDict.keys()), [2, 3, 4])
        self.assertEqual(round.pots[2].size, 10)
        self.assertEqual(list(round.pots[2].playersDict.keys()), [3, 4])

        self.assertEqual(round.players[0].stack, 10)
        self.assertEqual(round.players[1].stack, 9)
        self.assertEqual(round.players[2].stack, 8)
        self.assertEqual(round.players[3].stack, 3)
        self.assertEqual(round.players[4].stack, 3)

    def test_turn(self):

        round = Round(self.playerList, 0)
        self.game._preflopBetting(round)
        self.game._flopBetting(round)
        self.game._turnBetting(round)

        self.assertEqual(round.pots.size, 20)
        self.assertEqual(len(round.pots), 3)

        self.assertEqual(round.pots[0].size, 4)
        self.assertEqual(list(round.pots[0].playersDict.keys()), [1, 2, 3, 4])
        self.assertEqual(round.pots[1].size, 3)
        self.assertEqual(list(round.pots[1].playersDict.keys()), [2, 3, 4])
        self.assertEqual(round.pots[2].size, 13)
        self.assertEqual(list(round.pots[2].playersDict.keys()), [3, 4])

        self.assertEqual(round.players[0].stack, 10)
        self.assertEqual(round.players[1].stack, 9)
        self.assertEqual(round.players[2].stack, 8)
        self.assertEqual(round.players[3].stack, 0)
        self.assertEqual(round.players[4].stack, 3)



if __name__ == '__main__':

    unittest.main()