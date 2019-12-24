"""

Developer: Lance Yao

"""
from collections.abc import MutableSequence
from modules.card_enums import CardEnum
from modules.card import Card
from random import shuffle, randrange


class Deck(MutableSequence):
    """
    A Deck with 52 Cards upon init
    """

    def __init__(self):
        self._deck = [Card(rank, suit)
                      for rank in CardEnum.RANK_DICT.value
                      for suit in CardEnum.SUIT_DICT.value]

    def __str__(self):
        return 'Deck of {} cards'.format(len(self))

    def __repr__(self):
        pass

    def __getitem__(self, item):
        return self._deck[item]

    def __setitem__(self, key, value):
        self._deck[key] = value

    def __delitem__(self, key):
        self._deck.remove(key)

    def __len__(self):
        return len(self._deck)

    def insert(self, index, card):
        self._deck.insert(index, card)

    def shuffle(self):
        shuffle(self._deck)

    def offer(self):
        return self._deck.pop()

    def offer_random(self):
        index = randrange(len(self))
        card = self._deck[index]
        del self._deck[index]
        return card
