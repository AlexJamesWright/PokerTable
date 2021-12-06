from pokertable.playerfactory import PlayerFactory
from pokertable.enums import PlayerType
from pokertable.round import Round
import unittest

class TestRoundPostBlindAnte(unittest.TestCase):
    
    def setUp(self) -> None:
        self.playerFactory = PlayerFactory()
    
    def test_smallBlindsFourPlayersNoAnteDealerZero(self):
        players = [
            self.playerFactory.newPlayer(stack=10),
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10)
            ]
        round = Round(players=players)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 0)
        self.assertEqual(round.pots.playerBets[1], 1)
        self.assertEqual(round.pots.playerBets[2], 2)
        self.assertEqual(round.pots.playerBets[3], 0)
        self.assertEqual(round.actionIndex, -1)
        self.assertEqual(round.dealerButtonIdx, 0)
        self.assertEqual(len(round.pots), 1)
        
    def test_smallBlindsFourPlayersAnteDealerZero(self):
        players = [
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10)
        ]
        round = Round(players=players, smallBlind=2, ante=1)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 1)
        self.assertEqual(round.pots.playerBets[1], 3)
        self.assertEqual(round.pots.playerBets[2], 5)
        self.assertEqual(round.pots.playerBets[3], 1)
        self.assertEqual(round.actionIndex, -1)
        self.assertEqual(round.dealerButtonIdx, 0)
        self.assertEqual(len(round.pots), 1)
        
    def test_smallBlindsTwoPlayersNoAnteDealerZero(self):
        players = [
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10)
        ]
        round = Round(players=players, smallBlind=2)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 2)
        self.assertEqual(round.pots.playerBets[1], 4)
        self.assertEqual(round.actionIndex, 0)
        self.assertEqual(round.dealerButtonIdx, 0)
        self.assertEqual(len(round.pots), 1)
        
    def test_smallBlindsTwoPlayersAnteDealerZero(self):
        players = [
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10)
            ]
        round = Round(players=players, smallBlind=2, ante=1)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 3)
        self.assertEqual(round.pots.playerBets[1], 5)
        self.assertEqual(round.actionIndex, 0)
        self.assertEqual(round.dealerButtonIdx, 0)
        self.assertEqual(len(round.pots), 1)
    
    def test_smallBlindsFourPlayersNoAnteDealerNonZero(self):
        players = [
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10)
            ]
        round = Round(players=players, dealerButtonIdx=2, smallBlind=2)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 4)
        self.assertEqual(round.pots.playerBets[1], 0)
        self.assertEqual(round.pots.playerBets[2], 0)
        self.assertEqual(round.pots.playerBets[3], 2)
        self.assertEqual(round.actionIndex, -3)
        self.assertEqual(round.dealerButtonIdx, 2)
        self.assertEqual(len(round.pots), 1)
        
    def test_smallBlindsFourPlayersAnteDealerNonZero(self):
        players = [
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10)
            ]
        round = Round(players=players, dealerButtonIdx=2, smallBlind=2, ante=1)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 5)
        self.assertEqual(round.pots.playerBets[1], 1)
        self.assertEqual(round.pots.playerBets[2], 1)
        self.assertEqual(round.pots.playerBets[3], 3)
        self.assertEqual(round.actionIndex, -3)
        self.assertEqual(round.dealerButtonIdx, 2)
        self.assertEqual(len(round.pots), 1)
        
    def test_smallBlindsTwoPlayersNoAnteDealerNonZero(self):
        players = [
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10)
            ]
        round = Round(players=players, dealerButtonIdx=1, smallBlind=2)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 4)
        self.assertEqual(round.pots.playerBets[1], 2)
        self.assertEqual(round.actionIndex, -1)
        self.assertEqual(round.dealerButtonIdx, 1)
        self.assertEqual(len(round.pots), 1)
        
    def test_smallBlindsTwoPlayersAnteDealerNonZero(self):
        players = [
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=10)
            ]
        round = Round(players=players, dealerButtonIdx=1, smallBlind=2, ante=1)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 5)
        self.assertEqual(round.pots.playerBets[1], 3)
        self.assertEqual(round.actionIndex, -1)
        self.assertEqual(round.dealerButtonIdx, 1)
        self.assertEqual(len(round.pots), 1)
        
    def test_smallBlindsFourPlayersShortStackedMultiplePots(self):
        players = [
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=100), 
            self.playerFactory.newPlayer(stack=1), 
            self.playerFactory.newPlayer(stack=10)
            ]
        round = Round(players=players, smallBlind=2)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 0)
        self.assertEqual(round.pots.playerBets[1], 2)
        self.assertEqual(round.pots.playerBets[2], 1)
        self.assertEqual(round.pots.playerBets[3], 0)
        self.assertEqual(round.actionIndex, -1)
        self.assertEqual(round.dealerButtonIdx, 0)
    
    
class TestRoundBettingRound(unittest.TestCase):
    
    def setUp(self) -> None:
        self.playerFactory = PlayerFactory()
    
    def test_preFlopBettingSimple(self):
        players = [
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBet(0),
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBet(5),
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBet(0),
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBet(5)
            ]

        round = Round(players=players)
        round.postPlayersBlindAnte()
        round.bettingRound(finalisePots=False)
        
        self.assertEqual(round.pots.nbettors, 3)
        round.pots.finalise()
        self.assertEqual(len(round.pots), 2)
        self.assertEqual(round.pots[0].size, 6)
        self.assertEqual(round.pots[1].size, 6)

class TestRoundFinishedBetting(unittest.TestCase):
    
    def setUp(self) -> None:
        self.playerFactory = PlayerFactory()

    def test_preflop(self):
        players = [
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBet(0),
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBet(5),
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBet(0),
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBet(5)
            ]

        round = Round(players=players)

        self.assertFalse(round._finishedBetting())
        round.postPlayersBlindAnte()
        self.assertFalse(round._finishedBetting())
        round.bettingRound()
        self.assertTrue(round._finishedBetting())

    def test_flop(self):
        players = [
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBets([0]),
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBets([5, 2, 5]),
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBets([0]),
            self.playerFactory.newPlayer(kind=PlayerType.SETTER, stack=10).setBets([5, 5])
            ]

        round = Round(players=players)

        round.postPlayersBlindAnte()
        round.bettingRound()
        round.bettingRound()

        self.assertTrue(round._finishedBetting())
        # Whilst we're here, might as well check the pots...
        self.assertEqual(round.pots.size, 22)



class TestRoundCheckValidAmount(unittest.TestCase):

    def setUp(self):
        self.playerFactory = PlayerFactory()

    def test_antes(self):
        players = [
            self.playerFactory.newPlayer(stack=10),
            self.playerFactory.newPlayer(stack=20), 
            self.playerFactory.newPlayer(stack=10), 
            self.playerFactory.newPlayer(stack=2)
            ]
        round = Round(players=players, smallBlind=2, ante=1)

        # Manually post antes and blinds
        self.assertTrue(round.checkValidAmount(1, players[0]))
        self.assertTrue(round.checkValidAmount(1, players[0]))
        self.assertTrue(round.checkValidAmount(1, players[0]))
        self.assertTrue(round.checkValidAmount(1, players[0]))
        self.assertTrue(round.checkValidAmount(1, players[0]))



if __name__ == '__main__':
    unittest.main()