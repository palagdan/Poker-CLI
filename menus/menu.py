import os

from models.account import Account
from utils.color import Color, print_with_color
from models.player import HumanPlayer


class Menu:
    """
    A base class for menus in the poker game application.

    Attributes:
        app (Application): The main application instance.

    Methods:
        display_menu(): Displays the menu to the user.
        check_input(): Checks and processes the user's input.
    """

    def __init__(self, app):
        """
        Initializes the Menu instance.

        Args:
            app (Application): The main application instance.
        """
        self.app = app


class MainMenu(Menu):
    """
    A class representing the main menu of the poker game application.

    Inherits from:
        Menu

    Methods:
        display_menu(): Displays the main menu to the user.
        check_input(): Checks and processes the user's input for the main menu.
    """

    def __init__(self, app):
        """
        Initializes the MainMenu instance.

        Args:
            app (Application): The main application instance.
        """
        Menu.__init__(self, app)

    def display_menu(self):
        """
        Displays the main menu to the user.
        """
        print_with_color("\u2660Welcome to Poker Game ", Color.GREEN, end='')
        print_with_color(self.app.curr_account.username, Color.RED, end='')
        print_with_color(" !\u2661", Color.GREEN)
        print()
        print_with_color("Your Profile: ", Color.YELLOW)
        print_with_color("==================================", Color.DARK_GRAY)
        print("Username: ", end='')
        print_with_color(f"{self.app.curr_account.username}", Color.MAGENTA)
        print("Chips: ", end='')
        print_with_color(f"{self.app.curr_account.chips}", Color.MAGENTA)
        print_with_color("==================================", Color.DARK_GRAY)
        print()
        print("1. Start New Game")
        print("2. Quit")

    def check_input(self):
        """
        Checks and processes the user's input for the main menu.
        """
        while True:
            choice = input("> ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    self.app.curr_menu = self.app.game_settings_menu
                    break
                elif choice == 2:
                    self.app.exit()
                    break
                else:
                    print_with_color("Invalid choice. Please enter a number between 1 and 2.", Color.RED)
            else:
                print_with_color("Invalid choice. Please enter a number between 1 and 2.", Color.RED)
