# Advent of Code 2022
# Day 9

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def move_position(position, direction):
    if direction == "U":
        position[1] += 1
    elif direction == "D":
        position[1] -= 1
    elif direction == "L":
        position[0] -= 1
    elif direction == "R":
        position[0] += 1

    return position


def get_trailing_position(leading_position, trailing_position):
    x_diff = leading_position[0] - trailing_position[0]
    y_diff = leading_position[1] - trailing_position[1]
    is_adjacent = abs(x_diff) <= 1 and abs(y_diff) <= 1

    if not is_adjacent:
        if leading_position[0] == trailing_position[0] or leading_position [1] == trailing_position[1]:
            if abs(x_diff) >= 2:
                if x_diff > 0:
                    trailing_position[0] += 1
                else:
                    trailing_position[0] -= 1
            elif abs(y_diff) >= 2:
                if y_diff > 0:
                    trailing_position[1] += 1
                else:
                    trailing_position[1] -= 1
        else:
            if abs(x_diff) >= 1:
                if x_diff > 0:
                    trailing_position[0] += 1
                else:
                    trailing_position[0] -= 1
            if abs(y_diff) >= 1:
                if y_diff > 0:
                    trailing_position[1] += 1
                else:
                    trailing_position[1] -= 1

    return trailing_position


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    head_position = [0, 0]
    tail_position = [0, 0]
    tail_positions = [tuple(head_position)]
    for line in puzzle_input:
        direction, steps = line.split()
        for i in range(int(steps)):
            move_position(head_position, direction)
            tail_position = get_trailing_position(head_position, tail_position)
            if tuple(tail_position) not in tail_positions:
                tail_positions.append(tuple(tail_position))

    answer = len(tail_positions)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    head_position = [0, 0]
    knot_positions = [[0, 0] for i in range(9)]
    tail_positions = [tuple(head_position)]
    for line in puzzle_input:
        direction, steps = line.split()
        for i in range(int(steps)):
            move_position(head_position, direction)

            for knot_index, knot_position in enumerate(knot_positions):
                if knot_index > 0:
                    curr_head_position = knot_positions[knot_index - 1]
                else:
                    curr_head_position = head_position

                knot_position = get_trailing_position(curr_head_position, knot_position)

            if tuple(knot_positions[-1]) not in tail_positions:
                tail_positions.append(tuple(knot_positions[-1]))

    answer = len(tail_positions)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
