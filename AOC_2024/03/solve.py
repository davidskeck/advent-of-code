# Advent of Code 2024
# Day 3

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
    
    valid_muls = []
    for line in puzzle_input:
        valid_muls = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
        for mul in valid_muls:
            values = [int(val) for val in mul[4:-1].split(',')]
            answer += values[0] * values[1]

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    operators = []
    operation_ok = True
    for line in puzzle_input:
        operators = re.findall(r"mul\([0-9]+,[0-9]+\)|don\'t\(\)|do\(\)", line)
        for operator in operators:
            if "mul" in operator and operation_ok:
                values = [int(val) for val in operator[4:-1].split(',')]
                answer += values[0] * values[1]
            elif "don't()" in operator:
                operation_ok = False
            elif "do()" in operator:
                operation_ok = True

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
