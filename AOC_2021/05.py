# Advent of Code 2021
# Day 5

import os


class VentLine:
    def __init__(self, coordinates):
        split_coordinates = coordinates.split("->")
        start_pos, end_pos = split_coordinates[0].split(','), split_coordinates[1].split(',')
        self.start_x, self.start_y = (int(start_pos[0]), int(start_pos[1]))
        self.end_x, self.end_y = (int(end_pos[0]), int(end_pos[1]))

        self.is_vert_horiz = self.start[0] == self.end[0] or self.start[1] == self.end[1]


def main():
    with open(f"input{os.sep}day05_example.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().strip().split('\n')
    
    vent_lines = []
    for segment in puzzle_input:
        vent_lines.append(VentLine(segment))

    for line in vent_lines:
        if line.is_vert_horiz:
            pass

#    print(f"Part One: {}")
    
#    print(f"Part Two: {}")


if __name__ == "__main__":
    main()

