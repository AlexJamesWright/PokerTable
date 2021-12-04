from pokertable.enums import PlayerType

class Player:
    
    kind = PlayerType.BASE
    id = None
    
    def __init__(self, stack: float, iden: int=None, **kwargs):
        self.stack = stack 
        self.id = iden
        self.__holeCards = [None, None]
        self.folded = False
        self.betMade = False

    def setCard(self, card):
        if not self.__holeCards[0]:
            self.__holeCards[0] = card
        elif not self.__holeCards[1]:
            self.__holeCards[1] = card
        else:
            raise RuntimeError(f"Cannot set player's hole cards: already set as [{self.__holeCards[0]}, {self.__holeCards[1]}]")
       
    def has(self, amount: float):
        return self.stack >= amount
    
    def getBet(self):
        bet = self._getBet()
        self.folded = (bet < 1e-10)
        self.betMade = True
        return bet

    def _getBet(self):
        raise NotImplementedError

    @property
    def name(self):
        return self.kind.value
    
    def __repr__(self):
        return f"Player {self.id}:\n\tstack = {self.stack}\n\thole cards = {self.__holeCards}"


class Setter(Player):

    kind = PlayerType.SETTER 

    def __init__(self, stack: float, iden: int=None, **kwargs):
        super().__init__(stack, iden, **kwargs)
        self._betNumber = 0
        self.bets = []

    def setBet(self, betSize): 
        self.bets.append(betSize) 
        return self

    def _getBet(self):
        self._betNumber += 1
        return self.bets[-1]

class User(Player):

    kind = PlayerType.USER

    def _getBet(self):
        return int(input("Enter betsize: "))

class Caller(Player):
    
    def _getBet(self):
        pass