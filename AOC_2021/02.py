# Advent of Code 2021
# Day 2

import os


def main():
    with open(f"input{os.sep}day02.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().split('\n')
    
    current_depth = 0
    current_horizontal = 0
    for vector in puzzle_input:
        if "forward" in vector:
            current_horizontal += int(vector.split()[1])
        elif "down" in vector:
            current_depth += int(vector.split()[1])
        elif "up" in vector:
            current_depth -= int(vector.split()[1])
        
    print("Part 1:", current_depth * current_horizontal)
    
    current_depth = 0
    current_horizontal = 0
    current_aim = 0 
    for vector in puzzle_input:
        if "forward" in vector:
            current_horizontal += int(vector.split()[1])
            current_depth += current_aim * int(vector.split()[1])
        elif "down" in vector:
            current_aim += int(vector.split()[1])
        elif "up" in vector:
            current_aim -= int(vector.split()[1])

    print("Part 2:", current_depth * current_horizontal)
    

if __name__ == "__main__":
    main()

