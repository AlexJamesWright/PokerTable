class PlayerIDError(Exception):
    """Player ID already in use"""
    pass

class PlayerKindError(Exception):
    """Player kind not recognised"""
    pass

class InvalidBetAmount(Exception):
    """Invalid bet amount"""
    pass