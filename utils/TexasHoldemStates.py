from enum import Enum

class Action(Enum):
    """
    An enumeration representing possible actions in a Texas Hold'em game.

    Attributes:
        FOLD (str): The action of folding, i.e., forfeiting the current hand.
        CHECK (str): The action of checking, i.e., declining to bet and passing the action to the next player.
        BET (str): The action of placing a bet.
        RAISE (str): The action of raising the current bet.
    """

    FOLD = "FOLD"
    CHECK = "CHECK"
    BET = "BET"
    RAISE = "RAISE"


class TexasHoldemState(Enum):
    """
    An enumeration representing the stages of a Texas Hold'em game.

    Attributes:
        PREFLOP (int): The stage before any community cards are dealt.
        FLOP (int): The stage where the first three community cards are dealt.
        TURN (int): The stage where the fourth community card is dealt.
        RIVER (int): The stage where the fifth and final community card is dealt.
        SHOWDOWN (int): The stage where the players reveal their hands to determine the winner.
        END (int): The stage indicating the end of the game.
    """

    PREFLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4
    SHOWDOWN = 5
    END = 6
