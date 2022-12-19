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
DISPLAY_PADDING_X = 300
DISPLAY_PADDING_Y = 20
ROCK_COLOR = 13
SAND_COLORS = [9, 10, 15]
OFFSCREEN_RENDER = False


class SandGrain:
    def __init__(self, starting_point, floor_y, pyxel_image=None):
        self.x, self.y = starting_point
        self.floor_y = floor_y
        self.color = random.choice(SAND_COLORS)
        self.can_move = None
        self.on_floor = False
        self.in_abyss = False
        self.pyxel_image = pyxel_image

    def update(self):
        self.can_move = True
        canvas = pyxel if self.pyxel_image is None else self.pyxel_image
        if canvas.pget(self.x, self.y + 1) == 0:
            self.y += 1
        elif canvas.pget(self.x - 1, self.y + 1) == 0:
            self.y += 1
            self.x -= 1
        elif canvas.pget(self.x + 1, self.y + 1) == 0:
            self.y += 1
            self.x += 1
        else:
            self.can_move = False

        if self.y >= self.floor_y - 2:
            self.in_abyss = True

        if self.y >= self.floor_y:
            self.y = self.floor_y + 1


class PyxelApp:
    def __init__(self, input_file):
        with open(input_file) as puzzle_data:
            self.puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]
        self.part_one_answer = 0
        self.part_two_answer = 0
        self.grains_at_rest = 0

        self.max_x_size = 0
        self.min_x_size = None
        self.max_y_size = 0
        self.min_y_size = 0
        self.floor_y = 0
        self.rock_lines = []
        self.sand_grains = []

        self.parse_puzzle_input()
        self.prepare_pyxel_canvas()

        if OFFSCREEN_RENDER:
            self.offscreen_render()
        else:
            self.add_one_sand_grain()

        pyxel.run(self.update, self.draw)

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

        x_canvas_size = self.max_x_size - self.min_x_size + DISPLAY_PADDING_X
        y_canvas_size = self.max_y_size + DISPLAY_PADDING_Y
        pyxel.init(x_canvas_size, y_canvas_size, fps=120)
        self.pyxel_image = pyxel.Image(x_canvas_size, y_canvas_size)

    def get_scaled_point(self, position):
        x_pos = position[0] - self.min_x_size + (DISPLAY_PADDING_X / 2) + 25
        y_pos = position[1] + (DISPLAY_PADDING_Y / 2)

        return x_pos, y_pos

    def draw_rock_lines(self, on_image=False):
        canvas = pyxel if not on_image else self.pyxel_image
        for line in self.rock_lines:
            start_point = line[0]
            for point_index in range(1, len(line)):
                end_point = line[point_index]
                x1, y1 = self.get_scaled_point(start_point)
                x2, y2 = self.get_scaled_point(end_point)
                canvas.line(x1, y1, x2, y2, ROCK_COLOR)
                start_point = end_point

        canvas.line(0, self.floor_y, pyxel.width, self.floor_y, ROCK_COLOR)

    def add_one_sand_grain(self):
        canvas = None if not OFFSCREEN_RENDER else self.pyxel_image
        starting_point = self.get_scaled_point(SAND_POUR_POINT)
        self.sand_grains.append(SandGrain(starting_point, self.floor_y, pyxel_image=canvas))

    def update_grains(self):
        grain_was_added = False
        current_grain = self.sand_grains[-1]
        current_grain.update()
        all_grains_at_rest = not current_grain.can_move
        self.grains_at_rest = len(self.sand_grains) if all_grains_at_rest else len(self.sand_grains) - 1

        if self.part_one_answer == 0:
            if current_grain.in_abyss:
                print(f"P1: {self.grains_at_rest}")
                self.part_one_answer = self.grains_at_rest

        if all_grains_at_rest:
            latest_grain_rest_point = (current_grain.x, current_grain.y)
            if latest_grain_rest_point != self.get_scaled_point(SAND_POUR_POINT):
                self.add_one_sand_grain()
                grain_was_added = True
            else:
                if self.part_two_answer == 0:
                    print(f"P2: {self.grains_at_rest}")
                    self.part_two_answer = self.grains_at_rest

        return grain_was_added

    def offscreen_render(self):
        self.pyxel_image.cls(0)
        self.draw_rock_lines(on_image=True)
        self.add_one_sand_grain()
        grain_was_added = self.update_grains()
        while self.part_one_answer == 0 or self.part_two_answer == 0 or grain_was_added:
            grain_was_added = self.update_grains()
            if grain_was_added:
                grain = self.sand_grains[-2]
                self.pyxel_image.pset(grain.x, grain.y, grain.color)
            else:
                grain = self.sand_grains[-1]
                if not grain.can_move:
                    self.pyxel_image.pset(grain.x, grain.y, grain.color)

            if self.part_one_answer > 0:
                self.pyxel_image.text(1, 1, f"P1: {self.part_one_answer}", 3)
            if self.part_two_answer > 0:
                self.pyxel_image.text(1, 10, f"P2: {self.part_two_answer}", 3)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        if OFFSCREEN_RENDER:
            pyxel.blt(0, 0, self.pyxel_image, 0, 0, self.pyxel_image.width, self.pyxel_image.height)
        else:
            if self.part_one_answer == 0 or self.part_two_answer == 0:
                pyxel.cls(0)
                self.draw_rock_lines()
                for grain in self.sand_grains:
                    pyxel.pset(grain.x, grain.y, grain.color)

                self.update_grains()

                if self.part_one_answer > 0:
                    pyxel.text(1, 1, f"P1: {self.part_one_answer}", 3)
                if self.part_two_answer > 0:
                    pyxel.text(1, 10, f"P2: {self.part_two_answer}", 3)


if __name__ == "__main__":
    app = PyxelApp(input_files[0])
