# Advent of Code 2024
# Day 6

import time
import copy

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    guard_grid = []
    guard_pos = None
    for idx, line in enumerate(puzzle_input):
        guard_grid.append([space for space in line])
        if '^' in line:
            guard_pos = [idx, line.index('^')]

    start_guard_pos = copy.copy(guard_pos)
    
    traversed_grid = copy.deepcopy(guard_grid)
    traversed_grid[guard_pos[0]][guard_pos[1]] = "X"
    guard_dir = N
    locations_visited = []
    try:
        while True:
            guard_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
            row, col = guard_pos
            if row < 0 or col < 0:
                break
            if traversed_grid[row][col] == "#":
                guard_pos = (guard_pos[0] - guard_dir[0], guard_pos[1] - guard_dir[1])
                if guard_dir == N:
                    guard_dir = E
                elif guard_dir == E:
                    guard_dir = S
                elif guard_dir == S:
                    guard_dir = W
                elif guard_dir == W:
                    guard_dir = N
            else:
                traversed_grid[row][col] = "X"
                if (row, col) not in locations_visited:
                    locations_visited.append((row, col))

    except Exception as error:
        pass

    for row in traversed_grid:
        answer = len(locations_visited)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    for idx, loc in enumerate(locations_visited):
        infinite_loop_locs = []
        guard_pos = copy.copy(start_guard_pos)
        traversed_grid = copy.deepcopy(guard_grid)
        l_row, l_col = loc
        traversed_grid[l_row][l_col] = "#"
        guard_dir = N
        
        try:
            while True:
                guard_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
                row, col = guard_pos
                if row < 0 or col < 0:
                    break
                    
                if traversed_grid[row][col] == "#":
                    guard_pos = (guard_pos[0] - guard_dir[0], guard_pos[1] - guard_dir[1])
                    if guard_dir == N:
                        guard_dir = E
                    elif guard_dir == E:
                        guard_dir = S
                    elif guard_dir == S:
                        guard_dir = W
                    elif guard_dir == W:
                        guard_dir = N

                loc_dir = ((row, col), guard_dir)

                if loc_dir not in infinite_loop_locs:
                    infinite_loop_locs.append(loc_dir)
                else:
                    answer += 1
                    break

        except Exception as error:
            pass

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
