from game_globals import *
import random


class Round(object):
    def __init__(self, players):
        self.players = players
        self.deck = list(allcards[:])  # get a deep copy of all_cards for dealing

    def playRound(self):  # begins the next 5 tricks
        print "Start a round!  Deal dem cards yo."
        self.dealCards()
        self.players[0].team.roundScore = 0
        self.players[1].team.roundScore = 0

        game.trump = self.bid()
        print "trump is set to %s" % game.trump

        self.leader = self.players[(self.players.index(game.dealer) + 1 % 4)]
        for x in range(5):
            self.leader = self.playTrick(self.leader)

        winner = "TODO"
        return winner

    def playTrick(self, leader):
        # reset game.center (the middle of the table)
        game.resetTrick()
        # get the start card from leader
        # assume cards played are legal
        played = leader.playCard()
        game.center[played] = leader

        if played.isTrump():
            game.lead = played.offSuit()
        else:
            game.lead = played.suit

        # play the trick
        leader_index = self.players.index(leader)

        for x in range(1, 4):
            turnIndex = leader_index + x
            played = self.players[turnIndex % 4].playCard()
            game.center[played] = self.players[(turnIndex) % 4]

        # return the winner of the trick
        win_card = self.getWinningCard()
        win_player = game.center[win_card]
        win_player.team.roundScore += 1
        print "%s wins the trick with %s " % (win_player.name, win_card)

        print "Team A roundScore %s" % self.players[0].team.roundScore
        print "Team B roundScore %s" % self.players[1].team.roundScore
        return win_player

    def bid(self):
        topCard = self.deck[0]
        print "Up card is: %s" % topCard

        for x in range(1, 5):
            hasOrdered = self.players[(self.players.index(game.dealer) + x % 4)].orderUpCard(topCard)
            if hasOrdered:
                game.dealer.discardCard(hasOrdered)
                return topCard.suit

        print "%s is flipped down" % topCard
        for x in range(1, 4):
            orderedSuit = self.players[(self.players.index(game.dealer) + x % 4)].orderUpSuit()
            if orderedSuit != "pass":
                return orderedSuit

        return game.dealer.forceOrderUp()

    def getTrump(self):
        return self.trump

    def dealCards(self):
        random.shuffle(self.deck)  # mutates deck
        deal_index = self.players.index(game.dealer)

        for x in range(1, 5):
            self.players[(x + deal_index) % 4].setHand(self.deck[:5])
            self.deck = self.deck[5:]

    def getWinningCard(self):
        # Just pick a random card to start so I don't have to initialize one
        highest = next(iter(game.center))
        print "%s was lead" % game.lead
        for x in game.center:
            highest = highest.beats(x)

        # print "Winning card is %s|%s" % (highest.num,highest.suit)
        return highest
