# Advent of Code 2022
# Day 4

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = puzzle_data.read().split('\n')

    # Part One
    answer = 0
    elf_assignments = []
    full_elf_assignments = []
    for assignment_pair in puzzle_input:
        if assignment_pair == '':
            continue
        current_elf = []
        full_elf = []
        for pair in assignment_pair.split(','):
            start, end = tuple(pair.split('-'))
            current_elf.append((int(start), int(end)))
            full_pair = []
            for i in range(int(start), int(end) + 1):
                full_pair.append(i)
            full_elf.append(full_pair)
        elf_assignments.append(current_elf)
        full_elf_assignments.append(full_elf)

    for elf in elf_assignments:
        first_pair, second_pair = tuple(elf)
        if (first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[1]) or (second_pair[0] <= first_pair[0] and second_pair[1] >= first_pair[1]):
            answer += 1

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    for elf in full_elf_assignments:
        first_pair, second_pair = tuple(elf)
        for pos in first_pair:
            if pos in second_pair:
                answer += 1
                break

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
