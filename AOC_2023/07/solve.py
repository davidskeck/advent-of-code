# Advent of Code 2023
# Day 07

import time
from enum import IntEnum
from collections import Counter

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

class HandRanking(IntEnum):
    FIVE_OF_KIND  = 1
    FOUR_OF_KIND  = 2
    FULL_HOUSE    = 3
    THREE_OF_KIND = 4
    TWO_PAIR      = 5
    ONE_PAIR      = 6
    HIGH_CARD     = 7

card_ranking = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13
}


class Hand:
    def __init__(self, input_str):
        self.bet = int(input_str.split()[-1])
        self.cards = input_str.split()[0]

        self.ranking = HandRanking.HIGH_CARD
        card_counts = Counter(self.cards)
        self.joker_count = card_counts.get("J")

        # Just get a count of how many of the same cards were seen 
        # [1: 5] would mean all different cards
        # [2: 2] would mean two pair
        self.cards_consolidated = Counter(card_counts.values())

        if 5 in self.cards_consolidated.keys():
            self.ranking = HandRanking.FIVE_OF_KIND
        elif 4 in self.cards_consolidated.keys():
            self.ranking = HandRanking.FOUR_OF_KIND
        elif 3 in self.cards_consolidated.keys() and 2 in self.cards_consolidated.keys():
            self.ranking = HandRanking.FULL_HOUSE
        elif 3 in self.cards_consolidated.keys():
            self.ranking = HandRanking.THREE_OF_KIND
        elif self.cards_consolidated.get(2) == 2:
            self.ranking = HandRanking.TWO_PAIR
        elif self.cards_consolidated.get(2) == 1:
            self.ranking = HandRanking.ONE_PAIR

        self.card_values = []
        self.calculate_ranking()

    def calculate_ranking(self):
        self.card_values = [int(self.ranking)]
        card_value_list = [card_ranking.get(card) for card in self.cards]
        self.card_values += card_value_list
    
    def calculate_joker_ranking(self):
        if self.joker_count is not None and self.ranking > HandRanking.FIVE_OF_KIND:
            if self.ranking is HandRanking.FOUR_OF_KIND:
                self.ranking = HandRanking.FIVE_OF_KIND
            elif self.ranking is HandRanking.FULL_HOUSE:
                if self.joker_count >= 2:
                    self.ranking = HandRanking.FIVE_OF_KIND
                elif self.joker_count == 1:
                    self.ranking = HandRanking.FOUR_OF_KIND
            elif self.ranking is HandRanking.THREE_OF_KIND:
                if self.joker_count == 3:
                    self.ranking = HandRanking. FOUR_OF_KIND
                elif self.joker_count == 2:
                    self.ranking = HandRanking.FIVE_OF_KIND
                elif self.joker_count == 1:
                    self.ranking = HandRanking.FOUR_OF_KIND
            elif self.ranking is HandRanking.TWO_PAIR:
                if self.joker_count == 2:
                    self.ranking = HandRanking.FOUR_OF_KIND
                else:
                    self.ranking = HandRanking.FULL_HOUSE
            elif self.ranking is HandRanking.ONE_PAIR:
                self.ranking = HandRanking.THREE_OF_KIND
            elif self.ranking is HandRanking.HIGH_CARD:
                self.ranking = HandRanking.ONE_PAIR
        
        card_ranking["J"] = 14
        self.calculate_ranking()
        card_ranking["J"] = 4


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    card_ranking["J"] = 4
    
    hands = []
    for line in puzzle_input:
        hands.append(Hand(line))
    
    hands.sort(key=lambda hand: hand.card_values, reverse=True)
    for index, hand in enumerate(hands):
        answer += (index + 1) * hand.bet

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    for hand in hands:
        hand.calculate_joker_ranking()
    
    hands.sort(key=lambda hand: hand.card_values, reverse=True)
    for index, hand in enumerate(hands):
        answer += (index + 1) * hand.bet

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
