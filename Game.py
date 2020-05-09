from Team import Team
from game_globals import *
from Round import Round
import RandomPlayer

# holder and runner of the entire game

class Game():
    def __init__(self):

        #Make teams of players across from one another
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


    def rotateDeal(self):  # rotate the dealer
        # use this if game.dealer is a direct reference
        return self.players[(self.players.index(self.dealer) + 1) % 4]