# Advent of Code 2021
# Day 1

import os


def main():
    with open(f"input{os.sep}day01.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().split()
    
    previous_depth = None
    total_changes = 0
    for current_depth in puzzle_input:
        if previous_depth is not None:
            if int(current_depth) > int(previous_depth):
                total_changes += 1
        
        previous_depth = current_depth

    print(f"The number of times the depth increases is {total_changes}.")
    
    total_sum_changes = 0
    for i in range(len(puzzle_input) - 3):
        if int(puzzle_input[i]) < int(puzzle_input[i+3]):
            total_sum_changes += 1

    print(f"The number of times the moving sum changes is {total_sum_changes}.")

if __name__ == "__main__":
    main()

