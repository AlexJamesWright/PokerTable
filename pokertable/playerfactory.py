from pokertable.errors import PlayerTypeError
from pokertable.enums import PlayerType
from pokertable.players import Player, Setter, User


class PlayerFactory:
    
    def __init__(self):
        self._playersMade = 0
    
    def newPlayer(self, kind=PlayerType.BASE, stack=10, **kwargs):
        # TODO this would be perfect for pattern matching with py310 comes out on conda
        if kind == PlayerType.BASE:
            player = Player(stack=stack, iden=self._playersMade, kwargs=kwargs)
        elif kind == PlayerType.SETTER:
            player = Setter(stack=stack, iden=self._playersMade, kwargs=kwargs)
        elif kind == PlayerType.USER:
            player = User(stack=stack, iden=self._playersMade, kwargs=kwargs)
        else:
            raise PlayerTypeError(f"Player type {kind} not recognised")
        
        
        self._playersMade += 1
        return player