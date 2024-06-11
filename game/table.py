from game.game import TexasHoldemGame
from utils.color import Color, print_with_color


class Table:
    """
    A class representing a poker table where Texas Hold'em games are played.

    Attributes:
        game_settings: The settings for the current game.
        games_played (int): The number of games played on the table.
        current_game: The current game being played on the table.
        dealer: The index of the dealer position at the table.

    Methods:
        start_new_game(game_settings): Starts a new Texas Hold'em game with the provided settings.
        createTable(game_settings): Creates and manages multiple Texas Hold'em games at the table.
        check_input_new_game(): Prompts the user to play another game or quit the table.
    """

    def __init__(self):
        """
        Initializes a Table instance.
        """
        self.game_settings = None
        self.games_played: int = 0
        self.current_game: None = None
        self.dealer = 0

    def start_new_game(self, game_settings):
        """
        Starts a new Texas Hold'em game with the provided settings.

        Args:
            game_settings (GameSettings): The settings for the new game.
        """
        self.current_game = TexasHoldemGame(game_settings)
        self.current_game.run()

    def createTable(self, game_settings):
        """
        Creates and manages multiple Texas Hold'em games at the table.

        Args:
            game_settings (GameSettings): The initial settings for the games to be created.
        """
        while True:
            game_settings.dealer = self.dealer
            self.start_new_game(game_settings)
            self.dealer = (self.dealer + 1) % len(game_settings.players)
            if not self.check_input_new_game():
                break

    def check_input_new_game(self):
        """
        Prompts the user to play another game or quit the table.

        Returns:
            bool: True if the user chooses to play another game, False otherwise.
        """
        while True:
            print("Do you want to play another game?")
            print("1. Yes 2. No")
            choice = input(">")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 2:
                    if choice == 1:
                        return True
                    else:
                        return False
                else:
                    print_with_color("Invalid choice.", Color.RED)
            else:
                print_with_color("Invalid choice.", Color.RED)
