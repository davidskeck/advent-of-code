# Advent of Code 2022
# Day 14

import time
import random

import pyxel
import pyperclip

input_files = [
    #"example.txt",
    "input.txt"
]

SAND_POUR_POINT = (500, 0)
DISPLAY_PADDING = 400
ROCK_COLOR = 13
SAND_COLORS = [9, 10, 15]


class SandGrain:
    def __init__(self, starting_point, floor_y):
        self.x, self.y = starting_point
        self.floor_y = floor_y
        self.color = random.choice(SAND_COLORS)
        self.can_move = None
        self.on_floor = False
        self.in_abyss = False

    def update(self):
        self.can_move = True
        if pyxel.pget(self.x, self.y + 1) == 0:
            self.y += 1
        elif pyxel.pget(self.x - 1, self.y + 1) == 0:
            self.y += 1
            self.x -= 1
        elif pyxel.pget(self.x + 1, self.y + 1) == 0:
            self.y += 1
            self.x += 1
        else:
            self.can_move = False

        if self.x < 0 or self.x > pyxel.width:
            self.in_abyss = True
        if self.y < 0 or self.y >= self.floor_y + 1:
            self.in_abyss = True

        if self.y >= self.floor_y:
            self.y = self.floor_y + 1


class PyxelApp:
    def __init__(self, input_file):
        with open(input_file) as puzzle_data:
            self.puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]
        self.answer = 0
        self.grains_at_rest = 0
        self.part_two_known = False

        # Part One
        self.max_x_size = 0
        self.min_x_size = None
        self.max_y_size = 0
        self.min_y_size = 0
        self.floor_y = 0
        self.rock_lines = []
        self.sand_grains = []

        self.parse_puzzle_input()
        self.prepare_pyxel_canvas()

        pyxel.run(self.pyxel_update, self.pyxel_draw)

        pyperclip.copy(answer)
        print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    def parse_puzzle_input(self):
        for line in self.puzzle_input:
            current_line = ([tuple(coord.split(',')) for coord in line.split('->')])
            converted_line = []
            for point in current_line:
                converted_line.append((int(point[0]), int(point[1])))
            self.rock_lines.append(converted_line)

    def prepare_pyxel_canvas(self):
        for line in self.rock_lines:
            x_max_for_line = max([point[0] for point in line])
            if x_max_for_line > self.max_x_size:
                self.max_x_size = x_max_for_line
            x_min_for_line = min([point[0] for point in line])
            if self.min_x_size is None or self.min_x_size > x_min_for_line:
                self.min_x_size = x_min_for_line
            y_max_for_line = max([point[1] for point in line])
            if y_max_for_line > self.max_y_size:
                self.max_y_size = y_max_for_line

        self.floor_y = self.get_scaled_point((0, self.max_y_size + 2))[1]

        x_canvas_size = self.max_x_size - self.min_x_size + DISPLAY_PADDING
        y_canvas_size = self.max_y_size + DISPLAY_PADDING
        pyxel.init(x_canvas_size, y_canvas_size, fps=120)

    def get_scaled_point(self, position):
        x_pos = position[0] - self.min_x_size + (DISPLAY_PADDING / 2)
        y_pos = position[1] + (DISPLAY_PADDING / 2)

        return x_pos, y_pos

    def draw_rock_lines(self):
        for line in self.rock_lines:
            start_point = line[0]
            for point_index in range(1, len(line)):
                end_point = line[point_index]
                x1, y1 = self.get_scaled_point(start_point)
                x2, y2 = self.get_scaled_point(end_point)
                pyxel.line(x1, y1, x2, y2, ROCK_COLOR)
                start_point = end_point

        pyxel.line(0, self.floor_y, pyxel.width, self.floor_y, ROCK_COLOR)

    def add_one_sand_grain(self):
        starting_point = self.get_scaled_point(SAND_POUR_POINT)
        if pyxel.pget(starting_point[0], starting_point[1]) == 0:
            self.sand_grains.append(SandGrain(starting_point, self.floor_y))
        else:
            self.part_two_known = True

    def pyxel_update(self):
        for grain in self.sand_grains:
            grain.update()
        all_grains_at_rest = True
        self.grains_at_rest = 0
        any_grains_in_abyss = False
        for grain in self.sand_grains:
            if grain.can_move:
                all_grains_at_rest = False
            else:
                self.grains_at_rest += 1
            if grain.in_abyss:
                any_grains_in_abyss = True

        if any_grains_in_abyss:
            print(f"{self.grains_at_rest}")
            self.answer = self.grains_at_rest
            pyperclip.copy(self.answer)

        if not any_grains_in_abyss and all_grains_at_rest or pyxel.frame_count % 10 == 0:
            self.add_one_sand_grain()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


    def pyxel_draw(self):
        pyxel.cls(0)
        self.draw_rock_lines()
        for grain in self.sand_grains:
            pyxel.pset(grain.x, grain.y, grain.color)
        answer_color = 3 if self.answer > 0 else 7
        if self.part_two_known:
            answer_color = 8
            print(f"{self.grains_at_rest}")
        pyxel.text(1, 1, f"{self.grains_at_rest}", answer_color)


def main(input_file):
    app = PyxelApp(input_file)
    #pyperclip.copy(answer)
    #print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
