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
        self._nplayers = len(self.players)
        self.dealerButtonIdx = dealerButtonIdx
        self.smallBlind = smallBlind 
        self.bigBlind = bigBlind or 2*smallBlind
        self.maxBet = self.bigBlind
        self.ante = ante
        self.actionIndex = None
        dealerButtonIdx+1
        self.pots = Pots()
        
    @property 
    def nplayers(self):
        return len(self.players)
        
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
        # Starting new round
        self._startNewRound()
        self._postAntes()
        self._postSmallBlind()
        self._postBigBlind()
        
    def _postSmallBlind(self):
        self.pots.betSize(self.smallBlind+self.ante, self.players[self.actionIndex])
        self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers)
    
    def _postBigBlind(self):
        self.pots.betSize(self.bigBlind+self.ante, self.players[self.actionIndex])
        self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers)
    
    def _postAntes(self):
        for player in self.players:
            self.pots.betSize(self.ante, player)
            
    def _startNewRound(self):
        # For a new round, we need to set the action index 
        if self.nplayers > 2:
            self.actionIndex = nextPlayerIndex(self.dealerButtonIdx, self.nplayers)
        elif self.nplayers == 2:
            self.actionIndex = self.dealerButtonIdx
        else:
            raise RuntimeError(f'Not enough players to start new round: {self.players}')
        
            
    def bettingRound(self):
        self.actionIndex = nextPlayerIndex(self.dealerButtonIdx, self.nplayers)
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