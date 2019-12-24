"""

Developer: Lance Yao

"""
from enum import Enum


class CardEnum(Enum):

    RANK_DICT = {1: 'Ace',
                 2: '2',
                 3: '3',
                 4: '4',
                 5: '5',
                 6: '6',
                 7: '7',
                 8: '8',
                 9: '9',
                 10: '10',
                 11: 'Jack',
                 12: 'Queen',
                 13: 'King'}

    SUIT_DICT = {1: '♠',
                 2: '♥',
                 3: '♦',
                 4: '♣'}
