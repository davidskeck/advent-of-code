# Advent of Code 2023
# Day 03

import re
import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

class PartNumber:
    def __init__(self, y_pos, span, value):
        self.y_pos = y_pos
        self.span = span
        self.value = value
        self.valid = False
        self.gear_location = None
        self.active = True

    def check_valid(self, val, location):
        if val != '.' and not val.isdigit():
            self.valid = True
            if val == '*':
                self.gear_location = location
        return self.valid


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0

    part_numbers = []
    for index, line in enumerate(puzzle_input):
        numbers_found = re.finditer(r'\d{1,}', line)
        for number in numbers_found:
            part_numbers.append(PartNumber(index, number.span(), int(number.group())))

    for number in part_numbers:
        current_y = number.y_pos
        current_x = number.span[0]

        if current_x > 0:
            val = puzzle_input[current_y][current_x-1]
            if number.check_valid(val, (current_y, current_x-1)):
                continue
        if number.span[1] < len(puzzle_input[0]):
            val = puzzle_input[current_y][number.span[1]]
            if number.check_valid(val, (current_y, number.span[1])):
                continue
        if current_y > 0:
            start_index = number.span[0]
            if start_index > 0:
                start_index -= 1
            end_index = number.span[1]
            if end_index < len(puzzle_input[0]):
                end_index += 1
            for i in range(start_index, end_index):
                val = puzzle_input[current_y-1][i]
                if number.check_valid(val, (current_y-1, i)):
                    continue
        if current_y < len(puzzle_input) - 1:
            start_index = number.span[0]
            if start_index > 0:
                start_index -= 1
            end_index = number.span[1]
            if end_index < len(puzzle_input[0]) - 1:
                end_index += 1
            for i in range(start_index, end_index):
                val = puzzle_input[current_y+1][i]
                if number.check_valid(val, (current_y+1, i)):
                    continue
    
    for number in part_numbers:
        if number.valid:
            answer += number.value

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    gear_ratios = []
    for number in part_numbers:
        if number.active:
            number.active = False
            matches = []
            if number.gear_location is not None:
                for inner_number in part_numbers:
                    if inner_number.active and number.gear_location == inner_number.gear_location:
                        matches.append(inner_number)
                        inner_number.active = False
            if len(matches) == 1:
                gear_ratios.append(number.value * matches[0].value)

    for ratio in gear_ratios:
        answer += ratio

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
