# Advent of Code 2021
# Day 7

import os


def calculate_fuel(crabs, desired_position):
    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(crab - desired_position)

    return total_fuel

def recalculate_fuel(crabs, desired_position):
    total_fuel = 0
    for crab in crabs:
        total_fuel += sum(range(abs(crab - desired_position) + 1))

    return total_fuel

def main():
    with open(f"input{os.sep}day07.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().split(',')
    
    crabs = []
    for crab in puzzle_input:
        crabs.append(int(crab))
    
    crabs.sort()
    least_fuel = None
    max_position = crabs[-1]
    min_position = crabs[0]
    for position in range (min_position, max_position):
        fuel = calculate_fuel(crabs, position)
        if least_fuel is None or fuel < least_fuel:
            least_fuel = fuel

    print(f"Part One: {least_fuel}")
    
    least_fuel = None
    max_position = crabs[-1]
    min_position = crabs[0]
    for position in range (min_position, max_position):
        fuel = recalculate_fuel(crabs, position)
        if least_fuel is None or fuel < least_fuel:
            least_fuel = fuel


    print(f"Part Two: {least_fuel}")


if __name__ == "__main__":
    main()

