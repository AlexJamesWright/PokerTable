from pokertable.utils import nextPlayerIndex
from pokertable.players import Player
from pokertable.pots import Pots
import numpy as np

class Round:
    """
    Container for all things related to a single round. Contains the players,
    pots, and utility methods. This class handles betting.
    """
    def __init__(self, players, dealerButtonIdx=0, smallBlind=1, bigBlind=None, ante=0):
        self.players: list[Player] = players
        self._nplayers = len(self.players)
        self.dealerButtonIdx = dealerButtonIdx
        self.smallBlind = smallBlind 
        self.bigBlind = bigBlind or 2*smallBlind
        self.maxBet = self.bigBlind
        self.ante = ante
        self.actionIndex = None
        self.pots = Pots(self.players)
        self.boardCards = [None, None, None, None, None]
        
    @property 
    def nplayers(self):
        return len(self.players)
        
    def newRound(self):
        # TODO Might be more efficient to reset some variables, rather than 
        # create a new instance of Round in Game.playAllHands for every round
        # Would need to:
        #   - drop bust players here
        #   - reset largest bet size
        #   - new Pots() for self.pots
        pass 
    
    
    def finishedBetting(self):
        pass
    
        
    def postPlayersBlindAnte(self):
        # Starting new round
        self._startNewRound()
        self._postAntes()
        self._postSmallBlind()
        self._postBigBlind()
            
    def _startNewRound(self):
        # For a new round, we need to set the action index 
        if self.nplayers > 2:
            self.actionIndex = nextPlayerIndex(self.dealerButtonIdx, self.nplayers)
        elif self.nplayers == 2:
            self.actionIndex = self.dealerButtonIdx
        else:
            raise RuntimeError(f'Not enough players to start new round: {self.players}')
        
    def _postAntes(self):
        for player in self.players:
            self.pots.betSize(self.ante, player)

    def _postSmallBlind(self):
        self.pots.betSize(self.smallBlind+self.ante, self.players[self.actionIndex])
        self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers)
    
    def _postBigBlind(self):
        self.pots.betSize(self.bigBlind+self.ante, self.players[self.actionIndex])
        self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers)
            
    def bettingRound(self):
        self.lastRaise = self.bigBlind
        while self._stillBetting():
            if not self.players[self.actionIndex].folded: self.getPlayerBet(self.players[self.actionIndex])
            self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers)
        # End of betting round, reset maxBet for next betting round
        self.maxBet = self.bigBlind
        self.actionIndex = nextPlayerIndex(self.dealerButtonIdx, self.nplayers)
        
    def _finishedBetting(self) -> bool:
        """
        Has everyone called, checked or folded?
        """
        return bool(np.prod([player.folded or self.pots.playerBets[player.id] == self.pots.currentBetSize for player in self.players]))


    def _stillBetting(self) -> bool:
        """
        Has everyone called, checked or folded?
        """
        return not self._finishedBetting()
        
    def getPlayerBet(self, player):
        self.printBettingInfo(player)
        valid = False 
        while not valid:
            amount = self.players[self.actionIndex].getBet()
            valid = self.checkValidAmount(amount, player)
        self.pots.betSize(amount, self.players[self.actionIndex])
            
    def checkValidAmount(self, amount, player):

        if amount > player.stack:
            return self.invalidBetStatement(amount, self.maxBet, self.pots.currentBetSize+self.lastRaise, player.stack)

        raiseSize = amount - self.maxBet
        if amount==0 or raiseSize==0 or raiseSize>=self.lastRaise:
            # if call/check or raise
            if amount > self.maxBet: 
                self.lastRaise = raiseSize
            if amount > 0:
                self.maxBet = amount
                # TODO maxBet can be set higher than a persons stack size!
            return True

        return self.invalidBetStatement(amount, self.maxBet, self.pots.currentBetSize+self.lastRaise, player.stack)

    def invalidBetStatement(self, amount, maxBet, minRaise, stack):
        print(f"\nInvalid bet size of {amount}. Player's stack is {stack}.\nTo fold is 0; To call/check is {maxBet}; To min raise is {minRaise}")
        return False 

    def printBettingInfo(self, player):
        print('\n\n')
        print(self.pots)
        print(f"\nBoard = {self.boardCards}")
        print(player)