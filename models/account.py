from dataclasses import dataclass

@dataclass
class Account:
    """A data class representing a user account in a casino game.

    Attributes:
        username (str): The username of the account holder.
        chips (int): The number of chips or currency units associated with the account.

    Example:
        >>> account = Account("player1", 1000)
        >>> account.username
        'player1'
        >>> account.chips
        1000
    """
    username: str
    chips: int
