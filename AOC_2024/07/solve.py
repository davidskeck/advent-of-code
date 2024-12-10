# Advent of Code 2024
# Day 07

import time
import numpy as np

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
    
    inputs = []
    for line in puzzle_input:
        t_val, eq = line.split(':')
        inputs.append((int(t_val), [int(val) for val in eq[1:].split()]))

    for t_val, digits in inputs:
        total_bits = len(digits) - 1
        total_combinations = pow(2, total_bits)
        for i in range(total_combinations):
            bin_val = format(i, f'0{total_bits}b')
            
            calc_val = digits[0]
            for idx, val in enumerate(digits):
                if idx < len(digits) - 1:
                    if bin_val[idx] == "0":
                        calc_val += digits[idx + 1]
                    else:
                        calc_val *= digits[idx + 1]

            if calc_val == t_val:
                answer += t_val
                break

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    for t_val, digits in inputs:
        total_trits = len(digits) - 1
        total_combinations = pow(3, total_trits)
        for i in range(total_combinations):
            tern_val = np.base_repr(i, base=3).zfill(total_trits)
            
            calc_val = digits[0]
            for idx, val in enumerate(digits):
                if idx < len(digits) - 1:
                    if tern_val[idx] == "0":
                        calc_val += digits[idx + 1]
                    elif tern_val[idx] == "1":
                        calc_val *= digits[idx + 1]
                    else:
                        calc_val = int(str(calc_val) + str(digits[idx + 1]))
                if calc_val > t_val:
                    break

            if calc_val == t_val:
                answer += t_val
                break

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
