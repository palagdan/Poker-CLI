import copy
import os
import time

from utils.TexasHoldemStates import TexasHoldemState
from utils.color import print_with_color
from utils.color import Color
from models.player import HumanPlayer
from utils.TexasHoldemCombinations import HandChecker


class Game:
    """
       Base class for all poker games.
    """


class TexasHoldemGame(Game):
    """
        Class representing a Texas Hold'em game.

        Attributes:
            players (list): A list of Player objects representing the players in the game.
            active_players (int): The number of active players in the game.
            curr_game_settings: The settings for the current game.
            running (bool): Flag indicating whether the game is running.
            state (TexasHoldemState): The current state of the game.
            pot (int): The total amount of chips in the pot.
            community_cards (list): A list of Card objects representing the community cards.
            players_bet (dict): A dictionary storing the bets made by each player.
            last_state_player_index (int): The index of the last player to take action in the current state.
            current_player_index (int): The index of the current player taking action.

        Methods:
            deal_preflop(): Deals the preflop round of Texas Hold'em.
            deal_round(): Deals a round of betting.
            deal_community_cards(): Deals the community cards for the current state.
            make_raise(player, amount): Makes a raise bet for the specified player.
            make_bet(player, amount): Makes a bet for the specified player.
            make_check(player): Makes a check action for the specified player.
            make_call(player): Makes a call action for the specified player.
            make_fold(player): Makes a fold action for the specified player.
            collect_blind(player_position, blind_amount): Collects blinds from players.
            run(): Runs the Texas Hold'em game.
            next_state(): Moves the game to the next state.
            display_table(): Displays the current state of the table.
            display_combination(cards): Displays the best hand combination for the given cards.
            display_cards(cards): Displays the cards.
            display_hole_cards(): Displays the hole cards for the human player.
            display_human_player(): Displays the hole cards and best hand combination for the human player.
            determine_winner(): Determines the winner(s) of the game.
            deal_showdown(): Deals with the showdown phase of the game.
    """

    def __init__(self, game_settings):
        """
               Initializes a TexasHoldemGame instance with the specified game settings.

               Args:
                   game_settings: The settings for the current game.
        """
        self.players = game_settings.players[:]
        self.active_players = len(self.players)

        self.curr_game_settings = copy.deepcopy(game_settings)

        self.running = False
        self.state = TexasHoldemState.PREFLOP

        self.pot = 0

        self.community_cards = []

        self.players_bet = {}
        for player in self.players:
            self.players_bet[player.account.username] = 0
            player.active = True

        self.last_state_player_index = None
        self.current_player_index = 0

    def deal_preflop(self):
        """
              Deals the preflop round of Texas Hold'em.

              This method deals hole cards to players, collects blinds, and initiates the first round of betting.
        """
        for player in self.players:
            player.hole_cards = [self.curr_game_settings.deck.deal_card() for _ in range(2)]

        small_blind_player = (self.curr_game_settings.dealer + 1) % len(self.players)
        big_blind_player = (self.curr_game_settings.dealer + 2) % len(self.players)
        self.display_table()
        self.collect_blind(small_blind_player, self.curr_game_settings.small_blind)
        self.collect_blind(big_blind_player, self.curr_game_settings.big_blind)

        self.current_player_index = (big_blind_player + 1) % len(self.players)
        self.last_state_player_index = small_blind_player

        self.deal_round()

        if self.active_players == 1:
            self.determine_winner()
            self.state = TexasHoldemState.END
        else:
            self.next_state()

    def deal_round(self):
        """
               Deals a round of betting.

               This method allows each active player to take action (bet, raise, call, check, or fold) in turn.
        """
        while True:
            current_player = self.players[self.current_player_index]
            if current_player.active:
                current_player.choose_action(self)
            if self.current_player_index == self.last_state_player_index:
                break
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def deal_community_cards(self):
        """
                Deals the community cards for the current state.

                This method deals community cards based on the current game state (flop, turn, or river).
        """
        self.current_player_index = (self.curr_game_settings.dealer + 1) % len(self.players)
        self.last_state_player_index = self.curr_game_settings.dealer

        if self.state == TexasHoldemState.FLOP:
            for _ in range(3):
                self.community_cards.append(self.curr_game_settings.deck.deal_card())
        else:
            self.community_cards.append(self.curr_game_settings.deck.deal_card())

        self.display_table()

        self.deal_round()
        if self.active_players == 1:
            self.determine_winner()
            self.state = TexasHoldemState.END
        else:
            self.next_state()

    def make_raise(self, player, amount):
        """
             Makes a raise bet for the specified player.

            Args:
                player: The player making the raise bet.
                amount: The amount of chips to raise by.

             Returns:
                bool: True if the raise is successful, False otherwise.
        """
        last_player_bet = self.players[(self.last_state_player_index + 1) % len(self.players)]
        diff = self.players_bet[last_player_bet.account.username] - self.players_bet[player.account.username]
        if diff < amount <= player.account.chips:
            player.account.chips -= amount
            self.players_bet[player.account.username] += amount
            self.pot += amount
            self.last_state_player_index = (self.current_player_index - 1) % len(self.players)
            print_with_color(f'{player.account.username} raised {amount}', Color.MAGENTA)
        else:
            return False
        return True

    def make_bet(self, player, amount):
        """
               Makes a bet for the specified player.

               Args:
                   player: The player making the bet.
                   amount: The amount of chips to bet.

               Returns:
                   bool: True if the bet is successful, False otherwise.
        """
        if player.account.chips > amount:
            player.account.chips -= amount
            self.players_bet[player.account.username] += amount
            self.pot += amount
            self.last_state_player_index = (self.current_player_index - 1) % len(self.players)
            print_with_color(f'{player.account.username} bet {amount}', Color.MAGENTA)
        else:
            return False
        return True

    def make_check(self, player):
        """
               Makes a check action for the specified player.

               Args:
                   player: The player making the check action.
        """
        print_with_color(f'{player.account.username} checked', Color.MAGENTA)

    def make_call(self, player):
        """
                Makes a call action for the specified player.

                Args:
                    player: The player making the call action.

                Returns:
                    bool: True if the call is successful, False otherwise.
        """
        last_player_bet = self.players[(self.last_state_player_index + 1) % len(self.players)]
        diff = self.players_bet[last_player_bet.account.username] - self.players_bet[player.account.username]
        if diff <= player.account.chips:
            player.account.chips -= diff
            self.players_bet[player.account.username] += diff
            self.pot += diff
            print_with_color(f'{player.account.username} called {diff}', Color.MAGENTA)
        else:
            self.players_bet[player.account.username] += player.account.chips
            self.pot += player.account.chips
            print_with_color(f'{player.account.username} all-in {player.account.chips}', Color.MAGENTA)
            player.account.chips = 0
        return True

    def make_fold(self, player):
        """
               Makes a fold action for the specified player.

               Args:
                   player: The player making the fold action.
        """
        print_with_color(f'{player.account.username} folded', Color.MAGENTA)
        player.active = False
        self.active_players -= 1

    def collect_blind(self, player_position, blind_amount):
        """
                Collects blinds from players.

                Args:
                    player_position: The position of the player paying the blind.
                    blind_amount: The amount of chips for the blind.
        """
        player = self.players[player_position]
        if player.account.chips >= blind_amount:
            player.account.chips -= blind_amount
            self.players_bet[player.account.username] += blind_amount
            self.pot += blind_amount
            print_with_color(f'{player.account.username} paid blind {blind_amount}', Color.MAGENTA)
        else:
            player.active = False

    def run(self):
        """
               Runs the Texas Hold'em game.

               This method controls the flow of the game, including dealing cards, managing betting rounds,
               and determining the winner(s).
        """
        self.curr_game_settings.deck.shuffle()
        while self.state != TexasHoldemState.END:
            print(5 * '\n')
            time.sleep(0.5)
            if self.state == TexasHoldemState.PREFLOP:
                self.deal_preflop()
            elif self.state == TexasHoldemState.FLOP:
                self.deal_community_cards()
            elif self.state == TexasHoldemState.TURN:
                self.deal_community_cards()
            elif self.state == TexasHoldemState.RIVER:
                self.deal_community_cards()
            elif self.state == TexasHoldemState.SHOWDOWN:
                self.deal_showdown()
                break
            else:
                break

    def next_state(self):
        """
                Moves the game to the next state.

                This method transitions the game to the next state (preflop, flop, turn, river, or showdown).
        """
        if self.state == TexasHoldemState.PREFLOP:
            self.state = TexasHoldemState.FLOP
        elif self.state == TexasHoldemState.FLOP:
            self.state = TexasHoldemState.TURN
        elif self.state == TexasHoldemState.TURN:
            self.state = TexasHoldemState.RIVER
        elif self.state == TexasHoldemState.RIVER:
            self.state = TexasHoldemState.SHOWDOWN
        elif self.state == TexasHoldemState.SHOWDOWN:
            self.state = TexasHoldemState.END

    def display_table(self):
        """
               Displays the current state of the table.

               This method prints out information about active players, pot size, community cards,
               and the hole cards of the human player.
        """
        print_with_color("Active Players", Color.GREEN)
        print_with_color("==================================", Color.DARK_GRAY)
        for player in self.players:
            if player.active:
                print_with_color(f'{player.account.username}', Color.BRIGHT_MAGENTA)
                print_with_color(f'\tChips: ', Color.WHITE, end='')
                print_with_color(f'{player.account.chips}', Color.GREEN)

        print_with_color("==================================", Color.DARK_GRAY)
        print("Pot: ", end="")
        print_with_color(f"{self.pot}", Color.GREEN)
        if len(self.community_cards) != 0:
            print_with_color("==================================", Color.DARK_GRAY)
            print("Table:")
            self.display_cards(self.community_cards)
            print_with_color("==================================", Color.DARK_GRAY)
        self.display_human_player()

    def display_combination(self, cards):
        """
                Displays the best hand combination for the given cards.

                Args:
                    cards: A list of Card objects representing the player's hand.

                This method calculates and displays the best hand combination for the given cards.
        """
        print_with_color(f'{HandChecker.check_hand(cards + self.community_cards).str} ',
                         Color.GREEN, end="")
        combination = HandChecker.get_combination_cards(cards + self.community_cards)
        print("( ", end='')
        for card in combination:
            print_with_color(f'{card} ', Color.GREEN, end='')
        print(")")

    def display_cards(self, cards):
        """
                Displays the cards.

                Args:
                    cards: A list of Card objects representing the cards to display.

                This method prints out the graphical representation of the cards.
        """
        if len(cards) == 0:
            return
        print((len(cards)) * "==== ")
        for card in cards:
            print(f'|{card}| ', end="")
        print()
        print((len(cards)) * "==== ")

    def display_hole_cards(self):
        """
               Displays the hole cards for the human player.

               This method prints out the hole cards of the human player.
        """
        for player in self.players:
            if isinstance(player, HumanPlayer):
                print_with_color("Your Cards:", Color.YELLOW)
                self.display_cards(player.hole_cards)

    def display_human_player(self):
        """
                Displays the hole cards and best hand combination for the human player.

                This method prints out the hole cards and best hand combination of the human player.
        """
        for player in self.players:
            if isinstance(player, HumanPlayer):
                self.display_hole_cards()
                self.display_combination(player.hole_cards)

    def determine_winner(self):
        """
                Determines the winner(s) of the game.

                This method evaluates the hands of active players and determines the winner(s) based on hand strength.
        """
        winner_rank = None
        winners = []
        winner_hand = None
        for player in self.players:
            if player.active:
                player_hand = player.hole_cards + self.community_cards
                player_rank = HandChecker.check_hand(player_hand).int

                if len(winners) == 0 or player_rank > winner_rank:
                    winners.clear()
                    winners.append(player)
                    winner_rank = player_rank
                    winner_hand = player_hand

                elif winner_rank == player_rank:
                    res = HandChecker.compare_same_combination(winner_hand, player_hand)
                    if res == 1:
                        continue
                    elif res == -1:
                        winners.clear()
                        winners.append(player)
                        winner_rank = player_rank
                        winner_hand = player_hand
                    else:
                        winners.append(player)
        splitted_pot = self.pot // len(winners)

        for winner in winners:
            print_with_color(winner.account.username, Color.MAGENTA, end="")
            print(" won ", end="")
            print_with_color(str(splitted_pot), Color.GREEN, end='')
            print(" with ", end="")
            self.display_combination(winner.hole_cards)
            winner.account.chips += splitted_pot
        print_with_color("Game is over", Color.YELLOW)

    def deal_showdown(self):
        """
               Deals with the showdown phase of the game.

               This method handles the showdown phase, revealing all players' cards and determining the winner(s).
        """
        print_with_color("Showdown", Color.GREEN)
        self.display_cards(self.community_cards)
        for player in self.players:

            if player.active:
                print_with_color(player.account.username, Color.MAGENTA)
                self.display_cards(player.hole_cards)

        self.determine_winner()
