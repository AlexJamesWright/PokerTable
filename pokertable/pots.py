import numpy as np

class Pot:
    """
    A single pot of money. All players must have the same amount of chips
    in the pot.
    """
    
    def __init__(self, potNo: int=0):
        self.__size = 0
        self.id = potNo
        self.playersDict = {}   # {playerid: Player}
        self.newBets = {}       # {playerid: bet amount}
        self.bets = []          # newBets for each round
        
    @property
    def size(self):
        return sum([sum(roundBets.values()) for roundBets in self.bets])
        
    def betSize(self, amount, player):
        if player not in self.playersDict: self.playersDict[player.id] = player
        self.newBets[player.id] = amount
        
    def finalise(self):
        for id, amount in self.newBets.items():
            self.playersDict[id].stack -= amount
            
        self.bets.append(self.newBets)
        self.newBets = {}
            
    def __len__(self):
        """
        How many players are in the pot.
        """
        return len(self.playersDict)
        
    def __repr__(self):
        pdictstr = ''
        for r, roundBetting in enumerate(self.bets):
            pdictstr += f'\n\tRound {r}:'
            for id, amount in roundBetting.items():
                pdictstr += '\n\t\t' + self.playersDict[id].__repr__() + f', bet={amount}'
        return f'Pot {self.id}: size={self.size}' + pdictstr
        
class Pots:
    """
    Pot container, potentially holding multiple concurrent pots.
    """
    
    def __init__(self):
        self.pots = [Pot()]
        self.playerBets = {}
        self.playerDict = {}
        self.finalised = False
        
    def __getitem__(self, p):
        return self.pots[p]
    
    def __len__(self):
        """
        How many pots are there?
        """
        return len(self.pots)

    @property
    def nbettors(self):
        return len(self.playerBets)

    @property 
    def currentBetSize(self):
        return np.max(list(self.playerBets.values()))
    
    def betSize(self, amount, player):
        """
        Current size of bet to stay in hand, can be call, check, raise or all-in. 
        """
        if player.id not in self.playerDict: self.playerDict[player.id] = player
        if player.has(amount):
            self.playerBets[player.id] = amount
        else:
            self.playerBets[player.id] = player.stack
        self.finalised = False
         
    def finalise(self):
        """
        Until we finalise a round of betting, we will not take any players money. When 
        we finalise, we create the necessary pots and then reduce each players stack.
        """
        amounts = sorted(set(self.playerBets.values()))
        
        self._addAmountsToPot(self.pots[-1], self.playerBets.keys(), amounts[0])
        
        for potNo, amount in enumerate(amounts[1:]):
            prevAmount = amounts[potNo]
            self.pots.append(Pot(potNo=len(self.pots)))
            
            # Drop players that are all-in
            self.playerBets = {id: amount for id, amount in self.playerBets.items() if self.playerDict[id].stack > prevAmount}
            self._addAmountsToPot(self.pots[-1], self.playerBets.keys(), amount-prevAmount)
            
        # If only one player in any of the pots, the big stack has gone all in 
        # and been called. Give the big stack the left over.
        if len(self.pots[-1]) == 1:
            player = list(self.pots[-1].playersDict.values())[0]
            amount = self.pots[-1].size
            player.stack += amount 
            self.pots = self.pots[:-1]
            
            
        # Take players bets from stack
        for pot in self.pots:
            pot.finalise()
            
        self.playerBets = {}
        self.finalised = True
            
    def _addAmountsToPot(self, pot, playerids, amount):
        for playerid in playerids:
            pot.betSize(amount, self.playerDict[playerid])
        
    def __repr__(self):
        if self.finalised:
            s = ''
            for pot in self.pots:
                s += pot.__repr__()
        else:
            s = 'Unfinalised pots:'
            for id, playerbet in self.playerBets.items():
                s += f'\n\tPlayer {id}: bet={playerbet}, stack={self.playerDict[id].stack}'
        return s
