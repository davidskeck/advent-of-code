# Advent of Code 2023
# Day 13

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def check_for_smudge(one, two):
    diff_count = 0
    for idx, sym in enumerate(one):
        if sym != two[idx]:
            diff_count += 1
        if diff_count >= 2:
            break
    
    return diff_count == 1


def get_reflections(pattern_data, vertical=False, part_two=False):
    if vertical:
        pattern_data = ["".join(data) for data in list(zip(*pattern_data[::-1]))]

    for i in range(len(pattern_data) // 2 * 2):
        smudge_fixed = False
        curr_first = i
        curr_second = i + 1
        match = True
        while match and curr_first >= 0 and curr_second < len(pattern_data):
            match = pattern_data[curr_first] == pattern_data[curr_second]
            if not match:
                if part_two and not smudge_fixed:
                    smudge_fixed = check_for_smudge(pattern_data[curr_first], pattern_data[curr_second])
                    if smudge_fixed:
                        match = True
            curr_first -= 1
            curr_second += 1
        if match:
            if not part_two:
                return i + 1
            elif smudge_fixed:
                return i + 1


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n')]

    # Part One
    answer = 0
    
    patterns = []
    pattern = []
    for line in puzzle_input:
        if line == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)

    for pattern in patterns:
        this_horizontal = get_reflections(pattern)
        if this_horizontal:
            answer += this_horizontal * 100
        else:
            this_vertical = get_reflections(pattern, vertical=True)
            if this_vertical:
                answer += this_vertical

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    
    for index, pattern in enumerate(patterns):
        this_horizontal = get_reflections(pattern, part_two=True)
        if this_horizontal:
            answer += this_horizontal * 100
        else:
            this_vertical = get_reflections(pattern, vertical=True, part_two=True)
            if this_vertical:
                answer += this_vertical

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
