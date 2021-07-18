def nextPlayerIndex(currentIndex, nplayers):
    """
    Increment a player index by one. 
    """
    return (currentIndex + 1) % -nplayers
    