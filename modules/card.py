"""

Developer: Lance Yao

"""
from modules.card_enums import CardEnum


class Card:
    """
    Poker Card
    """
    def __init__(self, rank: int, suit: int):
        if rank not in CardEnum.RANK_DICT.value or suit not in CardEnum.SUIT_DICT.value:
            raise ValueError('Values provided not in range')
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return '{} {}'.format(CardEnum.SUIT_DICT.value[self.suit],
                              CardEnum.RANK_DICT.value[self.rank])

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({} {})'.format(class_name,
                                  CardEnum.SUIT_DICT.value[self.suit],
                                  CardEnum.RANK_DICT.value[self.rank])

    def __eq__(self, other):
        return self.rank == other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __hash__(self):
        return hash((self.rank, self.suit))
