import json
import random
from cfonts import render, say
from menus.game_settings_menu import GameSettingsMenu
from menus.menu import *
from game.table import Table
from menus.starting_menu import StartingMenu
from models.account import Account
from models.deck import Deck, StandardDeck
from settings import GameSettings
from models.player import ComputerPlayer, HumanPlayer


class Application:
    """
        A class representing the main application for a poker game.

        Attributes:
            running (bool): Indicates whether the application is currently running.
            playing (bool): Indicates whether a game is currently being played.
            starting_menu (StartingMenu): The starting menu of the application.
            main_menu (MainMenu): The main menu of the application.
            game_settings_menu (GameSettingsMenu): The game settings menu of the application.
            curr_menu (Menu): The current menu being displayed in the application.
            config (dict): The configuration data loaded from the accounts JSON file.
            accounts (list): The list of accounts loaded from the configuration data.
            players_number (int): The number of players in the game.
            deck (Deck): The deck of cards used in the game.
            chips_amount (int): The initial amount of chips each player has.
            small_blind (int): The amount of the small blind in the game.
            curr_account (Account): The current account logged into the application.

        Methods:
            read_config(file_path): Reads the configuration data from the specified JSON file.
            write_to_config(file_path, data): Writes the given data to the specified JSON file.
            game_loop(): Runs the main game loop, creating a table and starting a new game if applicable.
            run(): Runs the application, displaying menus and handling user input.
            exit(): Exits the application, saving any changes to the accounts JSON file.
        """
    def __init__(self):
        self.running = True
        self.playing = False

        self.starting_menu = StartingMenu(self)
        self.main_menu = MainMenu(self)
        self.game_settings_menu = GameSettingsMenu(self)
        self.curr_menu = self.starting_menu

        self.config = self.read_config("config_files/accounts.json")
        self.accounts = self.config["accounts"]

        self.players_number = 2
        self.deck = StandardDeck()
        self.chips_amount = 100
        self.small_blind = 1
        self.curr_account = None

    @staticmethod
    def read_config(file_path):
        """
        Reads the configuration data from the specified JSON file.

        Args:
            file_path (str): The path to the JSON file containing the configuration data.

        Returns:
            dict: The configuration data loaded from the file.
        """
        with open(file_path, 'r') as file:
            config_data = json.load(file)
        return config_data

    @staticmethod
    def write_to_config(file_path, data):
        """
        Writes the given data to the specified JSON file.

        Args:
            file_path (str): The path to the JSON file to write the data to.
            data (dict): The data to write to the file.
        """
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def game_loop(self):
        """
        Runs the main game loop, creating a table and starting a new game if applicable.
        """
        if self.playing:
            table = Table()

            players = [ComputerPlayer(Account(username="BOT-" + str(i), chips=self.chips_amount)) for i in
                       range(self.players_number - 1)]
            players.append(HumanPlayer(self.curr_account))
            random.shuffle(players)
            game_settings = GameSettings(players=players, deck=self.deck, dealer=0, small_blind=self.small_blind,
                                         big_blind=self.small_blind * 2)
            table.createTable(game_settings)

    def run(self):
        """
        Runs the application, displaying menus and handling user input.
        """
        while self.running:
            print(100 * "\n")
            #  self.printBanner()
            output = render('POKER CLI', colors=['green', 'yellow'], align='center')
            print(output)
            self.curr_menu.display_menu()
            self.curr_menu.check_input()
            self.game_loop()
            self.playing = False

    def exit(self):
        """
        Exits the application, saving any changes to the accounts JSON file.
        """
        self.running = False
        self.curr_menu = None
        for account in self.config["accounts"]:
            if account["username"] == self.curr_account.username:
                account["chips"] = self.curr_account.chips

        self.write_to_config("config_files/accounts.json", self.config)