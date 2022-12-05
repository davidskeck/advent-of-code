# Advent of Code 2022
# Day 5

import copy
import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = ""
    stack_data = []
    instructions = []
    for line in puzzle_input:
        if "move" not in line:
            stack_data.append(line)
        else:
            instructions.append(line.strip())

    stacks = {}
    for stack_name in stack_data[-1].split():
        stacks[int(stack_name)] = []

    for stack_contents in stack_data[:-1]:
        for i in range (0, len(stack_contents), 4):
            crate = stack_contents[i:i+4].strip()
            if crate != '':
                current_stack = stacks[i // 4 + 1]
                current_stack.insert(0, crate.strip("[]"))

    moveable_stacks = copy.deepcopy(stacks)
    for instruction in instructions:
        instruction = instruction.split()
        number_to_move = int(instruction[1])
        from_stack = int(instruction[3])
        to_stack = int(instruction[-1])

        from_stack = moveable_stacks[from_stack]
        to_stack = moveable_stacks[to_stack]
        for i in range(number_to_move):
            crate = from_stack.pop()
            to_stack.append(crate)

    for stack in moveable_stacks.values():
        answer += stack[-1]

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = ""

    moveable_stacks = copy.deepcopy(stacks)
    for instruction in instructions:
        instruction = instruction.split()
        number_to_move = int(instruction[1])
        from_stack = int(instruction[3])
        to_stack = int(instruction[-1])

        from_stack = moveable_stacks[from_stack]
        to_stack = moveable_stacks[to_stack]
        to_stack.extend(from_stack[-number_to_move:])
        del from_stack[-number_to_move:]

    for stack in moveable_stacks.values():
        answer += stack[-1]

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for file in input_files:
        main(file)
