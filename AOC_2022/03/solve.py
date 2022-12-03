# Advent of Code 2022
# Day 3

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = puzzle_data.read().split('\n')

    answer = 0

    # Part One


    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two


    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for file in input_files:
        main(file)
