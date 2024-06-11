from collections import Counter
from enum import Enum
from itertools import combinations

from models.deck import Deck


class HandStrength(Enum):
    """
       An enumeration representing the strength of a poker hand.

       Attributes:
           HIGH_CARD (dict): Represents a high card hand.
           PAIR (dict): Represents a pair hand.
           TWO_PAIR (dict): Represents a two pair hand.
           THREE_OF_A_KIND (dict): Represents a three of a kind hand.
           STRAIGHT (dict): Represents a straight hand.
           FLUSH (dict): Represents a flush hand.
           FULL_HOUSE (dict): Represents a full house hand.
           FOUR_OF_A_KIND (dict): Represents a four of a kind hand.
           STRAIGHT_FLUSH (dict): Represents a straight flush hand.

       Methods:
           str: Returns the string representation of the hand strength.
           int: Returns the integer representation of the hand strength.
       """

    HIGH_CARD = {
        "str": "HIGH CARD",
        "int": 0
    }
    PAIR = {
        "str": "PAIR",
        "int": 1
    }
    TWO_PAIR = {
        "str": "TWO PAIRS",
        "int": 2
    }

    THREE_OF_A_KIND = {
        "str": "THREE OF A KIND",
        "int": 3
    }
    STRAIGHT = {
        "str": "STRAIGHT",
        "int": 4
    }
    FLUSH = {
        "str": "FLUSH",
        "int": 5
    }
    FULL_HOUSE = {
        "str": "FULL HOUSE",
        "int": 6
    }
    FOUR_OF_A_KIND = {
        "str": "FOUR OF KIND",
        "int": 7
    }
    STRAIGHT_FLUSH = {
        "str": "STRAIGHT FLUSH",
        "int": 8
    }

    @property
    def str(self):
        return self.value["str"]

    @property
    def int(self):
        return self.value["int"]


class HandChecker:
    """
       A class to check the strength of poker hands.

       Methods:
           hand_strength(hole_cards, community_cards): Calculates the strength of a hand given the hole cards and community cards.
           check_hand(cards): Determines the strength of a given set of cards.
           compare_same_combination(hand1, hand2): Compares two hands with the same combination.
           has_pair(cards): Checks if the given set of cards contains a pair.
           has_two_pair(cards): Checks if the given set of cards contains two pairs.
           has_three_of_a_kind(cards): Checks if the given set of cards contains three of a kind.
           has_straight(cards): Checks if the given set of cards contains a straight.
           has_flush(cards): Checks if the given set of cards contains a flush.
           has_full_house(cards): Checks if the given set of cards contains a full house.
           has_four_of_a_kind(cards): Checks if the given set of cards contains four of a kind.
           has_straight_flush(cards): Checks if the given set of cards contains a straight flush.
       """

    @staticmethod
    def calculate_hand_strength(hole_cards, community_cards):
        """
                Calculates the strength of a hand given the hole cards and community cards.

                Args:
                    hole_cards (list): The hole cards.
                    community_cards (list): The community cards.

                Returns:
                    float: The strength of the hand.
                """
        our_cards = hole_cards + community_cards
        our_rank = HandChecker.check_hand(our_cards).int
        ahead, tied, behind = 0, 0, 0

        deck = Deck()
        all_cards = deck.cards
        remaining_cards = list(filter(lambda x: x not in our_cards, all_cards))

        for opp_cards_tuple in combinations(remaining_cards, 2):
            opp_cards = community_cards + list(opp_cards_tuple)
            opp_rank = HandChecker.check_hand(opp_cards).int
            if our_rank > opp_rank:
                ahead += 1
            elif our_rank < opp_rank:
                behind += 1
            else:
                res = HandChecker.compare_same_combination(our_cards, opp_cards)
                if res == 1:
                    ahead += 1
                elif res == 0:
                    tied += 1
                else:
                    behind += 1

        hand_strength = ((ahead + tied) / 2) / (ahead + tied + behind) if (ahead + tied + behind) != 0 else 0
        return hand_strength

    @staticmethod
    def check_hand(cards):
        """
              Determines the strength of a given set of cards.

              Args:
                  cards (list): The set of cards.

              Returns:
                  HandStrength: The strength of the hand.
              """
        if HandChecker.has_straight_flush(cards):
            return HandStrength.STRAIGHT_FLUSH
        elif HandChecker.has_four_of_a_kind(cards):
            return HandStrength.FOUR_OF_A_KIND
        elif HandChecker.has_full_house(cards):
            return HandStrength.FULL_HOUSE
        elif HandChecker.has_flush(cards):
            return HandStrength.FLUSH
        elif HandChecker.has_straight(cards):
            return HandStrength.STRAIGHT
        elif HandChecker.has_three_of_a_kind(cards):
            return HandStrength.THREE_OF_A_KIND
        elif HandChecker.has_two_pair(cards):
            return HandStrength.TWO_PAIR
        elif HandChecker.has_pair(cards):
            return HandStrength.PAIR
        else:
            return HandStrength.HIGH_CARD

    @staticmethod
    def get_combination_cards(cards):
        """
        Finds the cards involved in the combination from a given set of cards.

        Args:
            cards (list): The set of cards.

        Returns:
            list: The cards involved in the combination.
        """
        if HandChecker.has_straight_flush(cards):
            return HandChecker.get_straight_flush(cards)
        elif HandChecker.has_four_of_a_kind(cards):
            return HandChecker.get_four_of_a_kind(cards)
        elif HandChecker.has_full_house(cards):
            return HandChecker.get_full_house(cards)
        elif HandChecker.has_flush(cards):
            return HandChecker.get_flush(cards)
        elif HandChecker.has_straight(cards):
            return HandChecker.get_straight(cards)
        elif HandChecker.has_three_of_a_kind(cards):
            return HandChecker.get_three_of_a_kind(cards)
        elif HandChecker.has_two_pair(cards):
            return HandChecker.get_two_pair(cards)
        elif HandChecker.has_pair(cards):
            return HandChecker.get_pair(cards)
        else:
            return HandChecker.get_high_card(cards)

    @staticmethod
    def compare_same_combination(hand1, hand2):
        """
        Compares two hands with the same combination.

        Args:
            hand1 (list): The first hand.
            hand2 (list): The second hand.

        Returns:
            int: 1 if hand1 wins, -1 if hand2 wins, 0 if it's a tie.
        """
        hand1 = sorted([card.rank.int for card in hand1], reverse=True)
        hand2 = sorted([card.rank.int for card in hand2], reverse=True)

        for rank1, rank2 in zip(hand1, hand2):
            if rank1 > rank2:
                return 1
            elif rank1 < rank2:
                return -1
        return 0

    @staticmethod
    def get_high_card(cards):
        """
        Retrieves the highest card from a given set of cards.

        Args:
            cards (list): The set of cards.

        Returns:
            Card: The highest card.
        """
        sorted_cards = sorted(cards, key=lambda card: card.rank.int)
        return [sorted_cards[-1]]

    @staticmethod
    def has_pair(cards):
        """
        Checks if the given set of cards contains a pair.

        Args:
            cards (list): The set of cards.

        Returns:
            bool: True if a pair is present, False otherwise.
        """
        rank_counts = Counter(card.rank.int for card in cards)
        return any(counter == 2 for counter in rank_counts.values())

    @staticmethod
    def get_pair(cards):
        """
          Retrieves the cards involved in a pair combination.

          Args:
              cards (list): The set of cards.

          Returns:
              list: The cards involved in the pair combination.
          """
        rank_counts = Counter(card.rank.int for card in cards)
        pair_rank = next(rank for rank, count in rank_counts.items() if count == 2)
        return [card for card in cards if card.rank.int == pair_rank][:2]


    @staticmethod
    def has_two_pair(cards):
        """
        Checks if the given set of cards contains two pairs.

        Args:
            cards (list): The set of cards.

        Returns:
            bool: True if two pairs are present, False otherwise.
        """
        rank_counts = Counter(card.rank.int for card in cards)
        num_pairs = sum(1 for count in rank_counts.values() if count == 2)
        return num_pairs == 2

    @staticmethod
    def get_two_pair(cards):
        """
            Retrieves the cards involved in a two pairs combination.

            Args:
                cards (list): The set of cards.

            Returns:
                list: The cards involved in the two pairs combination.
            """
        rank_counts = Counter(card.rank.int for card in cards)
        pair_ranks = [rank for rank, counter in rank_counts.items() if counter == 2]

        if len(pair_ranks) >= 2:
            pair_rank1, pair_ranks2 = pair_ranks[:2]
            return sorted([card for card in cards if card.rank.int == pair_rank1 or card.rank.int == pair_ranks2])
        return []

    @staticmethod
    def has_three_of_a_kind(cards):
        """
        Checks if the given set of cards contains three of a kind.

        Args:
            cards (list): The set of cards.

        Returns:
            bool: True if three of a kind is present, False otherwise.
        """
        rank_counts = Counter(card.rank.int for card in cards)
        return any(counter == 3 for counter in rank_counts.values())

    @staticmethod
    def get_three_of_a_kind(cards):
        """
        Retrieves the cards involved in a three of a kind combination from a given set of cards.

        Args:
            cards (list): The set of cards.

        Returns:
            list: The cards involved in the three of a kind combination.
        """
        rank_counts = Counter(card.rank.int for card in cards)
        three_kind_rank = next(rank for rank, count in rank_counts.items() if count == 3)
        return sorted([card for card in cards if card.rank.int == three_kind_rank][0:3])

    @staticmethod
    def has_straight(cards):
        """
        Checks if the given set of cards contains a straight.

        Args:
            cards (list): The set of cards.

        Returns:
            bool: True if a straight is present, False otherwise.
        """
        # Sort the cards by rank
        sorted_cards = sorted(cards, key=lambda card: card.rank.int)

        # Iterate through the sorted cards to find sequences of consecutive ranks
        for i in range(len(sorted_cards) - 4):
            # Check if the ranks of five consecutive cards form a sequence
            if all(sorted_cards[i + j].rank.int - sorted_cards[i + j - 1].rank.int == 1 for j in range(1, 5)):
                return True  # Found a straight
        return False  # No straight found

    @staticmethod
    def get_straight(cards):
        """
        Retrieves the cards involved in a straight combination from a given set of cards.

        Args:
            cards (list): The set of cards.

        Returns:
            list: The cards involved in the straight combination, if present. Otherwise, an empty list.
        """
        # Sort the cards by rank
        sorted_cards = sorted(cards, key=lambda card: card.rank.int)

        # Iterate through the sorted cards to find sequences of consecutive ranks
        for i in range(len(sorted_cards) - 4):
            # Check if the ranks of five consecutive cards form a sequence
            if all(sorted_cards[i + j].rank.int - sorted_cards[i + j - 1].rank.int == 1 for j in range(1, 5)):
                # If found, return the straight cards
                return sorted(sorted_cards[i:i + 5])

        # If no straight is found, return an empty list
        return []


    @staticmethod
    def has_flush(cards):
        """
        Checks if the given set of cards contains a flush.

        Args:
            cards (list): The set of cards.

        Returns:
            bool: True if a flush is present, False otherwise.
        """
        suit_counts = Counter(card.suit for card in cards)
        return any(count == 5 for count in suit_counts.values())

    @staticmethod
    def get_flush(cards):
        """
        Retrieves the cards involved in a flush combination from a given set of cards.

        Args:
            cards (list): The set of cards.

        Returns:
            list: The cards involved in the flush combination.
        """
        suit_counts = Counter(card.suit for card in cards)
        suit = next(suit for suit, count in suit_counts.items() if count == 5)
        return sorted([card for card in cards if card.suit == suit])

    @staticmethod
    def has_full_house(cards):
        """
        Checks if the given set of cards contains a full house.

        Args:
            cards (list): The set of cards.

        Returns:
            bool: True if a full house is present, False otherwise.
        """
        rank_counts = Counter(card.rank.int for card in cards)
        return any(count == 3 for count in rank_counts.values()) and any(count == 2 for count in rank_counts.values())

    @staticmethod
    def get_full_house(cards):
        """
        Retrieves the cards involved in a full house combination from a given set of cards.

        Args:
            cards (list): The set of cards.

        Returns:
            list: The cards involved in the full house combination, sorted by rank in ascending order.
                  If no full house combination is found, an empty list is returned.
        """
        rank_counts = Counter(card.rank.int for card in cards)
        three_kind_rank = next(rank for rank, count in rank_counts.items() if count == 3)
        pair_rank = next(rank for rank, count in rank_counts.items() if count == 2)
        return sorted([card for card in cards if card.rank.int == three_kind_rank] +
                      [card for card in cards if card.rank.int == pair_rank][:2])

    @staticmethod
    def has_four_of_a_kind(cards):
        """
        Checks if the given set of cards contains four of a kind.

        Args:
            cards (list): The set of cards.

        Returns:
            bool: True if four of a kind is present, False otherwise.
        """
        # Count the occurrences of each rank in the list of cards
        rank_counts = Counter(card.rank.int for card in cards)

        # Check if any rank occurs exactly four times
        return any(count == 4 for count in rank_counts.values())

    @staticmethod
    def get_four_of_a_kind(cards):
        """
                Retrieves the cards involved in a four of a kind combination from a given set of cards.

                Args:
                    cards (list): The set of cards.

                Returns:
                    list: The cards involved in the four of a kind combination.
         """
        rank_counts = Counter(card.rank.int for card in cards)
        four_of_kind_rank = next(rank for rank, count in rank_counts.items() if count == 4)
        return [card for card in cards if card.rank.int == four_of_kind_rank]

    @staticmethod
    def has_straight_flush(cards):
        """
        Checks if the given set of cards contains a straight flush.

        Args:
            cards (list): The set of cards.

        Returns:
            bool: True if a straight flush is present, False otherwise.
        """
        if len(cards) < 5:
            return False

        # Sort the cards by rank in descending order
        sorted_cards = sorted(cards, key=lambda card: card.rank.int, reverse=True)

        for i in range(len(sorted_cards) - 4):
            # Check if the current card and the next 4 cards form a sequence
            if all(sorted_cards[i].rank.int - j == sorted_cards[i + j].rank.int for j in range(1, 5)):
                # Check if all cards in the sequence have the same suit
                if len(set(card.suit for card in sorted_cards[i:i + 5])) == 1:
                    return True  # Found a straight flush
        return False  # No straight flush found

    @staticmethod
    def get_straight_flush(cards):
        """
        Retrieves the cards involved in a straight flush combination from a given set of cards.

        Args:
            cards (list): The set of cards.

        Returns:
            list: The cards involved in the straight flush combination, if present. Otherwise, an empty list.
        """
        if len(cards) < 5:
            return []

        # Sort the cards by rank in descending order
        sorted_cards = sorted(cards, key=lambda card: card.rank.int)

        for i in range(len(sorted_cards) - 4):
            # Check if the current card and the next 4 cards form a sequence

            if all(sorted_cards[i + j].rank.int - sorted_cards[i + j - 1].rank.int == 1 for j in range(1, 5)):
                # Check if all cards in the sequence have the same suit
                if len(set(card.suit for card in sorted_cards[i:i + 5])) == 1:
                    # Return the straight flush cards
                    return sorted_cards[i:i + 5]

        # If no straight flush is found, return an empty list
        return []

