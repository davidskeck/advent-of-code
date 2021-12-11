# Advent of Code 2021
# Day 11

import os


def check_indices(x, y, input_list):
    access_ok = False
    if x >= 0 and y >= 0:
        try:
            _ = input_list[x][y]
            access_ok = True
        except:
            access_ok = False

    return access_ok


def get_adjacent_locations(x, y, octo_map):
    adjacent_locations = []
    if check_indices(x - 1, y, octo_map):
        adjacent_locations.append((octo_map[x - 1][y], x - 1, y))
    if check_indices(x + 1, y, octo_map):
        adjacent_locations.append((octo_map[x + 1][y], x + 1, y))
    if check_indices(x, y - 1, octo_map):
        adjacent_locations.append((octo_map[x][y - 1], x, y - 1))
    if check_indices(x, y + 1, octo_map):
        adjacent_locations.append((octo_map[x][y + 1], x, y + 1))
    if check_indices(x - 1, y - 1, octo_map):
        adjacent_locations.append((octo_map[x - 1][y - 1], x - 1, y - 1))
    if check_indices(x + 1, y + 1, octo_map):
        adjacent_locations.append((octo_map[x + 1][y + 1], x + 1, y + 1))
    if check_indices(x + 1, y - 1, octo_map):
        adjacent_locations.append((octo_map[x + 1][y - 1], x + 1, y - 1))
    if check_indices(x - 1, y + 1, octo_map):
        adjacent_locations.append((octo_map[x - 1][y + 1], x - 1, y + 1))
    
    return adjacent_locations 


def main():
    with open(f"input{os.sep}day11.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().strip().split()
    
    octo_map = []
    for line in puzzle_input:
        octo_map.append(list(line))
    
    octo_map = [list(map(int, row)) for row in octo_map]
    
    total_flashes = 0
    step = 0
    while True:
        step += 1
        flashed_locations = []
        for row_index in range(len(octo_map)):
            for column_index, column in enumerate(octo_map[row_index]):
                octo_map[row_index][column_index] += 1
        
        flashed_locations = []
        while True:
            new_flashes = False
            for row_index in range(len(octo_map)):
                for column_index, column in enumerate(octo_map[row_index]): 
                    if octo_map[row_index][column_index] > 9 and (row_index, column_index) not in flashed_locations:
                        new_flashes = True
                        flashed_locations.append((row_index, column_index))
                        octo_map[row_index][column_index] = 0 
                        adjacent_locations = get_adjacent_locations(row_index, column_index, octo_map)
                        for location in adjacent_locations:
                            val, row, col = location
                            if val != 0:
                                octo_map[row][col] += 1
            if not new_flashes:
                break
        
        if step <= 100:
            total_flashes += len(flashed_locations)
        if step == 100:
            print(f"Part One: {total_flashes}")
        if len(flashed_locations) == 100:
            print(f"Part Two: {step}")
            break


if __name__ == "__main__":
    main()

