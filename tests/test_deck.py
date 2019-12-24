import unittest
from modules.deck import Deck
from modules.card import Card


class TestDeck(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = Deck()
        self.benchmark = set([Card(rank, suit)
                              for rank in range(1, 14)
                              for suit in range(1, 5)])

    def test_deck_content(self):
        benchmark = set(self.benchmark)
        for card in self.deck:
            self.assertIn(card, benchmark)
            benchmark.remove(card)
        self.assertEqual(len(benchmark), 0)

    def test_offer(self):
        card = self.deck.offer()  # Offer from the deck top
        self.assertIsInstance(card, Card)
        self.deck.append(card)  # Put the card back to the deck top

    def test_deck_len(self):
        self.assertEqual(len(self.deck), 52)
        card = self.deck.offer()
        self.assertEqual(len(self.deck), 51)
        self.deck.append(card)
