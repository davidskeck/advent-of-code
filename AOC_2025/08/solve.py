# Advent of Code 2025
# Day 08

import time
from math import sqrt, prod

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
    
    box_locs = []
    for line in puzzle_input:
        box_locs.append(tuple([int(loc) for loc in line.split(',')]))

    sorted_connections = {}
    for o_idx, o_box in enumerate(box_locs):
        for i_idx, i_box in enumerate(box_locs):
            if o_idx != i_idx:
                a = pow(i_box[0] - o_box[0], 2)
                b = pow(i_box[1] - o_box[1], 2)
                c = pow(i_box[2] - o_box[2], 2)
                curr_boxes = tuple(sorted([i_box, o_box]))
                if curr_boxes not in sorted_connections:
                    sorted_connections[curr_boxes] = sqrt(a + b + c)
    
    sorted_connections = dict(sorted(sorted_connections.items(), key=lambda entry: entry[1]))

    if "example" in input_file:
        num_connections = 10
    else:
        num_connections = 1000

    circuits = {loc: {loc} for loc in box_locs}
    for idx, curr_connection in enumerate(sorted_connections.keys()):
        curr_connection = list(curr_connection)
        for circuit_name in circuits:
            if curr_connection[0] in circuits[circuit_name]:
                circuit_one = circuit_name
            if curr_connection[1] in circuits[circuit_name]:
                circuit_two = circuit_name
        
        if circuit_one != circuit_two:
            circuits[circuit_one] |= circuits[circuit_two]
            del circuits[circuit_two]

        if idx == num_connections - 1:
            circuit_sizes = sorted(len(circuits[name]) for name in circuits)
            answer = prod(circuit_sizes[-3:])

            pyperclip.copy(answer)
            print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")
        
        if len(circuits) == 1:
            # Part Two
            answer = 0

            answer = curr_connection[0][0] * curr_connection[1][0]

            pyperclip.copy(answer)
            print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")
            break


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
