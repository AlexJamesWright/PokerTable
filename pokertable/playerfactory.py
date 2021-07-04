from pokertable.errors import PlayerKindError
from pokertable.players import Player

class PlayerFactory:
    
    def __init__(self):
        self._playersMade = 0
    
    def newPlayer(self, kind, stack, kwargs=None):
        # TODO this would be perfect for pattern matching with py310 comes out on conda
        if kind == 'Base':
            player = Player(stack, self._playersMade, **kwargs)
        else:
            raise PlayerKindError(f"Player kind {kind} not recognised")
        
        self._playersMade += 1
        return player