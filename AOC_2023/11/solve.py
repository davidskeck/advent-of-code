# Advent of Code 2023
# Day 11

import time
import re

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

def get_expansion_counts(galaxy, y_exp, x_exp):
    y_exp_count = 0
    for expansion in y_exp:
        if galaxy[0] > expansion:
            y_exp_count += 1
    
    x_exp_count = 0
    for expansion in x_exp:
        if galaxy[1] > expansion:
            x_exp_count += 1

    return (y_exp_count, x_exp_count)


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    universe = [line for line in puzzle_input]
    y_expansions = []
    for index, line in enumerate(puzzle_input):
        if all(pos == '.' for pos in line):
            y_expansions.append(index)

    for exp_num, exp_idx in enumerate(y_expansions):
        universe.insert(exp_idx + exp_num, len(puzzle_input[0]) * '.')
    
    x_expansions = []
    for index in range(len(universe[0])):
        current_col = [pos[index] for pos in universe]
        if all(pos == '.' for pos in current_col):
            x_expansions.append(index)
    
    for exp_num, exp_idx in enumerate(x_expansions):
        for row_idx, row in enumerate(universe):
            row_list = list(row)
            row_list.insert(exp_idx + exp_num, '.')
            row = "".join(row_list)
            universe[row_idx] = row

    galaxies = []
    for index, line in enumerate(universe):
        galaxies_found = re.finditer(r'#', line)
        for g_found in galaxies_found:
            galaxies.append((index, g_found.span()[0]))

    checked_galaxies = []
    for i in range(len(galaxies)):
        for j in range(len(galaxies)):
            if j not in checked_galaxies and i != j:
                distance = abs(galaxies[i][1] - galaxies[j][1]) + abs(galaxies[i][0] - galaxies[j][0])
                answer += distance
        checked_galaxies.append(i)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    galaxies = []
    for index, line in enumerate(puzzle_input):
        galaxies_found = re.finditer(r'#', line)
        for g_found in galaxies_found:
            galaxies.append((index, g_found.span()[0]))
    
    galaxy_expansion_counts = []
    for galaxy in galaxies:
        galaxy_expansion_counts.append(get_expansion_counts(galaxy, y_expansions, x_expansions))

    multipler = 1000000 - 1  # -1 to account for existing empty col/row
    checked_galaxies = []
    for i in range(len(galaxies)):
        for j in range(len(galaxies)):
            if j not in checked_galaxies and i != j:
                i_gal = galaxies[i]
                i_gal_vals = (i_gal[0] + (galaxy_expansion_counts[i][0] * multipler), i_gal[1] + (galaxy_expansion_counts[i][1] * multipler))
                j_gal = galaxies[j]
                j_gal_vals = (j_gal[0] + (galaxy_expansion_counts[j][0] * multipler), j_gal[1] + (galaxy_expansion_counts[j][1] * multipler))
                distance = abs(i_gal_vals[1] - j_gal_vals[1]) + abs(i_gal_vals[0] - j_gal_vals[0])
                answer += distance
        checked_galaxies.append(i)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
