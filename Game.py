from Team import Team
from game_globals import *
from Round import Round
import RandomPlayer


# holder and runner of the entire game
class Game():
    def __init__(self):

        # Make teams of players across from one another
        self.team1 = Team("team1")
        self.team2 = Team("team2")

        # initialize AI's here
        self.playerA1 = RandomPlayer.RandomPlayer("Tyler", self.team1)
        self.playerA2 = RandomPlayer.RandomPlayer("Hudson", self.team1)
        self.playerB1 = RandomPlayer.RandomPlayer("Shawn", self.team2)
        self.playerB2 = RandomPlayer.RandomPlayer("Matt", self.team2)

        # make a list of the players for rotations
        self.players = [self.playerA1, self.playerB1, self.playerA2, self.playerB2]

        # Player A1 is the default first player, it is then rotated each round
        game.dealer = self.playerA1

    # Begins the game
    def playGame(self):
        # Checks that both teams have not reached 11 before moving to the next round
        while not self.team1.hasWon() and not self.team2.hasWon():
            currentRound = Round(self.players)
            currentRound.playRound()
            self.allotScore(currentRound)
            game.dealer = self.rotateDeal()

        return self.getWinner()


    def getWinner(self):
        if(self.team1.score >= 11):
            print "Team 1 Won:"
            print "The score was " \
                  "Team 1: %s" \
                  "TEam 2: %s" % (self.team1.score, self.team2.score)
            return self.team1
        else:
            print "Team 2 Won:"
            print "The score was " \
                  "Team 1: %s - " \
                  "Team 2: %s" % (self.team1.score, self.team2.score)
            self.team2
        pass

    def allotScore(self, round):
        scoreA = round.players[0].team.roundScore
        scoreB = round.players[1].team.roundScore
        #TODO add set logic 
        if scoreA > 3:
            if scoreA == 5:
                self.team1.score += 2
            else:
                self.team1.score += 1

        if scoreB > 3:
            if scoreB == 5:
                self.team2.score += 2
            else:
                self.team2.score += 1

        print "Team 1 Score %s" % self.team1.score
        print "Team 2 Score %s" % self.team2.score


    def rotateDeal(self):  # rotate the dealer
        # use this if game.dealer is a direct reference
        print "New dealer name is %s" % self.players[(self.players.index(game.dealer) + 1) % 4].name
        return self.players[((self.players.index(game.dealer) + 1) % 4)]
