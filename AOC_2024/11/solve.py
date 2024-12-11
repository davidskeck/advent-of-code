# Advent of Code 2024
# Day 11

import time
from collections import Counter

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

def blink(stones):
    updated_stones = []
    for stone in stones:
        if stone == 0:
            updated_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            half_stone = int(len(str_stone) / 2)
            updated_stones.append(int(str_stone[0:half_stone]))
            updated_stones.append(int(str_stone[half_stone:]))
        else:
            updated_stones.append(stone * 2024)
    
    return updated_stones


def blink_efficiently(stone_count):
    updated_stones = Counter()
    for stone, count in stone_count.items():
        if stone == 0:
            updated_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            half_stone = int(len(str_stone) / 2)
            updated_stones[int(str_stone[0:half_stone])] += count
            updated_stones[int(str_stone[half_stone:])] += count
        else:
            new_stone_val = stone * 2024
            updated_stones[new_stone_val] += count
    
    return updated_stones


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    stones = []
    for line in puzzle_input:
        stones = [int(stone) for stone in line.split()]
    
    for i in range(25):
        stones = blink(stones)

    answer = len(stones)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    stone_count = Counter(stones)
    for i in range(50):
        stone_count = blink_efficiently(stone_count)

    answer = sum(stone_count.values())
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
