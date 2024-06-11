from dataclasses import dataclass
from enum import Enum


class Suit(Enum):
    """
    An enumeration representing the suits of playing cards.

    Attributes:
        HEARTS: The Hearts suit represented by '♥'.
        DIAMONDS: The Diamonds suit represented by '♦'.
        CLUBS: The Clubs suit represented by '♣'.
        SPADES: The Spades suit represented by '♠'.
    """
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'
    SPADES = '♠'


class Rank(Enum):
    """
    An enumeration representing the ranks of playing cards.

    Attributes:
        TWO: The rank Two.
        THREE: The rank Three.
        FOUR: The rank Four.
        FIVE: The rank Five.
        SIX: The rank Six.
        SEVEN: The rank Seven.
        EIGHT: The rank Eight.
        NINE: The rank Nine.
        TEN: The rank Ten.
        JACK: The rank Jack.
        QUEEN: The rank Queen.
        KING: The rank King.
        ACE: The rank Ace.
    """
    TWO = {
        "str": '2',
        "int": 2
    }
    THREE = {
        "str": '3',
        "int": 3
    }
    FOUR = {
        "str": '4',
        "int": 4
    }
    FIVE = {
        "str": '5',
        "int": 5
    }
    SIX = {
        "str": '6',
        "int": 6
    }
    SEVEN = {
        "str": '7',
        "int": 7
    }
    EIGHT = {
        "str": '8',
        "int": 8
    }
    NINE = {
        "str": '9',
        "int": 9
    }
    TEN = {
        "str": '10',
        "int": 10
    }
    JACK = {
        "str": 'J',
        "int": 11
    }
    QUEEN = {
        "str": 'Q',
        "int": 12
    }
    KING = {
        "str": 'K',
        "int": 13
    }
    ACE = {
        "str": 'A',
        "int": 14
    }

    @property
    def str(self):
        """
        Get the string representation of the rank.

        Returns:
            str: The string representation of the rank.
        """
        return self.value['str']

    @property
    def int(self):
        """
        Get the integer representation of the rank.

        Returns:
            int: The integer representation of the rank.
        """
        return self.value['int']


@dataclass
class Card:
    """
    Represents a playing card with a rank and a suit.

    Attributes:
        rank (Rank): The rank of the card (e.g., TWO, THREE, ..., KING, ACE).
        suit (Suit): The suit of the card (e.g., HEARTS, DIAMONDS, CLUBS, SPADES).

    Methods:
        __repr__: Returns a string representation of the card in the format '{rank}{suit}'.
    """

    rank: Rank
    suit: Suit

    def __lt__(self, other):
        """
        Defines the behavior of the '<' operator for Card instances.
        """
        if isinstance(other, Card):
            return self.rank.int < other.rank.int
        raise TypeError("Cannot compare Card with non-Card object.")

    def __repr__(self):
        """
        Returns a string representation of the card in the format '{rank}{suit}'.

        Returns:
            str: The string representation of the card.
        """
        return f'{self.rank.str}{self.suit.value}'
