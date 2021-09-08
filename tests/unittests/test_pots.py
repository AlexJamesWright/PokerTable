from pokertable.players import Player
from pokertable.pots import Pots
import unittest 

class TestPots(unittest.TestCase):
    
    def setUp(self):
        self.players = [Player(10, 0), Player(30, 1), Player(70, 2), Player(1000, 3)]
    
    def tearDown(self):
        for p in self.players:
            del p
    
    def test_potsBetSize(self):
        pots = Pots(self.players)
        for player in self.players:
            pots.betSize(1, player)
        pots.finalise()
        self.assertEqual(len(pots), 1)
        self.assertEqual(pots[0].size, 4)
        
    def test_p2RaisesP1allIn(self):
        self.players = [Player(10, 0), Player(30, 1)]
        pots = Pots(self.players)
        
        # P1 bets 5
        pots.betSize(5, self.players[0])
        
        # P2 raises P1 all in, bets 10
        pots.betSize(10, self.players[1])
        
        # P1 calls all in, bets 10
        pots.betSize(10, self.players[0])
        pots.finalise()
        self.assertEqual(len(pots), 1)
        self.assertEqual(pots[0].size, 20)
        self.assertEqual(self.players[0].stack, 0)
        self.assertEqual(self.players[1].stack, 20)
        

    def test_firstPlayerAllIn(self):
        # Need to check that pots makes sense when players dont have enough
        pots = Pots(self.players)
        
        for player in self.players:
            pots.betSize(10, player)
            
        for player in self.players:
            pots.betSize(20, player)
            
        pots.finalise()
            
        self.assertEqual(len(pots), 2)
        self.assertEqual(pots[0].size, 40)
        self.assertEqual(pots[1].size, 30)
        self.assertEqual(list(pots[0].playersDict.keys()), [0, 1, 2, 3])
        self.assertEqual(list(pots[1].playersDict.keys()), [1, 2, 3])
        self.assertEqual(self.players[0].stack, 0)
        self.assertEqual(self.players[1].stack, 10)
        self.assertEqual(self.players[2].stack, 50)
        self.assertEqual(self.players[3].stack, 980)
            
    def test_secondPlayerAllIn(self):
        pots = Pots(self.players)
        
        pots.betSize(5, self.players[0])
        for player in self.players[-3:]:
            pots.betSize(30, player)
        pots.betSize(999999, self.players[0])
        
        pots.finalise()
            
        self.assertEqual(len(pots), 2)
        self.assertEqual(pots[0].size, 40)
        self.assertEqual(pots[1].size, 60)
        self.assertEqual(self.players[0].stack, 0)
        self.assertEqual(self.players[1].stack, 0)
        self.assertEqual(self.players[2].stack, 40)
        self.assertEqual(self.players[3].stack, 970)
        self.assertEqual(list(pots[0].playersDict.keys()), [0, 1, 2, 3])
        self.assertEqual(list(pots[1].playersDict.keys()), [1, 2, 3])
    
    def test_sharkAllIn(self):
        pots = Pots(self.players)
        
        pots.betSize(5, self.players[0])
        pots.betSize(15, self.players[1])
        pots.betSize(50, self.players[2])
        pots.betSize(1000, self.players[3])
        pots.betSize(1000, self.players[0])
        pots.betSize(1000, self.players[1])
        pots.betSize(1000, self.players[2])
        
        pots.finalise()
            
        self.assertEqual(len(pots), 3)
        self.assertEqual(pots[0].size, 40)
        self.assertEqual(pots[1].size, 60)
        self.assertEqual(pots[2].size, 80)
        self.assertEqual(self.players[0].stack, 0)
        self.assertEqual(self.players[1].stack, 0)
        self.assertEqual(self.players[2].stack, 0)
        self.assertEqual(self.players[3].stack, 930)
        self.assertEqual(list(pots[0].playersDict.keys()), [0, 1, 2, 3])
        self.assertEqual(list(pots[1].playersDict.keys()), [1, 2, 3])
        self.assertEqual(list(pots[2].playersDict.keys()), [2, 3])
        
        

if __name__ == '__main__':
    unittest.main()