# Advent of Code 2022
# Day 13

import time
import copy

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

class PacketPair:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def packet_less_than(left, right):
    is_in_order = True
    min_length =  min(len(left), len(right))

    if min_length == 0:
        if len(left) > len(right):
            is_in_order = False
        elif len(left) < len(right):
            is_in_order = True
        else:
            is_in_order = None
    else:
        for i in range(min_length):
            left_val = left[i]
            right_val = right[i]

            if isinstance(left_val, int) and isinstance(right_val, int):
                if left_val > right_val:
                    is_in_order = False
                    break
                if left_val == right_val:
                    is_in_order = None
                else:
                    is_in_order = True
                    break
            else:
                if isinstance(right_val, int):
                    right_val = [right_val]
                elif isinstance(left_val, int):
                    left_val = [left_val]

                if isinstance(left_val, list) and isinstance(right_val, list):
                    is_in_order = packet_less_than(left_val, right_val)
                    if is_in_order is not None:
                        break

        if is_in_order == None:
            if len(left) > len(right):
                is_in_order = False
            elif len(left) < len(right):
                is_in_order = True

    return is_in_order


def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    packet_pairs = []
    for index in range(0, len(puzzle_input), 2):
        left = eval(puzzle_input[index])
        right = eval(puzzle_input[index + 1])
        packet_pairs.append(PacketPair(left, right))

    indices_of_correct_pairs = []
    for index, pair in enumerate(packet_pairs):
        if packet_less_than(pair.left, pair.right):
            indices_of_correct_pairs.append(index + 1)

    answer = sum(indices_of_correct_pairs)
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    divider_packets = [[[2]], [[6]]]
    total_packets = [eval(line) for line in puzzle_input] + divider_packets
    sorted_packets = copy.deepcopy(total_packets)

    for completed_packets in range(len(sorted_packets)):
        swap_occurred = False
        for index in range(len(sorted_packets) - 1 - completed_packets):
            if not packet_less_than(sorted_packets[index], sorted_packets[index + 1]):
                temp_packet = sorted_packets.pop(index)
                sorted_packets.insert(index + 1, temp_packet)
                swap_occurred = True
        if not swap_occurred:
            break

    answer = sorted_packets.index(divider_packets[0]) + 1
    answer *= sorted_packets.index(divider_packets[1]) + 1
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
