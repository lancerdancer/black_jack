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

    def __init__(self, cards=None):
        if cards is None:
            self.cards = [Card(rank, suit)
                          for rank in CardEnum.RANK_DICT.value
                          for suit in CardEnum.SUIT_DICT.value]
        else:
            self.cards = []
            for card in cards:
                if isinstance(card, Card):
                    self.cards.append(card)
                elif isinstance(card, tuple):
                    self.cards.append(Card(card[0], card[1]))
                else:
                    raise ValueError

    def __str__(self):
        return 'Deck of {} cards'.format(len(self))

    def __repr__(self):
        pass

    def __getitem__(self, index):
        return self.cards[index]

    def __setitem__(self, index, value):
        self.cards[index] = value

    def __delitem__(self, index):
        self.cards.remove(index)

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        if isinstance(other, Deck):
            return self.__class__(self.cards + other.cards)
        elif isinstance(other, type(self.cards)):
            return self.__class__(self.cards + other)
        return self.__class__(self.cards + list(other))

    def insert(self, index, card):
        self.cards.insert(index, card)

    def shuffle(self):
        shuffle(self.cards)

    def offer(self):
        return self.cards.pop()

    def offer_random(self):
        index = randrange(len(self))
        card = self.cards[index]
        del self.cards[index]
        return card
