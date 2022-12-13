# Advent of Code 2022
# Day 12

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

def get_surrounding_paths(location, elevation_map):
    possible_paths = []
    row_pos, col_pos = location

    if row_pos > 0:
        upper_row = row_pos - 1
        height = elevation_map[upper_row][col_pos]
        possible_paths.append((height, (upper_row, col_pos)))
    if row_pos < len(elevation_map) - 1:
        lower_row = row_pos + 1
        height = elevation_map[lower_row][col_pos]
        possible_paths.append((height, (lower_row, col_pos)))
    if col_pos > 0:
        prev_col = col_pos - 1
        height = elevation_map[row_pos][prev_col]
        possible_paths.append((height, (row_pos, prev_col)))
    if col_pos < len(elevation_map[0]) - 1:
        next_col = col_pos + 1
        height = elevation_map[row_pos][next_col]
        possible_paths.append((height, (row_pos, next_col)))

    return possible_paths


def get_lowest_steps_for_starting_points(starting_points, signal_location, elevation_map):
    possible_lengths = []
    for point in starting_points:
        all_tracks = [[point]]
        visited_nodes = []
        while len(all_tracks) > 0:
            current_track = all_tracks.pop()
            current_location = current_track[-1]
            current_height = elevation_map[current_location[0]][current_location[1]]
            if current_height == 'S':
                current_height = 'a'
            paths = get_surrounding_paths(current_location, elevation_map)

            for path in paths:
                height, location = path
                if height == 'E':
                    height = 'z'
                if location not in current_track and ord(current_height) + 1 >= ord(height) and location not in visited_nodes:
                    all_tracks.insert(0, current_track + [location])
                    visited_nodes.append(location)

            if current_track[-1] == signal_location:
                possible_lengths.append(len(current_track) - 1)
                break

    return min(possible_lengths)


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = 0

    elevation_map = [line for line in puzzle_input]
    current_height = None
    starting_location = None
    lowest_elevation_locations = []
    signal_location = None
    for row_index, row in enumerate(elevation_map):
        if 'S' in row:
            starting_location = (row_index, row.find('S'))
            current_height = 'a'
            lowest_elevation_locations.append(starting_location)
        if 'E' in row:
            signal_location = (row_index, row.find('E'))
        for column_index, elevation in enumerate(row):
            if elevation == 'a':
                lowest_elevation_locations.append((row_index, column_index))

    answer = get_lowest_steps_for_starting_points([starting_location], signal_location, elevation_map)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = get_lowest_steps_for_starting_points(lowest_elevation_locations, signal_location, elevation_map)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for file in input_files:
        start_time = time.time()
        main(file)
        print(f"{file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
