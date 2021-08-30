from pokertable.enums import PlayerType

class Player:
    
    kind = PlayerType.BASE
    id = None
    
    def __init__(self, stack: float, iden: int=None, **kwargs):
        self.stack = stack 
        self.id = iden
        self.holdCards = None
       
    def has(self, amount: float):
        return self.stack >= amount
    
    def getBet(self):
        raise NotImplementedError

    @property
    def name(self):
        return self.kind.value
    
    def __repr__(self):
        return f"Player {self.id}: stack={self.stack}"

class User(Player):

    kind = PlayerType.USER

    def getBet(self):
        return input("Enter betsize: ")

class Caller(Player):
    
    def getBet(self):
        pass