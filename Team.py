
class Team():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score = 0

    def addScore(self, point):
        self.score += point

    def getScore(self):
        return self.score

    def showTeam(self):
        print "Team: %s, %s" % (self.player1.name, self.player2.name)

    def hasWon(self):
        if self.score >= 11:
            return True
        else:
            return False
