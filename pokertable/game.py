from pokertable.round import Round
from pokertable.cards import Cards
import numpy as np

class Game:
    
    def __init__(self, players: list):
        self.players = players
        self.nplayers = len(players)
        self._dealerButtonIndexPositive = np.random.randint(self.nplayers)
        
    def _getDealerButtonIndex(self):
        return self._dealerButtonIndexPositive
        
    def playAllHands(self, nrounds: int=100):
        # Get cards 
        cards = Cards.setUpDecks(nrounds, self.nplayers)
        for i in range(nrounds):
            dealerButtonIndex = self._dealerButtonIndexPositive-self.nplayers
            
            # New round 
            round = Round(self.players.copy(), cards[i], dealerButtonIndex)
            # round.newRound() TODO Replace line above when implemented
            self.playHand(round)
        
    def playHand(self, round):
        round.postPlayersBlindAnte()
        self._distributeCards(round)
        round.preflopBetting(round) 
        self._flop(round)
        round.bettingRound(round)
        self._turn(round)
        round.bettingRound(round) 
        self._river(round)
        round.bettingRound(round)
        self._settleHand(round)
        self._finalise(round)
        
    @classmethod
    def _distributeCards(cls, round):
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
        # Are there more than two players? If yes, keep playing, otherwise end game
        # Update dealer button 
        self._dealerButtonIndexPositive = (self._dealerButtonIndexPositive+1)%self.nplayers
        
    def summary(self, playerIdx):
        # Show player's hole cards, flop, turn and river cards, all players' stacks, and pot sizes
        pass
