# Advent of Code 2021
# Day 5

import os
from collections import Counter


class VentLine:
    def __init__(self, coordinates):
        split_coordinates = coordinates.split("->")
        start_pos, end_pos = split_coordinates[0].split(','), split_coordinates[1].split(',')
        self.start_x, self.start_y = (int(start_pos[0]), int(start_pos[1]))
        self.end_x, self.end_y = (int(end_pos[0]), int(end_pos[1]))
        self.path = []
        self.trace_path()
        self.is_vert_horiz = self.start_x == self.end_x or self.start_y == self.end_y

    def trace_path(self):
        if self.start_x == self.end_x:
            if self.start_y > self.end_y:
                larger = self.start_y
                smaller = self.end_y
            else:
                larger = self.end_y
                smaller = self.start_y
            for y in range(smaller, larger + 1):
                self.path.append((self.start_x, y))
        elif self.start_y == self.end_y:
            if self.start_x > self.end_x:
                larger = self.start_x
                smaller = self.end_x
            else:
                larger = self.end_x
                smaller = self.start_x
            for x in range(smaller, larger + 1):
                self.path.append((x, self.start_y))
        else:
            x_sign = 1 if self.end_x - self.start_x > 0 else -1
            y_sign = 1 if self.end_y - self.start_y > 0 else -1
            
            if x_sign == 1 and y_sign == -1:
                for index, x in enumerate(range(self.start_x, self.end_x + 1)):
                    self.path.append((x, self.start_y - index))
            elif x_sign == -1 and y_sign == 1:
                for index, y in enumerate(range(self.start_y, self.end_y + 1)):
                    self.path.append((self.start_x - index, y))
            elif x_sign == 1 and y_sign == 1:
                for index, x in enumerate(range(self.start_x, self.end_x + 1)):
                    self.path.append((x, self.start_y + index))
            elif x_sign == -1 and y_sign == -1:
                for index in range(abs(self.end_x - self.start_x) + 1):
                    self.path.append((self.start_x - index, self.start_y - index))


def main():
    with open(f"input{os.sep}day05.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().strip().split('\n')
    
    vent_lines = []
    for segment in puzzle_input:
        vent_lines.append(VentLine(segment))
    
    p1_points = []
    p2_points = []
    for line in vent_lines:
        if line.is_vert_horiz:
            p1_points.extend(line.path)
        p2_points.extend(line.path)

    point_counter = Counter(p1_points)
    collisions = 0
    for key, value in point_counter.items():
        if value > 1:
            collisions += 1

    print(f"Part One: {collisions}")

    point_counter = Counter(p2_points)
    collisions = 0
    for key, value in point_counter.items():
        if value > 1:
            collisions += 1

    print(f"Part Two: {collisions}")


if __name__ == "__main__":
    main()

