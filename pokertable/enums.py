from enum import Enum 

class Action(Enum):
    BLINDS = 'BLINDS'
    CALLED = 'CALLED'
    RAISED = 'RAISED'
    FOLDED = 'FOLDED'
    CHECKED = 'CHECKED'
    
    
class PlayerType(Enum):
    BASE = 'BasePlayer'
    USER = 'UserPlayer'