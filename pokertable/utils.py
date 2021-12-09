def nextPlayerIndex(currentIndex, nplayers, players=None):
    """
    Increment a player index by one, skipping players 
    that are all in or folded if possible.
    """
    if players is not None:
        nextIdx = nextPlayerIndex(currentIndex, nplayers)
        while players[nextIdx].folded or players[nextIdx].allIn:
            nextIdx = nextPlayerIndex(nextIdx, nplayers)
        return nextIdx
    else:
        return (currentIndex + 1) % -nplayers
    