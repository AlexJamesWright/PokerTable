import numpy as np
    
class Cards:
    
    deck = [str(c) + s for s in ['s', 'c', 'h', 'd'] for c in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']]
    
    @staticmethod
    def setUpDecks(nrounds, nplayers):
        # allDecks = np.tile(np.arange(52), (nrounds, 1))
        allDecks = np.tile(Cards.deck, (nrounds, 1))
        [np.random.shuffle(allDecks[i]) for i in range(nrounds)]
        return allDecks[:, :(2*nplayers+5)]
    
class Hole:
    
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2 
        self.stake = 0
        self.folded = False
        self.allIn = False