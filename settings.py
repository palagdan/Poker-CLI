from dataclasses import dataclass
from models.deck import Deck
from models.player import Player
from utils.TexasHoldemStates import TexasHoldemState, Action

@dataclass
class GameSettings:
    """
    A data class representing the settings for a game of Texas Hold'em.

    Attributes:
        players (list): A list of Player objects representing the players in the game.
        deck (Deck): The deck of cards used in the game.
        dealer (int): The index of the dealer player in the players list.
        small_blind (int): The amount of the small blind in the game.
        big_blind (int): The amount of the big blind in the game.
    """
    players: list[Player]
    deck: Deck
    dealer: int
    small_blind: int
    big_blind: int
