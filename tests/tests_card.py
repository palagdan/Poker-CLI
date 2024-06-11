import unittest
from models.card import Card, Rank, Suit


class TestCard(unittest.TestCase):

    def test_card_creation(self):
        card = Card(rank=Rank.ACE, suit=Suit.SPADES)
        self.assertEqual(card.rank, Rank.ACE)
        self.assertEqual(card.suit, Suit.SPADES)

    def test_card_comparison(self):
        card1 = Card(rank=Rank.JACK, suit=Suit.HEARTS)
        card2 = Card(rank=Rank.KING, suit=Suit.HEARTS)
        card3 = Card(rank=Rank.TEN, suit=Suit.DIAMONDS)

        self.assertTrue(card1 < card2)
        self.assertFalse(card2 < card1)
        self.assertFalse(card1 < card3)
        self.assertTrue(card3 < card1)

    def test_card_string_representation(self):
        card = Card(rank=Rank.QUEEN, suit=Suit.DIAMONDS)
        self.assertEqual(repr(card), 'Q♦')

    def test_rank_string_representation(self):
        self.assertEqual(Rank.TWO.str, '2')
        self.assertEqual(Rank.KING.str, 'K')
        self.assertEqual(Rank.ACE.str, 'A')

    def test_rank_integer_representation(self):
        self.assertEqual(Rank.FIVE.int, 5)
        self.assertEqual(Rank.JACK.int, 11)
        self.assertEqual(Rank.ACE.int, 14)
