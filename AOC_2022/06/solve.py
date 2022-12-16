# Advent of Code 2022
# Day 6

import time

from collections import Counter
import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def find_marker(puzzle_input, marker_size):
    current_chars = []
    for char_index in range(len(puzzle_input[0]) - marker_size):
        current_chars = puzzle_input[0][char_index: char_index + marker_size]
        is_unique = False
        for letter, count in Counter(current_chars).items():
            if count > 1:
                is_unique = False
                break
            else:
                is_unique = True

        if is_unique:
            answer = char_index + marker_size
            break

    return answer


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = find_marker(puzzle_input, 4)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = find_marker(puzzle_input, 14)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
