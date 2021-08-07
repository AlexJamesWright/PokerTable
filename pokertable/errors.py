class PlayerIDError(Exception):
    """Player ID already in use"""
    pass

class PlayerTypeError(Exception):
    """Player type not recognised"""
    pass

class InvalidBetAmount(Exception):
    """Invalid bet amount"""
    pass