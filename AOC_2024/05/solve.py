# Advent of Code 2024
# Day 05

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

    update_rules = []
    updates = []
    
    for line in puzzle_input:
        if '|' in line:
            update_rules.append(tuple([int(page) for page in line.split('|')]))
        elif ',' in line:
            updates.append([int(page) for page in line.split(',')])

    incorrect_updates = []
    for update in updates:
        update_valid = True
        for rule in update_rules:
            first, second = rule
            if first in update and second in update:
                if update.index(second) < update.index(first):
                    incorrect_updates.append(update)
                    update_valid = False
                    break
        
        if update_valid:
            answer += update[int(len(update) / 2)]

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    for update in incorrect_updates:
        update_valid = False
        while not update_valid:
            clean_run = True
            for rule in update_rules:
                first, second = rule
                if first in update and second in update:
                    scd_idx = update.index(second)
                    frs_idx = update.index(first)
                    if scd_idx < frs_idx:
                        clean_run = False
                        update = update[:scd_idx] + [first] + update[scd_idx + 1:frs_idx] + [second] + update[frs_idx + 1:]
                        break
            if clean_run:
                update_valid = True

        answer += update[int(len(update) / 2)]

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
