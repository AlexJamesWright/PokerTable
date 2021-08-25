from pokertable.enums import PlayerType

class Player:
    
    kind = PlayerType.BASE
    name = kind.value
    id = None
    
    def __init__(self, stack: float, iden: int=None, **kwargs):
        self.stack = stack 
        self.id = iden
        self.holdCards = None
       
    def has(self, amount: float):
        return self.stack >= amount
    
    def getBet(self):
        raise NotImplementedError
    
    def __repr__(self):
        return f"Player {self.id}: stack={self.stack}"


class Caller(Player):
    
    def getBet(self):