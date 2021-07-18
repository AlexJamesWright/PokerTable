from pokertable.players import Player
from pokertable.round import Round
import unittest

class TestRoundPostBlindAnte(unittest.TestCase):
    
    def test_smallBlindsFourPlayersNoAnteDealerZero(self):
        players = [Player(10), Player(10), Player(10), Player(10)]
        round = Round(players, None)
        round.postPlayersBlindAnte()
        self.assertEqual(players[0].stack, 10)
        self.assertEqual(players[1].stack, 9)
        self.assertEqual(players[2].stack, 8)
        self.assertEqual(players[3].stack, 10)
        self.assertEqual(len(round.pots), 1)
        self.assertEqual(round.pots[0].size, 3)
        
    def test_smallBlindsFourPlayersAnteDealerZero(self):
        players = [Player(10), Player(10), Player(10), Player(10)]
        round = Round(players, None, smallBlind=2, ante=1)
        round.postPlayersBlindAnte()
        self.assertEqual(players[0].stack, 9)
        self.assertEqual(players[1].stack, 7)
        self.assertEqual(players[2].stack, 5)
        self.assertEqual(players[3].stack, 9)
        self.assertEqual(len(round.pots), 1)
        self.assertEqual(round.pots[0].size, 10)
        
    def test_smallBlindsTwoPlayersNoAnteDealerZero(self):
        players = [Player(10), Player(10)]
        round = Round(players, None, smallBlind=2)
        round.postPlayersBlindAnte()
        self.assertEqual(players[0].stack, 8)
        self.assertEqual(players[1].stack, 6)
        self.assertEqual(len(round.pots), 1)
        self.assertEqual(round.pots[0].size, 6)
        
    def test_smallBlindsTwoPlayersAnteDealerZero(self):
        players = [Player(10), Player(10)]
        round = Round(players, None, smallBlind=2, ante=1)
        round.postPlayersBlindAnte()
        self.assertEqual(players[0].stack, 7)
        self.assertEqual(players[1].stack, 5)
        self.assertEqual(len(round.pots), 1)
        self.assertEqual(round.pots[0].size, 8)
    
    def test_smallBlindsFourPlayersNoAnteDealerNonZero(self):
        players = [Player(10), Player(10), Player(10), Player(10)]
        round = Round(players, None, 2, smallBlind=2)
        round.postPlayersBlindAnte()
        self.assertEqual(players[0].stack, 6)
        self.assertEqual(players[1].stack, 10)
        self.assertEqual(players[2].stack, 10)
        self.assertEqual(players[3].stack, 8)
        self.assertEqual(len(round.pots), 1)
        self.assertEqual(round.pots[0].size, 6)
        
    def test_smallBlindsFourPlayersAnteDealerNonZero(self):
        players = [Player(10), Player(10), Player(10), Player(10)]
        round = Round(players, None, 2, smallBlind=2, ante=1)
        round.postPlayersBlindAnte()
        self.assertEqual(players[0].stack, 5)
        self.assertEqual(players[1].stack, 9)
        self.assertEqual(players[2].stack, 9)
        self.assertEqual(players[3].stack, 7)
        self.assertEqual(len(round.pots), 1)
        self.assertEqual(round.pots[0].size, 10)
        
    def test_smallBlindsTwoPlayersNoAnteDealerNonZero(self):
        players = [Player(10), Player(10)]
        round = Round(players, None, 1, smallBlind=2)
        round.postPlayersBlindAnte()
        self.assertEqual(players[0].stack, 6)
        self.assertEqual(players[1].stack, 8)
        self.assertEqual(len(round.pots), 1)
        self.assertEqual(round.pots[0].size, 8)
        
    def test_smallBlindsTwoPlayersAnteDealerNonZero(self):
        players = [Player(10), Player(10)]
        round = Round(players, None, 1, smallBlind=2, ante=1)
        round.postPlayersBlindAnte()
        self.assertEqual(players[0].stack, 5)
        self.assertEqual(players[1].stack, 7)
        self.assertEqual(len(round.pots), 1)
        self.assertEqual(round.pots[0].size, 8)
        
    def test_smallBlindsFourPlayersShortStackedMultiplePots(self):
        players = [Player(10), Player(100), Player(1), Player(10)]
        round = Round(players, None, smallBlind=2)
        round.postPlayersBlindAnte()
        self.assertEqual(players[0].stack, 98)
        self.assertEqual(players[0].stack, 0)
        self.assertEqual(players[0].stack, 10)
        self.assertEqual(players[0].stack, 10)
        self.assertEqual(len(round.pots), 2)
        self.assertEqual(round.pots[0].size, 2)
        self.assertEqual(round.pots[1].size, 1)
    
    
class TestRoundFinishedBettering(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()