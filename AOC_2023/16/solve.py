# Advent of Code 2023
# Day 16

import time
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


direction_change_dict = {
    Direction.EAST: {"/": Direction.NORTH, "|": (Direction.NORTH, Direction.SOUTH), "\\": Direction.SOUTH, "-": Direction.EAST},
    Direction.SOUTH: {"/": Direction.WEST, "|": Direction.SOUTH, "\\": Direction.EAST, "-": (Direction.WEST, Direction.EAST)},
    Direction.WEST: {"/": Direction.SOUTH, "|": (Direction.NORTH, Direction.SOUTH), "\\": Direction.NORTH, "-": Direction.WEST},
    Direction.NORTH: {"/": Direction.EAST, "|": Direction.NORTH, "\\": Direction.WEST, "-": (Direction.WEST, Direction.EAST)}
}


class Ray:
    def __init__(self, direction, position):
        self.is_valid = True
        self.direction = direction
        self.position = position


def track_rays(grid, starting_direction=Direction.EAST, starting_pos=(0,-1)):
    positions_tracked = set()
    paths_taken = []
    rays = [Ray(starting_direction, starting_pos)]
    tracking = True
    while tracking:
        tracking = False
        for ray in rays:
            if ray.is_valid:
                tracking = True
                positions_tracked.add(ray.position)
                paths_taken.append((ray.direction, ray.position))
                y_pos, x_pos = ray.position
                if ray.direction == Direction.EAST or ray.direction == Direction.WEST:
                    x_pos += ray.direction.value[1]
                else:
                    y_pos += ray.direction.value[0]
                if (y_pos >= 0 and y_pos < len(grid)) and (x_pos >= 0 and x_pos < len(grid[0])):
                    next_symbol = grid[y_pos][x_pos]
                    ray.position = (y_pos, x_pos)
                    if next_symbol != '.':
                        new_direction = direction_change_dict[ray.direction][next_symbol]
                        if type(new_direction) != tuple:
                            ray.direction = new_direction
                        else:
                            ray.direction = new_direction[0]
                            if (new_direction[1], ray.position) not in paths_taken:
                                rays.append(Ray(new_direction[1], ray.position))
                                # paths_taken.append((new_direction[1], ray.position))
                    if (ray.direction, ray.position) in paths_taken:
                        ray.is_valid = False
                else:
                    ray.is_valid = False

    return len(positions_tracked) - 1  # remove one position to account for starting off grid


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    answer = track_rays(puzzle_input)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    energized_tile_counts = []
    for i in range(len(puzzle_input)):
        energized_tile_counts.append(track_rays(puzzle_input, starting_direction=Direction.EAST, starting_pos=(i, -1)))
        energized_tile_counts.append(track_rays(puzzle_input, starting_direction=Direction.WEST, starting_pos=(i, len(puzzle_input))))
    for i in range(len(puzzle_input[0])):
        energized_tile_counts.append(track_rays(puzzle_input, starting_direction=Direction.SOUTH, starting_pos=(-1, i)))
        energized_tile_counts.append(track_rays(puzzle_input, starting_direction=Direction.NORTH, starting_pos=(len(puzzle_input[0]), i)))

    answer = max(energized_tile_counts)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
