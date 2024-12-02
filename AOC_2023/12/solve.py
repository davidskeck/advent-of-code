# Advent of Code 2023
# Day 12

import time
import re

import pyperclip

input_files = [
    "example.txt",
    # "input.txt"
]

UNKNOWN = "?"
DAMAGED = "#"
OK = "."


class ConditionRecord:
    def __init__(self, record_data):
        self.possible_arrangements = []
        row = record_data.split()[0]
        groups = [int(data) for data in record_data.split()[-1].split(',')]
        unknown_blocks = re.finditer(r'[?]{1,}', row)
        for block in unknown_blocks:
            self.generate_all_possibilities(block)
    
    def generate_all_possibilities(self, block):
        possibilities = []

            



def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0

    records = []
    for line in puzzle_input:
        records.append(ConditionRecord(line))

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
