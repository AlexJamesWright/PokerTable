from enum import Enum 

class Action(Enum):
    RAISE = 'raise'
    CHECK = 'check'
    CALL = 'call'
    FOLD = 'fold'
    WAIT = 'wait'
    
    
class PlayerType(Enum):
    BASE = 'BasePlayer'
    USER = 'UserPlayer'