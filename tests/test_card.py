import unittest
from modules.card import Card

class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.target = Card(5, 2)
        self.target_equal = Card(5, 3)
        self.target_big = Card(10, 1)
        self.target_small = Card(1, 4)

    def test_instance(self):
        self.assertIsInstance(self.target, Card)

    def test_rank(self):
        self.assertEqual(self.target.rank, 5)

    def test_suit(self):
        self.assertEqual(self.target.suit, 2)

    def test_equal(self):
        self.assertEqual(self.target, self.target_equal)

    def test_greater(self):
        self.assertGreater(self.target, self.target_small)

    def test_less(self):
        self.assertLess(self.target, self.target_big)

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError, Card(-1, 1))
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError, Card(0, 1))
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError, Card(14, 1))

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError, Card(1, -1))
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError, Card(1, 0))
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError, Card(1, 5))
