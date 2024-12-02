# Advent of Code 2024
# Day 1

import time
from collections import Counter

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    ids_one = []
    ids_two = [] 
    for line in puzzle_input:
        one, two = line.split()
        ids_one.append(int(one))
        ids_two.append(int(two))
    ids_one.sort()
    ids_two.sort()

    for idx, loc_id in enumerate(ids_one):
        answer += abs(loc_id - ids_two[idx])

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    count_values = Counter(ids_two)
    for loc_id in ids_one:
        answer += loc_id * count_values[loc_id]

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
