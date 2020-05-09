from Game import Game
from game_globals import Card
import codecs

# Getting the unicode chars for the suits
heart = u"\u2665"
spade = u"\u2660"
diamond = u"\u2666"
club = u"\u2663"

# assert sum([1, 2, 3]) == 6, "Should be 6"

game = Game()
card = Card(diamond, 11)
game.trump = heart

assert card.offSuit() == heart

assert card.isLeft()

assert card.isTrump()