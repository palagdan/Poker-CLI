
from dataclasses import dataclass
from utils.TexasHoldemCombinations import HandChecker
from utils.color import Color, print_with_color
from models.account import Account


@dataclass
class Player:
    """
      Represents a player in a poker game.

      Attributes:
          account (Account): The player's account.
          hole_cards (list): The player's hole cards.
          active (bool): Whether the player is active in the game.
    """
    account: Account
    hole_cards = []
    active = True

    def choose_action(self, game):
        """
                Chooses an action for the player in the game.

                Args:
                    game (TexasHoldemGame): The current Texas Hold'em game instance.
        """
        if self.account.chips == 0:
            return
        last_player_bet = game.players[(game.last_state_player_index + 1) % len(game.players)]

        if game.players_bet[last_player_bet.account.username] > game.players_bet[self.account.username]:
            diff = game.players_bet[last_player_bet.account.username] - game.players_bet[self.account.username]
            if diff < 0:
                self.to_call_all_in(game)
            else:
                self.to_call_or_raise(game, diff)

        else:
            # without Call. Check, Raise, Fold impl
            self.to_check_raise(game)

    def to_call_all_in(self, game):
        """
                Implements the action for the player to call all-in.

                Args:
                    game (TexasHoldemGame): The current Texas Hold'em game instance.
        """
        pass

    def to_call_or_raise(self, game, diff):
        """
               Implements the action for the player to call or raise.

               Args:
                   game (TexasHoldemGame): The current Texas Hold'em game instance.
                   diff (int): The difference between the current bet and the previous bet.
        """
        pass

    def to_check_raise(self, game):
        """
                Implements the action for the player to check or raise.

                Args:
                    game (TexasHoldemGame): The current Texas Hold'em game instance.
        """
        pass


@dataclass
class ComputerPlayer(Player):
    """
      Represents a computer-controlled player in a poker game.

      Inherits from:
          Player
      """

    def to_call_all_in(self, game):
        hand_strength = HandChecker.calculate_hand_strength(self.hole_cards, game.community_cards)

        if hand_strength > 0.5:
            game.make_call(self)
        else:
            game.make_fold(self)

    def to_call_or_raise(self, game, diff):
        hand_strength = HandChecker.calculate_hand_strength(self.hole_cards, game.community_cards)
        if hand_strength > 0.4:
            amount = min(self.account.chips, 5)
            game.make_raise(self, amount)
        elif hand_strength > 0.2:
            game.make_call(self)
        else:
            game.make_fold(self)

    def to_check_raise(self, game):
        hand_strength = HandChecker.calculate_hand_strength(self.hole_cards, game.community_cards)
        if hand_strength > 0.4:
            # 10% from game pot
            amount = min(self.account.chips, 5)
            game.make_raise(self, amount)
        else:
            game.make_check(self)


@dataclass
class HumanPlayer(Player):
    """
      Represents a human player in a poker game.

      Inherits from:
          Player
    """
    def to_call_all_in(self, game):
        while True:
            print(f'Choose the action: 1. All-In {self.account.chips} 2. Fold')
            choice = input(">")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 2:
                    if choice == 1:
                        game.make_call(self)
                        break
                    else:
                        game.make_fold(self)
                        break
                else:
                    print_with_color("Invalid choice.", Color.RED)
            else:
                print_with_color("Invalid choice.", Color.RED)

    def to_call_or_raise(self, game, diff):
        while True:
            print(f'Choose the action: 1. Call ({diff}) 2. Raise 3. Fold')
            choice = input(">")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 3:
                    if choice == 1:
                        if game.make_call(self):
                            break
                        else:
                            print_with_color("Invalid Call.", Color.RED)
                    elif choice == 2:
                        # players.chips - raise
                        # game.players_bet[game.current_player] += raise
                        # game.last_round_player = game.current_player
                        while True:
                            choice = input("Amount: ")
                            if choice.isdigit():
                                choice = int(choice)
                                if choice < self.account.chips or choice < diff:
                                    if game.make_raise(self, choice):
                                        return
                                    else:
                                        print_with_color("Invalid Raise.", Color.RED)
                                else:
                                    print_with_color(
                                        "You don't have enough chips or the raise is less than call", Color.RED)
                            else:
                                print_with_color(
                                    "Invalid amount.", Color.RED)

                    else:
                        # curr_game_settings.players.remove(current_player)
                        game.make_fold(self)
                        break
                else:
                    print_with_color("Invalid choice", Color.RED)
            else:
                print_with_color("Invalid choice.", Color.RED)

    def to_check_raise(self, game):
        while True:
            print(f'Choose the action: 1. Check  2. Bet 3. Fold')
            choice = input(">")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 3:
                    if choice == 1:
                        game.make_check(self)
                        break
                    elif choice == 2:
                        while True:
                            choice = input("Amount: ")
                            if choice.isdigit():
                                choice = int(choice)
                                if choice < self.account.chips:
                                    if game.make_bet(self, choice):
                                        return
                                    else:
                                        print_with_color(
                                            "Invalid Bet", Color.RED)
                                else:
                                    print_with_color(
                                        "You don't have enough chips", Color.RED)
                            else:
                                print_with_color(
                                    "Invalid amount.", Color.RED)

                    else:
                        # curr_game_settings.players.remove(current_player)
                        game.make_fold(self)
                        break
                else:
                    print_with_color("Invalid choice.", Color.RED)
            else:
                print_with_color("Invalid choice", Color.RED)
