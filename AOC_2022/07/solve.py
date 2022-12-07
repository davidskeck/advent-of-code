# Advent of Code 2022
# Day 07

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

TOTAL_DISK_SPACE = 70000000
TOTAL_SPACE_NEEDED = 30000000
MINIMUM_DIRECTORY_SIZE = 100000


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    directories = {}
    curr_dir_pos = ''
    for line in puzzle_input:
        if '$' in line:
            if "cd" in line:
                directory_target = line[5:].strip()
                if "/" in directory_target:
                    curr_dir_pos = "root"
                    directories["root"] = 0
                elif ".." in directory_target:
                    curr_dir_pos = curr_dir_pos[:curr_dir_pos.rindex("/")]
                else:
                    curr_dir_pos += "/" + directory_target
        if "dir" in line:
            dir_name = line.split("dir")[-1].strip()
            dir_name = curr_dir_pos + "/" + dir_name
            if dir_name not in directories:
                directories[dir_name] = 0
        if line.split()[0].isnumeric():
            if curr_dir_pos in directories:
                directories[curr_dir_pos] += int(line.split()[0])
            else:
                directories[curr_dir_pos] = int(line.split()[0])

    for key, value in directories.items():
        for inner_key, inner_value in directories.items():
            if key != inner_key and key in inner_key:
                directories[key] += inner_value

    total_size = 0
    for key, value in directories.items():
        if value <= MINIMUM_DIRECTORY_SIZE:
            total_size += value

    answer = total_size
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    current_size = directories["root"]
    free_space = TOTAL_DISK_SPACE - current_size
    size_needed = TOTAL_SPACE_NEEDED - free_space

    sizes_to_delete = []
    for key, value in directories.items():
        if value >= size_needed:
            sizes_to_delete.append(value)

    answer = sorted(sizes_to_delete)[0]
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for file in input_files:
        main(file)
