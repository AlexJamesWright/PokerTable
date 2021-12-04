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

    def _preflopBetting(self, round):
        round.postPlayersBlindAnte()
        self._distributeHoleCards()
        round.bettingRound() 

    def _flopBetting(self, round):
        self._flopCards(round)
        round.bettingRound()

    def _turnBetting(self, round):
        self._turnCards(round)
        round.bettingRound() 

    def _riverBetting(self, round):
        self._riverCards(round)
        round.bettingRound()
    
    def _postriverBetting(self, round):
        self._settleHand(round)
        self._finalise(round)

    def playHand(self, round):
        self._preflopBetting(round)
        self._flopBetting(round)
        self._turnBetting(round)
        self._riverBetting(round)
        self._postriverBetting(round)

    def _distributeHoleCards(self):
        for i, player in enumerate(self.playersList):
            player.setCard(self.roundCards[i])
        for i, player in enumerate(self.playersList):
            player.setCard(self.roundCards[i+self.nplayers])
    
    def _flopCards(self, round):
        round.boardCards[:3] = self.roundCards[-5:-2]
        round.actionIndex = nextPlayerIndex(self.dealerButtonIndex, self.nplayers) # If player is folded, round.bettingRound handles this

    def _turnCards(self, round):
        round.boardCards[3] = self.roundCards[-2]
        round.actionIndex = nextPlayerIndex(self.dealerButtonIndex, self.nplayers) # If player is folded, round.bettingRound handles this
    
    def _riverCards(self, round):
        round.boardCards[4] = self.roundCards[-1]
        round.actionIndex = nextPlayerIndex(self.dealerButtonIndex, self.nplayers) # If player is folded, round.bettingRound handles this
    
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
