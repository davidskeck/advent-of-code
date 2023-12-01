# Advent of Code <year>
# Day <day>

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = 0


    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    #answer = 0


    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
