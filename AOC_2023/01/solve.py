# Advent of Code 2023
# Day 01

import time

import pyperclip

input_files = [
    "example.txt",
    "example2.txt",
    "input.txt"
]

digit_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = 0

    for calib_value in puzzle_input:
        str_val = ""
        for val in calib_value:
            if val.isdigit():
                str_val += val
        if len(str_val) == 1:
            str_val *= 2
        if len(str_val) > 2:
            str_val = str_val[0] + str_val[-1]
        
        if len(str_val) > 0:
            answer += int(str_val)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    converted_calib_vals = []
    for calib_value in puzzle_input:
        converted_val = calib_value
        replacement_indices = {}
        for int_str in digit_dict.keys():
            int_str_idx = converted_val.find(int_str)
            if int_str_idx != -1:
                replacement_indices[int_str_idx] = int_str
                
        for int_str in digit_dict.keys():
            int_str_idx = converted_val.rfind(int_str)
            if int_str_idx != -1:
                replacement_indices[int_str_idx] = int_str

        for index, int_str in replacement_indices.items():
            str_list = list(converted_val)
            str_list[index] = digit_dict[int_str]
            converted_val = "".join(str_list)
        converted_calib_vals.append(converted_val)
    
    for calib_value in converted_calib_vals:
        str_val = ""
        for val in calib_value:
            if val.isdigit():
                str_val += val
        if len(str_val) == 1:
            str_val *= 2
        if len(str_val) > 2:
            str_val = str_val[0] + str_val[-1]
        answer += int(str_val)
    
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
