import unittest

from models.card import Card
from models.deck import StandardDeck


class TestStandardDeck(unittest.TestCase):

    def test_standard_deck_initialization(self):
        deck = StandardDeck()
        self.assertEqual(len(deck.cards), 52)

    def test_standard_deck_shuffle(self):
        deck = StandardDeck()
        original_order = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)

    def test_standard_deck_deal_card(self):
        deck = StandardDeck()
        card = deck.deal_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.cards), 51)

    def test_standard_deck_deal_card_empty_deck(self):
        deck = StandardDeck()
        while deck.cards:
            deck.deal_card()
        with self.assertRaises(ValueError):
            deck.deal_card()