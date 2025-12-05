# Advent of Code 2025
# Day 05

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

def check_in_range(ranges, ingredient):
    fresh = False

    for currRange in ranges:
        low, high = currRange
        if low <= ingredient <= high:
            fresh = True
            break
    
    return fresh


def consolidate_ranges(ranges):
    lows = sorted([curr[0] for curr in ranges])
    highs = sorted([curr[1] for curr in ranges])
    sorted_ranges = list(zip(lows, highs))

    consolidated_ranges = []
    curr_low, curr_high = sorted_ranges[0]
    for next_low, next_high in sorted_ranges[1:]:
        if next_low <= curr_high:
            curr_high = next_high
        else:
            consolidated_ranges.append((curr_low, curr_high))
            curr_low, curr_high = next_low, next_high
    consolidated_ranges.append((curr_low, curr_high))

    return consolidated_ranges


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    ranges = []
    ingredients = []
    for line in puzzle_input:
        if '-' in line:
            low, high = line.split('-')
            ranges.append((int(low), int(high)))
        else:
            ingredients.append(int(line))
    
    for currId in ingredients:
        if check_in_range(ranges, currId):
            answer += 1

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    
    conRanges = consolidate_ranges(ranges)
    for currRange in conRanges:
        low, high = currRange
        answer += (high - low) + 1

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
