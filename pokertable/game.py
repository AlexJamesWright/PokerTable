from pokertable.utils import nextPlayerIndex
from pokertable.round import Round
from pokertable.cards import Cards
import numpy as np

class Game:
    
    def __init__(self, playersList: dict):
        self.playersList = playersList
        self.__nplayers = len(self.playersList)
        self.dealerButtonIndex = np.random.randint(self.nplayers)
        
    @property
    def nplayers(self):
        """
        Players will drop out as they get busted, so need to return 
        nplayers dynamically.
        """
        return len(self.playersList)
    
    def anotherRound(self) -> bool:
        """"
        Should we play another round?
        """
        return self.nplayers > 1 and self.roundsLeft
        
    def playAllHands(self, maxRounds: int=100):
        self.roundsLeft = maxRounds
        
        # Get cards 
        cards = Cards.setUpDecks(maxRounds, self.nplayers)
        
        while self.anotherRound():
            # New round 
            round = Round(self.playersList, cards[maxRounds-self.roundsLeft], self.dealerButtonIndex)
            # round.newRound() TODO Replace line above when implemented
            self.playHand(round)
        
    def playHand(self, round):
        round.postPlayersBlindAnte()
        self._distributeCards(round)
        round.bettingRound() 
        self._flop(round)
        round.bettingRound()
        self._turn(round)
        round.bettingRound() 
        self._river(round)
        round.bettingRound()
        self._settleHand(round)
        self._finalise(round)
        
    def _distributeCards(self, round):
        holeCards = {}
        for player in self.playersList:
            pass
    
    @classmethod
    def _preflopBetting(cls, round):
        pass 
    
    @classmethod
    def _flop(cls, round):
        pass 
    
    @classmethod
    def _turn(cls, round):
        pass 
    
    @classmethod
    def _river(cls, round):
        pass 
    
    @ classmethod
    def _settleHand(cls, round):
        # Who won?
        pass
        
    def _finalise(self, round):
        # Kick out players who have no stack...
        for player in self.playersList:
            if player.stack < 0.01: del player
            
            
        # Move dealer button
        self.dealerButtonIndex = nextPlayerIndex(self.dealerButtonIndex, self.nplayers)
        
        self.roundsLeft -= 1
        
    def summary(self, playerIdx):
        # Show player's hole cards, flop, turn and river cards, all players' stacks, and pot sizes
        pass
