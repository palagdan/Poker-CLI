from menus.menu import Menu
from utils.color import print_with_color, Color


class GameSettingsMenu(Menu):
    """
    A class representing the game settings menu of the poker game application.

    Inherits from:
        Menu

    Methods:
        display_menu(): Displays the game settings menu to the user.
        check_input(): Checks and processes the user's input for the game settings menu.
        set_players(): Allows the user to set the number of players for the game.
    """

    def __init__(self, app):
        """
        Initializes the GameSettingsMenu instance.

        Args:
            app (Application): The main application instance.
        """
        Menu.__init__(self, app)

    def display_menu(self):
        """
        Displays the game settings menu to the user.
        """
        print_with_color("Game Settings Menu:", Color.GREEN)

        print_with_color("==================================", Color.DARK_GRAY)
        print(Color.BLUE.value + "Number of players: " + Color.RED.value + str(
            self.app.players_number) + Color.RESET.value)
        print_with_color("==================================", Color.DARK_GRAY)
        print()
        print("1. Start the game")
        print("2. Change number of players")
        print("3. Back to Main Menu")

    def check_input(self):
        """
        Checks and processes the user's input for the game settings menu.
        """
        while True:
            choice = input("> ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    self.app.curr_menu = self.app.main_menu
                    self.app.playing = True
                    break
                elif choice == 2:
                    self.set_players()
                    break
                elif choice == 3:
                    self.app.curr_menu = self.app.main_menu
                    break
                else:
                    print_with_color("Invalid choice. Please enter a number between 1 and 3.", Color.RED)
            else:
                print_with_color("Invalid choice. Please enter a number between 1 and 3.", Color.RED)

    def set_players(self):
        """
        Allows the user to set the number of players for the game.
        """
        print_with_color("Enter number of players(2 - 8)", Color.GREEN)
        while True:
            choice = input("> ")
            if choice.isdigit():
                choice = int(choice)
                if 2 <= choice <= 8:
                    self.app.players_number = choice
                    break
                else:
                    print_with_color("Invalid number of players. Please enter a number between 2 and 8.", Color.RED)
            else:
                print_with_color("Invalid number of players. Please enter a number between 2 and 8.", Color.RED)
