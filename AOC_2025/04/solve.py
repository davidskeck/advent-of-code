# Advent of Code 2025
# Day 04

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def check_access(grid, r_idx, c_idx):
    r_len = len(grid)
    c_len = len(grid[0])

    conflict_count = 0

    st_r = r_idx - 1
    st_c = c_idx - 1
    for i in range(3):
        for j in range(3):
            curr_r = st_r + i
            curr_c = st_c + j
            if (curr_r < 0 or curr_c < 0) or curr_r == r_idx and curr_c == c_idx:
                continue
            try:
                if '@' in grid[curr_r][curr_c]:
                    conflict_count += 1
            except Exception:
                pass

    if conflict_count >= 4:
        return False
    else:
        return True
        


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    paper_grid = []
    for line in puzzle_input:
        paper_grid.append([pos for pos in line])
    
    for r_idx, row in enumerate(paper_grid):
        for c_idx, col in enumerate(row):
            if "@" in col:
                if check_access(paper_grid, r_idx, c_idx):
                    answer += 1

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    while True:
        accessible_rolls = []
        for r_idx, row in enumerate(paper_grid):
            for c_idx, col in enumerate(row):
                if "@" in col:
                    if check_access(paper_grid, r_idx, c_idx):
                        answer += 1
                        accessible_rolls.append((r_idx, c_idx))
        
        for roll in accessible_rolls:
            roll_row, roll_col = roll
            paper_grid[roll_row][roll_col] = "."
        
        if len(accessible_rolls) == 0:
            break
    
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
