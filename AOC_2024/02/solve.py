# Advent of Code 2024
# Day 2

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
    
    lines = []
    for line in puzzle_input:
        line = [int(val) for val in line.split()]
        lines.append(line)
    
    for line in lines:
        valid = True
        decrease = False
        length = len(line)
        for idx, val in enumerate(line):
            if idx < length - 1:
                diff = val - line[idx + 1]
                if idx == 0 and diff < 0:
                    decrease = True
                if idx > 0:
                    if decrease:
                        if diff > 0:
                            valid = False
                            break
                    else:
                        if diff < 0:
                            valid = False
                            break
                abs_diff = abs(diff)
                if abs_diff == 0 or abs_diff > 3:
                    valid = False
                    break
        if valid:
            answer += 1     

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    checkable_lines = []
    for line in lines:
        extra_lines = []
        for i in range(len(line)):
            extra_lines.append(line[:i] + line[i + 1:])
        checkable_lines.append(extra_lines)

    for lines in checkable_lines:
        for line in lines:
            valid = True
            decrease = False
            length = len(line)
            for idx, val in enumerate(line):
                if idx < length - 1:
                    diff = val - line[idx + 1]
                    if idx == 0 and diff < 0:
                        decrease = True
                    if idx > 0:
                        if decrease:
                            if diff > 0:
                                valid = False
                                break
                        else:
                            if diff < 0:
                                valid = False
                                break
                    abs_diff = abs(diff)
                    if abs_diff == 0 or abs_diff > 3:
                        valid = False
                        break
            if valid:
                answer += 1
                break

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
