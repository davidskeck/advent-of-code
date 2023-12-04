# Advent of Code 2023
# Day 04

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

class ScratchCard:
    def __init__(self, card_str):
        self.number = int(card_str.split()[1].strip(":"))
        self.winning_numbers = [int(number) for number in card_str.split(":")[1].split("|")[0].split()]
        self.my_numbers = [int(number) for number in card_str.split("|")[1].split()]
        self.num_winning_numbers = 0
        for number in self.my_numbers:
            if number in self.winning_numbers:
                self.num_winning_numbers += 1

        self.worth = 0
        if self.num_winning_numbers > 0:
            self.worth = 1
            for i in range(self.num_winning_numbers-1):
                self.worth *= 2
        
        self.cards_won = [self.number + i for i in range(1, self.num_winning_numbers + 1)]

def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    scratch_cards = []
    for line in puzzle_input:
        scratch_cards.append(ScratchCard(line))
    
    for card in scratch_cards:
        answer += card.worth
    
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    card_copies = []
    for card in scratch_cards:
        for card_num in card.cards_won:
            card_copies.append(scratch_cards[card_num - 1])

    for card in card_copies:
        for card_num in card.cards_won:
            card_copies.append(scratch_cards[card_num - 1])
    
    answer = len(scratch_cards) + len(card_copies)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
