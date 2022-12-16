# Advent of Code 2022
# Day 1

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = puzzle_data.read().split('\n')  # Interestingly have to split on just the newline here... Otherwise you can't tell when one elf's calorie count ends and another starts.

    # Part One
    answer = 0
    calorie_counts = []
    current_cals = 0
    for input in puzzle_input:
        if input != '':
            current_cals += int(input)
        else:
            calorie_counts.append(current_cals)
            current_cals = 0

    sorted_calories = sorted(calorie_counts)
    answer = sorted_calories[-1]
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = sum(sorted_calories[-3:])
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
