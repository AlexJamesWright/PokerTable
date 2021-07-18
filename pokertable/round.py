from pokertable.errors import InvalidBetAmount
from pokertable.utils import nextPlayerIndex
from pokertable.players import Player
from pokertable.enums import Action
from pokertable.pots import Pots

class Round:
    """
    Container for all things related to a single round. Contains the players, cards,
    pots, and utility methods. This class handles betting.
    """
    def __init__(self, players, cards, dealerButtonIdx=0, smallBlind=1, bigBlind=None, ante=0):
        self.players: list[Player] = players
        self.nplayers = len(self.players)
        self.dealerButtonIdx = dealerButtonIdx
        self.smallBlind = smallBlind 
        self.bigBlind = bigBlind or 2*smallBlind
        self.maxBet = self.bigBlind
        self.ante = ante
        self.actionIndex = nextPlayerIndex(self.dealerButtonIdx, self.nplayers)
        dealerButtonIdx+1
        self.pots = Pots()
        
    def newRound(self):
        # TODO Might be more efficient to reset some variables, rather than 
        # create a new instance of Round in Game.playAllHands for every round
        # Would need to:
        #   - drop bust players here
        #   - reset largest bet size
        pass 
    
    
    def finishedBetting(self):
        pass
    
        
    def postPlayersBlindAnte(self):
        self._postAntes()
        self._postSmallBlind()
        self._postBigBlind()
        
    def _postSmallBlind(self):
        self.pots.betSize(self.bigBlind, self.players[self.actionIndex])
        self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers)
    
    def _postBigBlind(self):
        self.pots.betSize(self.bigBlind, self.players[self.actionIndex])
        self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers)
    
    def _postAntes(self):
        for player in self.players:
            self.pots.betSize(self.ante, player)
            
    def bettingRound(self):
        while self.pots.stillBetting():
            self.getPlayerBet(self)
            self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers)
        # End of betting round, reset maxBet for next betting round
        self.maxBet = self.bigBlind
        
    def getPlayerBet(self, player):
        valid = False 
        while not valid:
            amount = self.players[self.actionIndex].getBet()
            valid = self.checkValidAmount(amount)
        self.pots.betSize(amount, self.players[[self.actionIndex]])
            
    def checkValidAmount(self, amount):
        if (amount==self.maxBet) or (amount >= 2*self.maxBet):
            # if call/check or raise
            self.maxBet = amount
            return True
        return False