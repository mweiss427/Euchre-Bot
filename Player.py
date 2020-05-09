# Collection of functions each AI should implement:
# __init__(self, name)
# playCard(self)
# updateInfo(self)
# orderUp(self, center_card)
# pickUp(self, card)
# pickSuit(self, out_suit)
# reset(self)
# setHand(self, new-hand)


from game_globals import *


class Player:
    def __init__(self, name):
        self.BaseSetUp(name)

    def BaseSetUp(self, name, team):
        self.name = name  # name is a unique identifier
        self.tricks = 0
        self.hand = []
        self.team = team

    def printHand(self):
        for x in range(len(self.hand)):
            print "[%d: %s], " % (x, self.hand[x]),
        print

    def validMoves(self):
        # assume that the lead, left bower problem is taken care of
        validmoves = []
        for x in self.hand:
            if x.num == 11:
                if game.lead == game.trump and x.suit == x.offSuit():
                    validmoves.append(x)
            elif x.suit == game.lead:
                validmoves.append(x)

        if not validmoves:
            validmoves = self.hand

        return tuple(validmoves)

    def setHand(self, hand):
        assert len(hand) == 5, "from setHand of %s, hand needs to be 5" % self.name
        self.hand = hand
