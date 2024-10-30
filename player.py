class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score
    
    def name(self,name):
        self.name = name

    def score(self):
        self.score += 1

