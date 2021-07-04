from pokertable.players import Player
from pokertable.pots import Pots
import unittest 

class TestPots(unittest.TestCase):
    
    def setUp(self):
        self.players = [Player(10, 0), Player(30, 1), Player(70, 2), Player(1000, 3)]
    
    def tearDown(self):
        for p in self.players:
            del p
    
    def test_simpleCase(self):
        pots = Pots()
        for player in self.players:
            pots.addAmount(1, player)
        
        self.assertEqual(len(pots), 1)
        self.assertEqual(pots[0].size, 4)
       
       
        
    def test_blah(self):
        # Need to check that pots makes sense when players dont have enough
        pass 
    
if __name__ == '__main__':
    unittest.main()