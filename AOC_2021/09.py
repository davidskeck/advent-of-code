# Advent of Code 2021
# Day 9

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


def get_adjacent_locations(x, y, height_map):
    adjacent_locations = []
    if check_indices(x - 1, y, height_map):
        adjacent_locations.append((height_map[x - 1][y], x - 1, y))
    if check_indices(x + 1, y, height_map):
        adjacent_locations.append((height_map[x + 1][y], x + 1, y))
    if check_indices(x, y - 1, height_map):
        adjacent_locations.append((height_map[x][y - 1], x, y - 1))
    if check_indices(x, y + 1, height_map):
        adjacent_locations.append((height_map[x][y + 1], x, y + 1))
    
    return adjacent_locations 


def main():
    with open(f"input{os.sep}day09.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().strip().split()
    
    height_map = []
    for line in puzzle_input:
        height_map.append(list(line))
    
    height_map = [list(map(int, row)) for row in height_map]
    
    lowest_points = []
    for row_index in range(len(height_map)):
        for column_index, column in enumerate(height_map[row_index]):
            adjacent_locations = get_adjacent_locations(row_index, column_index, height_map)
            current_value = column
            is_lowest = True
            for location in adjacent_locations:
                value = location[0]
                if value <= current_value:
                    is_lowest = False
                    break
            if is_lowest:
                lowest_points.append((current_value, row_index, column_index))

    total_risk = 0
    for point in lowest_points:
        total_risk += point[0] + 1
    
    print(f"Part One: {total_risk}")

    basin_sizes = []
    for point in lowest_points:
        _, cur_row, cur_col = point
        current_basin_size = 1
        adjacent_locations = get_adjacent_locations(cur_row, cur_col, height_map)
        basin_points = [(cur_row, cur_col)]
        next_points = []
        for location in adjacent_locations:
            value, row, col = location
            next_point = (row, col)
            if value < 9:
                if next_point not in basin_points:
                    next_points.append(next_point)
                    basin_points.append(next_point)
        
        while len(next_points) > 0:
            additional_points = []
            for location in next_points:
                row, col = location
                adjacent_locations = get_adjacent_locations(row, col, height_map)
                for location in adjacent_locations:
                    value, row, col = location
                    if value < 9:
                        next_point = (row, col)
                        if next_point not in basin_points:
                            basin_points.append(next_point)
                            additional_points.append(next_point)

            next_points = additional_points
            
            if len(next_points) == 0:
                basin_sizes.append(len(basin_points))
    
    basin_sizes.sort()
    print(f"Part Two: {basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}")


if __name__ == "__main__":
    main()

