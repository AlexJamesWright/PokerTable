from pokertable.enums import Action
from pokertable.pots import Pots


class Round:
    """
    Container for all things related to a single round. Contains the players, cards,
    pots, and utility methods.
    """
    def __init__(self, players, cards, dealerButtonIdx=0, smallBlind=1, bigBlind=None, ante=0):
        self.players = players 
        self.nplayers = len(players)
        self.cards = cards 
        self.dealerButtonIdx = dealerButtonIdx
        self.smallBlind = smallBlind 
        self.bigBlind = bigBlind or 2*smallBlind
        self.ante = ante
        self.pots = Pots()
        self.flop = None
        self.turn = None 
        self.river = None
        self.currentPlayerIndex = dealerButtonIdx+1
        
    def newRound(self):
        # TODO Might be more efficient to reset some variables, rather than 
        # create a new instance of Round in Game.playAllHands for every round
        pass 
    
    
    def finishedBetting(self):
        pass
    
        
    def postPlayersBlindAnte(self):
        self._postAntes()
        self._postSmallBlind()
        self._postBigBlind()
        
    def _postSmallBlind(self):
        self.players[self.currentPlayerIndex].stack -= self.smallBlind
        
    
    def _postBigBlind(self):
        pass 
    
    def _postAntes(self):
        for player in self.players:
            self.pots.addAmount(self.ante, player)
            
    def bettingRound(self):
        pass