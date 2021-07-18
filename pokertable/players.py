class Player:
    
    name = 'BasePlayer'
    allIdens = []
    id = None
    
    def __init__(self, stack: float, iden: int=None, kwargs: dict=None):
        self.stack = stack 
        self.id = iden
       
    def has(self, amount: float):
        return self.stack >= amount
    
    def __repr__(self):
        return f"Player {self.id}: stack={self.stack}"
