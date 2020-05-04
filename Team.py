
class Team():
    def __init__(self, teamName):
        self.name = teamName
        self.score = 0
        self.roundScore = 0

    def getScore(self):
        return self.score

    def hasWon(self):
        if self.score >= 11:
            return True
        else:
            return False
