# Advent of Code 2022
# Day 08

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def check_tree_visible(tree_grid, height, position):
    row_pos, column_pos = position

    is_visible = False
    current_row = tree_grid[row_pos]
    current_column = [row[column_pos] for row in tree_grid]

    left_side = current_row[:column_pos]
    right_side = current_row[column_pos + 1:]
    up_side = current_column[:row_pos]
    down_side = current_column[row_pos + 1:]

    for side in [left_side, right_side, up_side, down_side]:
        if max(side) < height:
            is_visible = True
            break

    return is_visible


def get_tree_scenic_score(tree_grid, height, position):
    row_pos, column_pos = position

    is_visible = False
    current_row = tree_grid[row_pos]
    current_column = [row[column_pos] for row in tree_grid]

    left_side = reversed(current_row[:column_pos])
    right_side = current_row[column_pos + 1:]
    up_side = reversed(current_column[:row_pos])
    down_side = current_column[row_pos + 1:]

    scores = []
    for side in [left_side, right_side, up_side, down_side]:
        side_score = 0
        for side_height in side:
            side_score += 1
            if side_height >= height:
                break
        scores.append(side_score)

    scenic_score = 1
    for score in scores:
        scenic_score *= score

    return scenic_score


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    tree_grid = []
    for row_index, line in enumerate(puzzle_input):
        current_row = []
        for column_index, height in enumerate(line):
            current_row.append(int(height))
        tree_grid.append(current_row)

    answer += (len(tree_grid) * 2) + ((len(tree_grid[0]) - 2) * 2)

    row_size = len(tree_grid)
    column_size = len(tree_grid[0])
    visible_tree_positions = []
    for row_index, line in enumerate(tree_grid):
        for column_index, height in enumerate(line):
            if row_index != 0 and row_index != row_size - 1 and column_index != 0 and column_index != column_size - 1:
                position = (row_index, column_index)
                if check_tree_visible(tree_grid, height, position):
                    visible_tree_positions.append(position)

    answer += len(visible_tree_positions)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    scenic_scores = []
    for row_index, line in enumerate(tree_grid):
        for column_index, height in enumerate(line):
            if row_index != 0 and row_index != row_size - 1 and column_index != 0 and column_index != column_size - 1:
                position = (row_index, column_index)
                score = get_tree_scenic_score(tree_grid, height, position)
                scenic_scores.append(score)

    answer = max(scenic_scores)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for file in input_files:
        start_time = time.time()
        main(file)
        print(f"{file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
