# Advent of Code 2023
# Day 07

import time
from enum import IntEnum
from collections import Counter

import pyperclip

input_files = [
    "example.txt",
    # "input.txt"
]

class HandRanking(IntEnum):
    FIVE_OF_KIND  = 1
    FOUR_OF_KIND  = 2
    FULL_HOUSE    = 3
    THREE_OF_KIND = 4
    TWO_PAIR      = 5
    ONE_PAIR      = 6
    HIGH_CARD     = 7


class Hand:
    def __init__(self, input_str):
        self.bet = int(input_str.split()[-1])
        self.cards = input_str.split()[0]

        self.ranking = HandRanking.HIGH_CARD
        self.card_counts = Counter(self.cards).values()
        self.cards_consolidated = Counter(self.card_counts)

        if 5 in self.card_counts:
            self.ranking = HandRanking.FIVE_OF_KIND
        elif 4 in self.card_counts:
            self.ranking = HandRanking.FOUR_OF_KIND
        elif 3 in self.card_counts and 2 in self.card_counts:
            self.ranking = HandRanking.FULL_HOUSE
        elif 3 in self.card_counts:
            self.ranking = HandRanking.THREE_OF_KIND
        elif self.cards_consolidated.get(2) == 2:
            self.ranking = HandRanking.TWO_PAIR
        elif self.cards_consolidated.get(2) == 1:
            self.ranking = HandRanking.ONE_PAIR


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    hands = []
    for line in puzzle_input:
        hands.append(Hand(line))
    
    hands.sort(key=lambda hand: hand.ranking, reverse=True)
    for index, hand in enumerate(hands):
        answer += (index + 1) * hand.bet


    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    # answer = 0


    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
