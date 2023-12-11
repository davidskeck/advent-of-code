# Advent of Code 2023
# Day 10

import time
from enum import Enum

import pyperclip

input_files = [
    "example.txt",
    "example_p2.txt",
    "input.txt"
]

class Direction(Enum):
    NORTH = (-1,  0)
    EAST  = ( 0,  1)
    SOUTH = ( 1,  0)
    WEST  = ( 0, -1)


START_SYMBOL = "S"
directions_to_check = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]


negated_dir_dict = {
    Direction.NORTH: Direction.SOUTH,
    Direction.SOUTH: Direction.NORTH,
    Direction.EAST: Direction.WEST,
    Direction.WEST: Direction.EAST
}


# Y, X ordering
direction_dict = {
    "|": [Direction.NORTH, Direction.SOUTH],
    "-": [Direction.EAST,  Direction.WEST],
    "L": [Direction.NORTH, Direction.EAST],
    "J": [Direction.NORTH, Direction.WEST],
    "7": [Direction.SOUTH, Direction.WEST],
    "F": [Direction.SOUTH, Direction.EAST],
    ".": [],                                                                 # Ground
    START_SYMBOL: [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]  # Starting Position
}


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    start_pos = None
    for index, line in enumerate(puzzle_input):
        if START_SYMBOL in line:
            start_pos = (index, line.find("S"))
            break
    
    movement_path = [start_pos]

    loop_completed = False
    prev_dir = None
    current_pos = start_pos
    while not loop_completed:
        for direction in directions_to_check:
            curr_y, curr_x = current_pos
            next_dir = direction.value
            next_pos = (curr_y + next_dir[0], curr_x + next_dir[1])
            next_y, next_x = next_pos
            if (next_y >= 0 and next_x >= 0) and (next_y < len(puzzle_input) and next_x < len(puzzle_input[0])):
                possible_dirs = direction_dict[puzzle_input[next_y][next_x]]
                if len(possible_dirs) > 0 and (negated_dir_dict[direction] in possible_dirs) and direction in direction_dict[puzzle_input[curr_y][curr_x]]:
                        if prev_dir is not None:
                            if direction == negated_dir_dict[prev_dir]:
                                continue
                        if next_pos not in movement_path:
                            current_pos = next_pos
                            movement_path.append(current_pos)
                            prev_dir = direction
                            break
                        elif puzzle_input[next_pos[0]][next_pos[1]] == START_SYMBOL:
                            loop_completed = True
                            break

    answer = round(len(movement_path) / 2)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    for y_index, line in enumerate(puzzle_input):
        walls_hit = 0
        for x_index, symbol in enumerate(line):
            this_pos = (y_index, x_index)
            this_sym = puzzle_input[y_index][x_index]
            if walls_hit != 0 and walls_hit % 2 != 0 and this_pos not in movement_path:
                answer += 1
            if this_pos in movement_path and this_sym in '|F7S':
                walls_hit += 1

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
