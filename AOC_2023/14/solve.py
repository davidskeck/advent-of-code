# Advent of Code 2023
# Day 14

import time
import copy
from enum import Enum

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)

NUM_CYCLES = 1000000000


def roll_given_direction(grid, direction):
    y_dir, x_dir = direction.value
    if direction == Direction.EAST or direction == Direction.WEST:
        grid = ["".join(row) for row in list(zip(*grid[::-1]))]
        y_dir = x_dir

    movement_occurred = True
    while movement_occurred:
        movement_occurred = False
        for index, row in enumerate(grid):
            if (direction == Direction.NORTH or direction == Direction.WEST) and index == 0 or \
            (direction == Direction.SOUTH or direction == Direction.EAST) and index == len(grid) - 1:
                continue
            for pos, rock in enumerate(row):
                if rock == "O":
                    if grid[index + y_dir][pos] == ".":
                        str_list = [char for char in grid[index]]
                        str_list[pos] = "."
                        grid[index] = "".join(str_list)

                        str_list = [char for char in grid[index + y_dir]]
                        str_list[pos] = "O"
                        grid[index + y_dir] = "".join(str_list)
                        movement_occurred = True
    
    if direction == Direction.EAST or direction == Direction.WEST:
        grid = ["".join(row) for row in list(zip(*grid[::-1]))]
        grid = ["".join(row) for row in list(zip(*grid[::-1]))]
        grid = ["".join(row) for row in list(zip(*grid[::-1]))]

    return grid


def roll_all_directions(grid):
    directions = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]
    for direction in directions:
        grid = roll_given_direction(grid, direction)

    return grid


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    grid = puzzle_input.copy()
    updated_grid = roll_given_direction(grid, Direction.NORTH)

    for index, row in enumerate(updated_grid):
        for rock in row:
            if rock == "O":
                answer += len(updated_grid) - index

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    grid = puzzle_input.copy()
    grid_dict = {}
    grid_dict[0] = grid.copy()

    curr_grid = grid
    cycles = 1
    loop_start, loop_length = (0, 0)
    while True:
        curr_grid = roll_all_directions(curr_grid)
        if curr_grid not in grid_dict.values():
            grid_dict[cycles] = curr_grid.copy()
        else:
            for key, value in grid_dict.items():
                if value == curr_grid:
                    loop_start = key
                    loop_length = cycles - key
            break
        cycles += 1

    extra_loops = (NUM_CYCLES - loop_start) % loop_length
    curr_grid = grid_dict[loop_start+extra_loops]

    for index, row in enumerate(curr_grid):
        for rock in row:
            if rock == "O":
                answer += len(curr_grid) - index

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
