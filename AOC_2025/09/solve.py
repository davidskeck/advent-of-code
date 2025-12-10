# Advent of Code 2025
# Day 09

import time

import pyperclip
from shapely import Polygon, box

input_files = [
    "example.txt",
    "input.txt"
]


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    red_tile_locs = []
    for line in puzzle_input:
        col, row = tuple(line.split(','))
        red_tile_locs.append((int(col), int(row)))
    
    rect_sizes = {}
    for o_tile in red_tile_locs:
        for i_tile in red_tile_locs:
            if i_tile != o_tile:
                col_len = abs(o_tile[0] - i_tile[0]) + 1
                row_len = abs(o_tile[1] - i_tile[1]) + 1
                rect_sizes[tuple(sorted([o_tile, i_tile]))] = col_len * row_len
    
    answer = max(rect_sizes.values())

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    tile_shape = Polygon(red_tile_locs)
    rect_dict_sorted = dict(sorted(rect_sizes.items(), key=lambda entry: entry[1], reverse=True))
    for (o_tile, i_tile), rect_size in rect_dict_sorted.items():
        curr_rect = box(o_tile[0], o_tile[1], i_tile[0], i_tile[1])
        if tile_shape.contains(curr_rect):
            answer = rect_size
            break

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
