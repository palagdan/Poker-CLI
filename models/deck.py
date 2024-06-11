import random
from models.card import Suit, Rank, Card


class Deck:
    """A class representing a standard deck of playing cards.

    Attributes:
        cards (list): A list containing Card objects representing the cards in the deck.

    Methods:
        __init__(): Initializes the deck with all 52 standard playing cards.
        shuffle(): Shuffles the cards in the deck.
        deal_card(): Deals a single card from the top of the deck.
    """

    def __init__(self):
        """Initialize the deck with all 52 standard playing cards."""
        self.cards = [Card(rank, suit) for suit in Suit for rank in Rank]

    def shuffle(self):
        """Shuffles the cards in the deck."""
        random.shuffle(self.cards)

    def deal_card(self):
        """Deal a single card from the top of the deck.

        Returns:
            Card: A Card object representing the dealt card.

        Raises:
            ValueError: If there are no cards left in the deck.
        """
        if self.cards:
            return self.cards.pop()
        else:
            raise ValueError("No cards left in the deck.")


class StandardDeck(Deck):
    """A class representing a standard deck of playing cards inheriting from Deck class."""

    def __init__(self):
        """Initialize the standard deck by calling the superclass's __init__ method."""
        super().__init__()
