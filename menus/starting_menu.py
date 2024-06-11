from cfonts import render
from menus.menu import Menu
from models.account import Account
from utils.color import print_with_color, Color

class StartingMenu(Menu):
    """
    A class representing the starting menu of the poker game application.

    Inherits from:
        Menu

    Methods:
        display_menu(): Displays the starting menu to the user.
        check_input(): Checks and processes the user's input for the starting menu.
        create_account(): Creates a new user account based on user input.
    """

    def __init__(self, app):
        """
        Initializes the StartingMenu instance.

        Args:
            app (Application): The main application instance.
        """
        Menu.__init__(self, app)

    def display_menu(self):
        """
        Displays the starting menu to the user.
        """
        print_with_color("Choose your account or create a new one:", Color.GREEN)
        for index, account in enumerate(self.app.accounts, start=1):
            print(str(index) + ". Username: " + Color.CYAN.value + account["username"]
                  + Color.RESET.value + "\n   Chips: " + Color.CYAN.value + str(account["chips"]) + Color.RESET.value)
        print_with_color(str(len(self.app.accounts) + 1) + ". Create New Account", Color.YELLOW)

    def check_input(self):
        """
        Checks and processes the user's input for the starting menu.
        """
        while True:
            choice = input("> ")
            if choice.isdigit():
                choice = int(choice)
                if choice == len(self.app.accounts) + 1:
                    self.create_account()
                    break
                else:
                    try:
                        self.app.curr_account = Account(
                            username=self.app.accounts[choice - 1]["username"],
                            chips=self.app.accounts[choice - 1]["chips"])
                        self.app.curr_menu = self.app.main_menu
                        break
                    except Exception:
                        print_with_color("Invalid choice. Please select an account or create a new.", Color.RED)
            else:
                print_with_color("Invalid choice. Please select an account or create a new.", Color.RED)

    def create_account(self):
        """
        Creates a new user account based on user input.
        """
        username = None

        while True:
            username = input("Username: ")
            used = False
            for account in self.app.accounts:
                if username == account["username"]:
                    print_with_color("User with this username already exists!", Color.RED)
                    used = True
            if not used:
                break

            used = False

        account = {
            "username": username,
            "chips": 100
        }
        self.app.config["accounts"].append(account)
        self.app.accounts = self.app.config["accounts"]
        self.app.write_to_config("config_files/accounts.json", self.app.config)
