# Advent of Code 2023
# Day 08

import time

import pyperclip
import numpy as np


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
    
    
    current_node = node_dict["AAA"]
    end_found = False
    while not end_found:
        for direction in list(instructions):
            answer += 1
            next_node_name = current_node.elements[direction_dict.get(direction)]
            
            if next_node_name == "ZZZ":
                end_found = True
                break
            else:
                current_node = node_dict[next_node_name]

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    if input_file == "example.txt":
        input_file = "example_p2.txt"
        with open(input_file) as input_data:
            puzzle_input = [line for line in input_data.read().split('\n') if line != ""]
        
        instructions = puzzle_input[0]
        nodes = []
        for line in puzzle_input:
            if '=' in line:
                nodes.append(Node(line))
        
        node_dict = {}
        for index, node in enumerate(nodes):
            node_dict[node.name] = node

    answer = 0

    current_nodes = []
    for node in nodes:
        if node.name[-1] == "A":
            current_nodes.append((node, None))

    end_found = False
    while not end_found:
        for direction in list(instructions):
            answer += 1
            end_found = True
            for index, curr_node in enumerate(current_nodes):
                curr_node, distance = curr_node
                if distance is None:
                    end_found = False
                    next_node_name = curr_node.elements[direction_dict.get(direction)]
                    if next_node_name[-1] == "Z":
                        distance = answer
                    current_nodes[index] = (node_dict[next_node_name], distance)
    
    multiples = [curr_node[1] for curr_node in current_nodes]
    answer = int(np.lcm.reduce(multiples))

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
