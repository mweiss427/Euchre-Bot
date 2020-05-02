from Team import Team
from game_globals import *
from Round import Round
import RandomPlayer

# holder and runner of the entire game

class Game():
    def __init__(self):
        # initialize AI's here

        self.playerA1 = RandomPlayer.RandomPlayer("Tyler")
        self.playerA2 = RandomPlayer.RandomPlayer("Hudson")
        self.playerB1 = RandomPlayer.RandomPlayer("Shawn")
        self.playerB2 = RandomPlayer.RandomPlayer("Matt")

        # make a list of the players for rotations
        self.players = [self.playerA1, self.playerB1, self.playerA2, self.playerB2]

        # make teams of players across from one another
        self.team1 = Team(self.playerA1, self.playerA2)
        self.team2 = Team(self.playerB1, self.playerB2)

        # Player A1 is the default first player, it is then rotated each round
        game.dealer = self.playerA1

    # Begins the game
    def playGame(self):
        self.team1.showTeam()
        self.team2.showTeam()

        # Checks that both teams have not reached 11 before moving to the next round
        while not self.team1.hasWon() and not self.team2.hasWon():
            currentRound = Round(self.players)
            currentRound.playRound()
            self.allotScore(currentRound)
            self.dealer = self.rotateDeal()


    def allotScore(round):
        # simple rules used, no going alone  -- Should be redone -Shawn
        if game.caller == round.playerA1 or game.caller == round.playerA2:  # caller is in team A
            c_team = "A"
            c_tricks = game.tricksA
        else:
            c_tricks = game.tricksB
            c_team = "B"

        out.log("\t\tCaller: %s  Tricks: A; %d B; %d C: %d" % (c_team, game.tricksA, game.tricksB, c_tricks))

        if c_tricks == 0:
            if c_team != "A":
                game.scoreA += 4
            else:
                game.scoreB += 4
        elif c_tricks == 1 or c_tricks == 2:
            if c_team != "A":
                game.scoreA += 2
            else:
                game.scoreB += 2
        elif c_tricks == 3 or c_tricks == 4:
            if c_team == "A":
                game.scoreA += 1
            else:
                game.scoreB += 1
        else:
            if c_team == "A":
                game.scoreA += 2
            else:
                game.scoreB += 2

#    Leaving off for a week then deleting (Replaced with team.hasWon())
#    def hasWinner(self):
#        if game.scoreA >= 10:
#            print "Team A Has won!"
#            return True
#        elif game.scoreB >= 10:
#            print "Team B Has won!"
#            return True
#        else:
#            return False

#   Leaving off for a week then deleting (Replaced with while loop in playGame())
#    def endGame(self):  # ends the game
#        if game.scoreA >= 10:
#            print "Players %s and %s have won!" % (self.playerA1.name, self.playerA2.name)
#            out.log("Players %s and %s have won!" % (self.playerA1.name, self.playerA2.name))
#        elif game.scoreB >= 10:
#            print "Players %s and %s have won!" % (self.playerB1.name, self.playerB2.name)
#            out.log("Players %s and %s have won!" % (self.playerB1.name, self.playerB2.name))
#        print "With a score of %d to %d." % (game.scoreA, game.scoreB)
#        out.log("With a score of %d to %d." % (game.scoreA, game.scoreB))

    def rotateDeal(self):  # rotate the dealer
        # use this if game.dealer is a direct reference
        return self.players[(self.players.index(self.dealer) + 1) % 4]