# Advent of Code 2024
# Day 01

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
    
    dial_val = 50
    for line in puzzle_input:
        turn_val = int(line[1:])
        if "R" in line:
            dial_val += turn_val
        else:
            dial_val -= turn_val
        dial_val %= 100
        if dial_val == 0:
            answer += 1

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    dial_val = 50
    for line in puzzle_input:
        was_zero = dial_val == 0
        turn_val = int(line[1:])
        answer += abs(turn_val) // 100
        turn_val %= 100

        if "R" in line:
            dial_val += turn_val
        else:
            dial_val -= turn_val
        
        if (dial_val <= 0 and not was_zero) or dial_val >= 100:
            answer += 1

        dial_val %= 100

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
