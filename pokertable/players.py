from pokertable.errors import PlayerIDError

class Player:
    
    name = 'BasePlayer'
    allIdens = []
    
    def __init__(self, stack: float, iden: int=None, kwargs: dict=None):
        self.stack = stack 
        self.id = iden
       
    def has(self, amount: float):
        return self.stack >= amount
    


