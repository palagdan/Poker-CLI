import unittest
from models.card import *
from utils.TexasHoldemCombinations import HandChecker, HandStrength


class TestHandChecker(unittest.TestCase):

    def setUp(self):
        self.combinations_dict = {
            HandStrength.HIGH_CARD: [
                Card(rank=Rank.TWO, suit=Suit.HEARTS),
                Card(rank=Rank.KING, suit=Suit.CLUBS),
                Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
                Card(rank=Rank.TEN, suit=Suit.SPADES),
                Card(rank=Rank.FIVE, suit=Suit.HEARTS)
            ],
            HandStrength.PAIR: [
                Card(rank=Rank.TWO, suit=Suit.HEARTS),
                Card(rank=Rank.TWO, suit=Suit.CLUBS),
                Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
                Card(rank=Rank.FOUR, suit=Suit.SPADES),
                Card(rank=Rank.FIVE, suit=Suit.HEARTS)
            ],

            HandStrength.TWO_PAIR: [
                Card(rank=Rank.TWO, suit=Suit.HEARTS),
                Card(rank=Rank.TWO, suit=Suit.CLUBS),
                Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
                Card(rank=Rank.THREE, suit=Suit.SPADES),
                Card(rank=Rank.FIVE, suit=Suit.HEARTS)
            ],
            HandStrength.THREE_OF_A_KIND: [
                Card(rank=Rank.TWO, suit=Suit.HEARTS),
                Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
                Card(rank=Rank.TWO, suit=Suit.SPADES),
                Card(rank=Rank.THREE, suit=Suit.SPADES),
                Card(rank=Rank.FIVE, suit=Suit.HEARTS)
            ],
            HandStrength.STRAIGHT: [
                Card(rank=Rank.TWO, suit=Suit.HEARTS),
                Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
                Card(rank=Rank.FOUR, suit=Suit.SPADES),
                Card(rank=Rank.FIVE, suit=Suit.SPADES),
                Card(rank=Rank.SIX, suit=Suit.HEARTS)
            ],
            HandStrength.FLUSH: [
                Card(rank=Rank.TWO, suit=Suit.HEARTS),
                Card(rank=Rank.THREE, suit=Suit.HEARTS),
                Card(rank=Rank.NINE, suit=Suit.HEARTS),
                Card(rank=Rank.KING, suit=Suit.HEARTS),
                Card(rank=Rank.ACE, suit=Suit.HEARTS)
            ],
            HandStrength.FULL_HOUSE: [
                Card(rank=Rank.TWO, suit=Suit.HEARTS),
                Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
                Card(rank=Rank.TWO, suit=Suit.SPADES),
                Card(rank=Rank.THREE, suit=Suit.SPADES),
                Card(rank=Rank.THREE, suit=Suit.HEARTS)
            ],
            HandStrength.FOUR_OF_A_KIND: [
                Card(rank=Rank.TWO, suit=Suit.HEARTS),
                Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
                Card(rank=Rank.TWO, suit=Suit.SPADES),
                Card(rank=Rank.TWO, suit=Suit.CLUBS)
            ],
            HandStrength.STRAIGHT_FLUSH: [
                Card(rank=Rank.TWO, suit=Suit.HEARTS),
                Card(rank=Rank.THREE, suit=Suit.HEARTS),
                Card(rank=Rank.FOUR, suit=Suit.HEARTS),
                Card(rank=Rank.FIVE, suit=Suit.HEARTS),
                Card(rank=Rank.SIX, suit=Suit.HEARTS)
            ]
        }

    def test_has_pair(self):
        self.assertTrue(HandChecker.has_pair(self.combinations_dict[HandStrength.PAIR]))
        self.assertFalse(HandChecker.has_pair(self.combinations_dict[HandStrength.HIGH_CARD]))

    def test_get_pair(self):
        self.assertEqual(HandChecker.get_pair(self.combinations_dict[HandStrength.PAIR]),
                         [Card(rank=Rank.TWO, suit=Suit.HEARTS),
                          Card(rank=Rank.TWO, suit=Suit.CLUBS)])

    def test_has_two_pairs(self):
        self.assertTrue(HandChecker.has_two_pair(self.combinations_dict[HandStrength.TWO_PAIR]))
        self.assertFalse(HandChecker.has_two_pair(self.combinations_dict[HandStrength.HIGH_CARD]))

    def test_get_two_pairs(self):
        self.assertEqual(HandChecker.get_two_pair(self.combinations_dict[HandStrength.TWO_PAIR]),
                         [Card(rank=Rank.TWO, suit=Suit.HEARTS),
                          Card(rank=Rank.TWO, suit=Suit.CLUBS),
                          Card(rank=Rank.THREE, suit=Suit.DIAMONDS),
                          Card(rank=Rank.THREE, suit=Suit.SPADES)])

    def test_has_three_of_kind(self):
        self.assertTrue(HandChecker.has_three_of_a_kind(self.combinations_dict[HandStrength.THREE_OF_A_KIND]))
        self.assertFalse(HandChecker.has_three_of_a_kind(self.combinations_dict[HandStrength.HIGH_CARD]))

    def test_get_three_of_kind(self):
        self.assertEqual(HandChecker.get_three_of_a_kind(self.combinations_dict[HandStrength.THREE_OF_A_KIND]),
                         [Card(rank=Rank.TWO, suit=Suit.HEARTS),
                          Card(rank=Rank.TWO, suit=Suit.DIAMONDS),
                          Card(rank=Rank.TWO, suit=Suit.SPADES)])

    def test_has_straight(self):
        self.assertTrue(HandChecker.has_straight(self.combinations_dict[HandStrength.STRAIGHT]))
        self.assertFalse(HandChecker.has_straight(self.combinations_dict[HandStrength.HIGH_CARD]))

    def test_get_straight(self):
        self.assertEqual(HandChecker.get_straight(self.combinations_dict[HandStrength.STRAIGHT]),
                         self.combinations_dict[HandStrength.STRAIGHT])

    def test_has_flush(self):
        self.assertTrue(HandChecker.has_flush(self.combinations_dict[HandStrength.FLUSH]))
        self.assertFalse(HandChecker.has_flush(self.combinations_dict[HandStrength.HIGH_CARD]))

    def test_get_flush(self):
        self.assertEqual(HandChecker.get_flush(self.combinations_dict[HandStrength.FLUSH]),
                         (self.combinations_dict[HandStrength.FLUSH]))

    def test_has_full_house(self):
        self.assertTrue(HandChecker.has_full_house(self.combinations_dict[HandStrength.FULL_HOUSE]))
        self.assertFalse(HandChecker.has_full_house(self.combinations_dict[HandStrength.HIGH_CARD]))

    def test_get_full_house(self):
        self.assertEqual(HandChecker.get_full_house(self.combinations_dict[HandStrength.FULL_HOUSE]),
                         (self.combinations_dict[HandStrength.FULL_HOUSE]))

    def test_has_four_of_kind(self):
        self.assertTrue(HandChecker.has_four_of_a_kind(self.combinations_dict[HandStrength.FOUR_OF_A_KIND]))
        self.assertFalse(HandChecker.has_four_of_a_kind(self.combinations_dict[HandStrength.HIGH_CARD]))

    def test_get_four_of_kind(self):
        self.assertEqual(HandChecker.get_four_of_a_kind(self.combinations_dict[HandStrength.FOUR_OF_A_KIND]),
                         (self.combinations_dict[HandStrength.FOUR_OF_A_KIND]))

    def test_has_straight_flush(self):
        self.assertTrue(HandChecker.has_straight_flush(self.combinations_dict[HandStrength.STRAIGHT_FLUSH]))
        self.assertFalse(HandChecker.has_straight_flush(self.combinations_dict[HandStrength.HIGH_CARD]))

    def test_get_straight_flush(self):
        self.assertEqual(HandChecker.get_straight_flush(self.combinations_dict[HandStrength.STRAIGHT_FLUSH]),
                         (self.combinations_dict[HandStrength.STRAIGHT_FLUSH]))
