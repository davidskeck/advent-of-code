# Advent of Code 2022
# Day 10

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

CRT_WIDTH = 40


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    register_x = 1
    cycle_count = 0
    signal_strengths = []
    crt_display = [[] for i in range(7)]

    def execute_cycle():
        nonlocal cycle_count
        crt_row = cycle_count // CRT_WIDTH
        crt_pixel = cycle_count % CRT_WIDTH
        sprite_overlaps = register_x + 1 >= crt_pixel >= register_x - 1
        if sprite_overlaps:
            crt_display[crt_row].append('#')
        else:
            crt_display[crt_row].append(' ')
        
        cycle_count += 1
        if cycle_count == 20 or (cycle_count - 20) % 40 == 0:
            signal_strengths.append(cycle_count * register_x)
 
    for instruction in puzzle_input:
        if instruction == 'noop':
            execute_cycle()
        else:
            execute_cycle()
            execute_cycle()
            value = int(instruction.split()[-1])
            register_x += value
    answer = sum(signal_strengths)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = "\n"
    for row in crt_display:
        full_row = ""
        for char in row:
            full_row += char
        answer += full_row + '\n'
    
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
