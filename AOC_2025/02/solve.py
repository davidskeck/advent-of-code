# Advent of Code 2025
# Day 02

import re
import time

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
    ranges = []
    
    for line in puzzle_input:
        ranges_in = line.split(',')
        for range_in in ranges_in:
            ranges.append(range_in.split('-'))
    
    pattern = re.compile(R"([0-9]+)\1")
    for curr_range in ranges:
        start, end = curr_range
        for i in range(int(start), int(end) + 1):
            if len(str(i)) % 2 != 0:
                continue
            match = pattern.match(str(i))
            if match:
                match = match.group()
                if len(match) == len(str(i)):
                    answer += int(match)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    
    greedy_pattern = re.compile(R"([0-9]+)\1+")
    lazy_pattern = re.compile(R"([0-9]+?)\1+")
    patterns = [greedy_pattern, lazy_pattern]
    for curr_range in ranges:
        start, end = curr_range
        for i in range(int(start), int(end) + 1):
            for pattern in patterns:
                match = pattern.match(str(i))
                if match:
                    match = match.group()
                    if len(match) == len(str(i)):
                        answer += int(match)
                        break

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
