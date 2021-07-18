from pokertable.utils import nextPlayerIndex
import unittest 

class TestNextPlayerIndex(unittest.TestCase):
    
    def test_correctIndex(self):
        nplayers = 6
        players = ['a', 'b', 'c', 'd', 'e', 'f']
        
        self.assertEqual(players[nextPlayerIndex(-6, nplayers)], 'b')
        self.assertEqual(players[nextPlayerIndex(-5, nplayers)], 'c')
        self.assertEqual(players[nextPlayerIndex(-4, nplayers)], 'd')
        self.assertEqual(players[nextPlayerIndex(-3, nplayers)], 'e')
        self.assertEqual(players[nextPlayerIndex(-2, nplayers)], 'f')
        self.assertEqual(players[nextPlayerIndex(-1, nplayers)], 'a')
        self.assertEqual(players[nextPlayerIndex(0, nplayers)], 'b')
        self.assertEqual(players[nextPlayerIndex(1, nplayers)], 'c')
        self.assertEqual(players[nextPlayerIndex(2, nplayers)], 'd')
        self.assertEqual(players[nextPlayerIndex(3, nplayers)], 'e')
        self.assertEqual(players[nextPlayerIndex(4, nplayers)], 'f')
        self.assertEqual(players[nextPlayerIndex(5, nplayers)], 'a')
        
if __name__=='__main__':
    unittest.main()