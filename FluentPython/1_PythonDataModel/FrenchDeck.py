import collections
from random import choice

# Construct a simple class to represent individual card.
# namedtuple builds classes of objects that are just bundles
# of atrributes with no custom methods
Card = collections.namedtuple("Card", ['rank', 'suit'])
#print(Card)

class FrenchDeck(object):
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    # len() function implementation
    def __len__(self):
        return (len(self._cards))

    # makes FrenchDeck' object subscriptable
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(len(deck))  # invokes dunder __len__() by the compiler

# can be used to get random from sequence
print(choice(deck))

# by implementing the __getitem__ special method, FrenchDeck is also iterable

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

# iteration is always implicit. If a collection has no __contains__ method,
# the "in" operator does a sequntial scan.

print(Card('Q', "hearts") in deck)
print(Card('2', "beasts") in deck)

# Sorting
# ranking cards with aces highest, and suit by spades(highest), hearts, diamonds, and clubs(lowest)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
