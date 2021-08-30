from pokertable.playerfactory import PlayerFactory
from pokertable.players import Player
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
        round = Round(players=players, cards=None)
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
        round = Round(players=players, cards=None, smallBlind=2, ante=1)
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
        round = Round(players=players, cards=None, smallBlind=2)
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
        round = Round(players=players, cards=None, smallBlind=2, ante=1)
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
        round = Round(players=players, cards=None, dealerButtonIdx=2, smallBlind=2)
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
        round = Round(players=players, cards=None, dealerButtonIdx=2, smallBlind=2, ante=1)
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
        round = Round(players=players, cards=None, dealerButtonIdx=1, smallBlind=2)
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
        round = Round(players=players, cards=None, dealerButtonIdx=1, smallBlind=2, ante=1)
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
        round = Round(players=players, cards=None, smallBlind=2)
        round.postPlayersBlindAnte()
        self.assertEqual(round.pots.playerBets[0], 0)
        self.assertEqual(round.pots.playerBets[1], 2)
        self.assertEqual(round.pots.playerBets[2], 1)
        self.assertEqual(round.pots.playerBets[3], 0)
        self.assertEqual(round.actionIndex, -1)
        self.assertEqual(round.dealerButtonIdx, 0)
    
    
# class TestRoundFinishedBettering(unittest.TestCase):
    
#     def setUp(self) -> None:
#         self.playerFactory = PlayerFactory()
    
#     def test_preFlopBettingSimple(self):
#         players = [
#             self.playerFactory.newPlayer(stack=10),
#             self.playerFactory.newPlayer(stack=10), 
#             self.playerFactory.newPlayer(stack=10), 
#             self.playerFactory.newPlayer(stack=10)
#             ]
#         round = Round(players=players, cards=None)
#         round.postPlayersBlindAnte()
#         round.


if __name__ == '__main__':
    unittest.main()