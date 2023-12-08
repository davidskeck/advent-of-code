# Advent of Code 2023
# Day 08

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

direction_dict = {
    'L': 0,
    'R': 1
}


class Node:
    def __init__(self, input_str):
        self.name = input_str.split()[0]
        self.elements = [element.strip("(),") for element in input_str.split()[2:]]


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    instructions = puzzle_input[0]
    nodes = []
    for line in puzzle_input:
        if '=' in line:
            nodes.append(Node(line))
    
    node_dict = {}
    for index, node in enumerate(nodes):
        node_dict[node.name] = node
    
    # end_found = False
    # current_node = None
    # for node in nodes:
    #     if node.name == "AAA":
    #         current_node = node
    #         break

    # while not end_found:
    #     for direction in list(instructions):
    #         answer += 1
    #         next_node_name = current_node.elements[direction_dict.get(direction)]
    #         for node in nodes:
    #             if node.name == next_node_name:
    #                 current_node = node
    #                 break
    #         if current_node.name == "ZZZ":
    #             end_found = True
    #             break

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    current_nodes = []
    for node in nodes:
        if node.name[-1] == "A":
            current_nodes.append(node)

    end_found = False
    while not end_found:
        for direction in list(instructions):
            answer += 1
            for index, curr_node in enumerate(current_nodes):
                next_node_name = curr_node.elements[direction_dict.get(direction)]
                current_nodes[index] = node_dict[next_node_name]
            all_end_in_z = True
            for node in current_nodes:
                if node.name[-1] != "Z":
                    all_end_in_z = False
                    break
            if all_end_in_z:
                end_found = True
                break

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
