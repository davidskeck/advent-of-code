# Advent of Code 2022
# Day 3

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = puzzle_data.read().split('\n')

    # Part One
    answer = 0
    for rucksack in puzzle_input:
        if rucksack == "":
            continue
        size = len(rucksack) // 2
        compartment_one = rucksack[0:size]
        compartment_two = rucksack[size:]

        same_char = None
        for character in compartment_one:
            if character in compartment_two:
                same_char = character
                break

        if same_char.islower():
            answer += ord(same_char) - 96
        else:
            answer += ord(same_char) - 38

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    for ruck_index in range(0, len(puzzle_input) - 1, 3):
        ruck_one, ruck_two, ruck_three = tuple(puzzle_input[ruck_index: ruck_index + 3])

        same_char = None
        for character in ruck_one:
            if character in ruck_two and character in ruck_three:
                same_char = character
                break

        if same_char.islower():
            answer += ord(same_char) - 96
        else:
            answer += ord(same_char) - 38

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for file in input_files:
        main(file)
