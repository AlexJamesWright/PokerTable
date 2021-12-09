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
        self.maxBet = 0
        self.ante = ante
        self.actionIndex = None
        self.pots = Pots(self.players)
        self.boardCards = [None, None, None, None, None]
        self.lastRaise = 0
        
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
        self.pots.finalise()

    def _postSmallBlind(self):
        self.pots.betSize(self.smallBlind+self.ante, self.players[self.actionIndex])
        self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers, self.players)
    
    def _postBigBlind(self):
        self.pots.betSize(self.bigBlind+self.ante, self.players[self.actionIndex])
        self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers, self.players)
        self.maxBet = self.bigBlind+self.ante
        self.lastRaise = self.smallBlind

    def _prepareBettingRound(self):
        # Start of betting round, so set all madeBets to false
        for player in self.players:
            if not player.folded and not player.allIn:
                player.betMade = False
        self.pots.finalised = False

    def bettingRound(self, finalisePots=True):
       
        self._prepareBettingRound()

        while self._stillBetting():
            if not self.players[self.actionIndex].folded: self.getPlayerBet(self.players[self.actionIndex])
            self.actionIndex = nextPlayerIndex(self.actionIndex, self.nplayers, self.players)
        # End of betting round, reset maxBet for next betting round and 
        self.maxBet = self.bigBlind
        self.lastRaise = 0
        self.actionIndex = nextPlayerIndex(self.dealerButtonIdx, self.nplayers, self.players)

        if finalisePots: self.pots.finalise()

    def _playerListOfFinishedBetting(self):
        return [player.betMade and (player.folded or player.allIn or (player.id in self.pots.playerBets and self.pots.playerBets[player.id] == self.pots.currentBetSize)) for player in self.players]

    def _playerListOfActiveBetting(self):
        return np.logical_not(self._playerListOfFinishedBetting())

    def _finishedBetting(self) -> bool:
        """
        Has everyone called, checked or folded?
        """
        return self.pots.finalised or bool(np.prod(self._playerListOfFinishedBetting()))

    def _stillBetting(self) -> bool:
        """
        Has everyone called, checked or folded?
        """
        return not self._finishedBetting()

    def getPlayerBet(self, player):
        if not player.allIn:
            self.printBettingInfo(player)
            valid = False 
            while not valid:
                amount = player.getBet()
                valid = self.checkValidAmount(amount, player)
            self.pots.betSize(amount, player)
            if amount == 0 and self.lastRaise > 0:
                player.folded = True
            
    def checkValidAmount(self, amount, player):
            
        if amount >= player.stack:
            amount = player.stack
            player.allIn = True

        raiseSize = amount - self.maxBet
        if amount==0 or raiseSize==0 or raiseSize>=self.lastRaise or player.allIn:
            # if call/check or raise
            if amount > self.maxBet: 
                self.lastRaise = raiseSize
            if amount > 0:
                # This is the new largest bet (or equal size)
                self.maxBet = amount
            return True

        return self.invalidBetStatement(amount, self.maxBet, self.pots.currentBetSize+self.lastRaise, player.stack)

    def invalidBetStatement(self, amount, maxBet, minRaise, stack):
        # TODO This is not always true... can check on 0 post flop
        print(f"\nInvalid bet size of {amount}. Player's stack is {stack}.\nTo fold is 0; To call/check is {maxBet}; To min raise is {minRaise}")
        return False 

    def printBettingInfo(self, player):
        print('\n\n')
        print(self.pots)
        print(f'Current bet = {self.lastRaise}')
        print(f"\nBoard = {self.boardCards}")
        print(player)