# Advent of Code 2025
# Day 07

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    beam_start = (0, puzzle_input[0].find('S'))
    beams = [(beam_start)]
    curr_row = 1
    while curr_row < len(puzzle_input):
        retired_beams = []
        new_beams = []
        for idx, (row, col) in enumerate(beams):
            if puzzle_input[curr_row][col] == '^':
                answer += 1
                retired_beams.append(idx)
                new_beams += [(curr_row, col - 1), (curr_row, col + 1)]
            else:
                beams[idx] = (curr_row, col)

        for idx, retired_idx in enumerate(retired_beams):
            del beams[retired_idx - idx]

        beams += new_beams
        beams = list(set(beams))
        curr_row += 1

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    path_counts = [0] * len(puzzle_input[0])
    beam_start = (0, puzzle_input[0].find('S'))
    path_counts[beam_start[1]] = 1
    beams = [(beam_start)]
    curr_row = 1
    while curr_row < len(puzzle_input):
        retired_beams = []
        new_beams = []
        for idx, (row, col) in enumerate(beams):
            if puzzle_input[curr_row][col] == '^':
                answer += 1
                retired_beams.append(idx)
                new_beams += [(curr_row, col - 1), (curr_row, col + 1)]
                path_counts[col-1] += path_counts[col]
                path_counts[col+1] += path_counts[col]
                path_counts[col] = 0
            else:
                beams[idx] = (curr_row, col)

        for idx, retired_idx in enumerate(retired_beams):
            del beams[retired_idx - idx]

        beams += new_beams
        beams = list(set(beams))
        curr_row += 1

    answer = sum(path_counts)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
