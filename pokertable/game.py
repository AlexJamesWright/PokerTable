from pokertable.utils import nextPlayerIndex
from pokertable.round import Round
from pokertable.cards import Cards
import numpy as np

class Game:
    
    def __init__(self, playersList: dict):
        self.playersList = playersList
        self.__nplayers = len(self.playersList)
        self.dealerButtonIndex = 0#np.random.randint(self.nplayers)
        
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
            # Get cards for this round
            self.roundCards = cards[maxRounds-self.roundsLeft]
            # New round 
            round = Round(self.playersList, self.dealerButtonIndex)
            # round.newRound() TODO Replace line above when implemented
            self.playHand(round)

        
    def playHand(self, round):
        round.postPlayersBlindAnte()
        self._distributeHoleCards()
        round.bettingRound() 
        self._flop(round)
        print("The next round of betting doesnt work as Round thinks all betting has finished!")
        round.bettingRound()
        self._turn(round)
        round.bettingRound() 
        self._river(round)
        round.bettingRound()
        self._settleHand(round)
        self._finalise(round)
        
    def _distributeHoleCards(self):
        for i, player in enumerate(self.playersList):
            player.setCard(self.roundCards[i])
        for i, player in enumerate(self.playersList):
            player.setCard(self.roundCards[i+self.nplayers])
    

    def _flop(self, round):
        round.boardCards[:3] = self.roundCards[-5:-2]

    def _turn(self, round):
        round.boardCards[3] = self.roundCards[-2]
    
    def _river(self, round):
        round.boardCards[4] = self.roundCards[-1]
    
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
