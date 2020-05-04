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
import Player
import random
random.seed() # automatically uses system time

# automatically uses system time

class RandomPlayer(Player.Player):
    def __init__(self, name, team):
		self.BaseSetUp(name, team)

    def playCard(self):
        moves = self.validMoves()
        chosen = random.choice(moves)
        self.hand.remove(chosen)
        print "%s plays %s" % (self.name, chosen)
        return chosen

    def updateInfo(self, winner):
        # not necessary for random play
        pass

    def orderUp(self, center_card):
        choice = random.choice([True, False])
        if choice == True:
            print "%s orders up" % (self.name)
        else:
            print "%s passes" % (self.name)

    def pickSuit(self, out_suit):
        if random.choice([True, False]) or game.dealer == self:
            choice = random.choice([x for x in [heart, spade, club, diamond] if x != out_suit])
            print "%s plays %s" % (self.name, choice)
            return choice
        else:
            print "%s passes" % (self.name)
            return None

    def discardCard(self, card):
        assert type(card) == Card, "pickUp was given a %s, it wants a Card" % type(card)
        discard = random.choice(self.hand)
        self.hand.append(card)
        self.hand.remove(discard)
        return discard

    def reset(self):
        # not necessary for random play
        pass

##----------------------We need to implement out-suit for selecting
    def orderUpCard(self, topCard):
        print "%s passes, like a bitch" % self.name
        return False

    def orderUpSuit(self):
        print "%s passes...again, like a HUGH bitch" % self.name
        return "pass"

    def forceOrderUp(self):
            choice = random.choice([heart, spade, club, diamond])
            print "%s bids %s" % (self.name, choice)
            return choice