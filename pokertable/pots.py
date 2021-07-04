class Pot:
    def __init__(self, potNo: int=0):
        self.size = 0
        self.id = potNo
        self.playersDict = {}
        
    def add(self, amount, player):
        self.size += amount
        self.playersDict[player.id].stake -= amount
        
class Pots:
    def __init__(self):
        self.pots = [Pot()]
        self.playersIn = {}
        
    def __getitem__(self, p):
        return self.pots[p]
    
    def __len__(self):
        return len(self.pots)
    
    def addAmount(self, amount, player):
        if player.has(amount):
            self[-1].add(amount, player)
            self.playersIn[player.id] = player
        else:
            # Need to create a new pot, and retrospectively reduce this pots size
            pass

print(len(Pots()))