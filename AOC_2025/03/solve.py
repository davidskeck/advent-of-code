# Advent of Code 2025
# Day 03

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
    
    banks = []
    for line in puzzle_input:
        bank = []
        for j in line:
            bank.append(int(j))
        banks.append(bank)
    
    for bank in banks:
        first_largest = max(bank[:-1])
        second_largest = max(bank[bank.index(first_largest) + 1:])
        answer += int(f"{first_largest}{second_largest}")

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    for bank in banks:
        largest_str = ""
        max_voltage_len = 12
        curr_index = 0
        for i in range (max_voltage_len):
            end_index = -(max_voltage_len - 1 - len(largest_str))
            end_index = end_index if end_index !=0 else None 
            curr_bank = bank[curr_index:end_index]
            next_largest = max(curr_bank)
            largest_str += str(next_largest)
            curr_index += curr_bank.index(next_largest) + 1

        answer += int(largest_str)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
