# Advent of Code 2024
# Day 4

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def x_mas_detector(fs_mas_s, bs_mas_s):
    x_mas_s_detected = 0

    for fs_mas in fs_mas_s:
        fs_mid_index = fs_mas[1][1]
        for bs_mas in bs_mas_s:
            bs_mid_index = bs_mas[1][1]
            if fs_mid_index == bs_mid_index:
                x_mas_s_detected += 1
                break

    return x_mas_s_detected

def mas_detector(grid, start):
    # Make these zero indexed for easier comparison
    word = "MAS"
    row_len = len(grid) - 1
    col_len = len(grid[0]) - 1
    word_len = len(word) - 1
    row, col = start

    found_mas_s = []

    # Check NW direction
    if row - word_len >= 0 and col - word_len >= 0:
        collected_word = []
        indices = []
        for i in range(word_len + 1):
            indices.append((row - i, col - i))
            collected_word.append(grid[row - i][col - i])
        row_pos_word = ''.join(collected_word)
        if row_pos_word == word:
            found_mas_s.append(("BS", indices))

    # Check NE direction
    if row - word_len >= 0 and col + word_len <= col_len:
        collected_word = []
        indices = []
        for i in range(word_len + 1):
            indices.append((row - i, col + i))
            collected_word.append(grid[row - i][col + i])
        row_pos_word = ''.join(collected_word)
        if row_pos_word == word:
            found_mas_s.append(("FS", indices))

    # Check SE direction
    if row + word_len <= row_len and col + word_len <= col_len:
        collected_word = []
        indices = []
        for i in range(word_len + 1):
            indices.append((row + i, col + i))
            collected_word.append(grid[row + i][col + i])
        row_pos_word = ''.join(collected_word)
        if row_pos_word == word:
            found_mas_s.append(("BS", indices))

    # Check SW direction
    if row + word_len <= row_len and col - word_len >= 0:
        collected_word = []
        indices = []
        for i in range(word_len + 1):
            indices.append((row + i, col - i))
            collected_word.append(grid[row + i][col - i])
        row_pos_word = ''.join(collected_word)
        if row_pos_word == word:
            found_mas_s.append(("FS", indices))

    return found_mas_s

def word_detector(grid, start, word):
    # Make these zero indexed for easier comparison
    row_len = len(grid) - 1
    col_len = len(grid[0]) - 1
    word_len = len(word) - 1
    row, col = start

    words_detected = 0
    # Check positive column direction
    curr_row = grid[row]
    if col + word_len <= col_len:
        col_pos_word = ''.join(curr_row[col:col + word_len + 1])
        if col_pos_word == word:
            words_detected += 1
    
    # Check negative column direction
    curr_row = grid[row]
    if col - word_len >= 0:
        col_pos_word = curr_row[col - word_len:col + 1]
        col_pos_word = ''.join((reversed(col_pos_word)))
        if col_pos_word == word:
            words_detected += 1
    
    # Check positive row direction
    if row + word_len <= row_len:
        collected_word = []
        for i in range(word_len + 1):
            collected_word.append(grid[row + i][col])
        row_pos_word = ''.join(collected_word)
        if row_pos_word == word:
            words_detected += 1

    # Check negative row direction
    if row - word_len >= 0:
        collected_word = []
        for i in range(word_len + 1):
            collected_word.append(grid[row - i][col])
        col_pos_word = ''.join(collected_word)
        if col_pos_word == word:
            words_detected += 1

    # Check NW direction
    if row - word_len >= 0 and col - word_len >= 0:
        collected_word = []
        for i in range(word_len + 1):
            collected_word.append(grid[row - i][col - i])
        row_pos_word = ''.join(collected_word)
        if row_pos_word == word:
            words_detected += 1

    # Check NE direction
    if row - word_len >= 0 and col + word_len <= col_len:
        collected_word = []
        for i in range(word_len + 1):
            collected_word.append(grid[row - i][col + i])
        row_pos_word = ''.join(collected_word)
        if row_pos_word == word:
            words_detected += 1

    # Check SE direction
    if row + word_len <= row_len and col + word_len <= col_len:
        collected_word = []
        for i in range(word_len + 1):
            collected_word.append(grid[row + i][col + i])
        row_pos_word = ''.join(collected_word)
        if row_pos_word == word:
            words_detected += 1

    # Check SW direction
    if row + word_len <= row_len and col - word_len >= 0:
        collected_word = []
        for i in range(word_len + 1):
            collected_word.append(grid[row + i][col - i])
        row_pos_word = ''.join(collected_word)
        if row_pos_word == word:
            words_detected += 1

    return words_detected


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    word_search_grid = []
    for line in puzzle_input:
        word_search_grid.append(list(line))
    
    possible_starts = []
    for row_idx, row in enumerate(word_search_grid):
        for col_idx, char in enumerate(row):
            if char == "X":
                possible_starts.append((row_idx, col_idx))
    
    for start in possible_starts:
        answer += word_detector(word_search_grid, start, "XMAS")

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    possible_starts = []
    for row_idx, row in enumerate(word_search_grid):
        for col_idx, char in enumerate(row):
            if char == "M":
                possible_starts.append((row_idx, col_idx))

    fs_mas_s = []
    bs_mas_s = []
    for start in possible_starts:
        mas_s = mas_detector(word_search_grid, start)
        for mas in mas_s:
            if mas[0] == "FS":
                fs_mas_s.append(mas)
            else:
                bs_mas_s.append(mas)

    answer += x_mas_detector(fs_mas_s, bs_mas_s)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
