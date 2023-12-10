# Advent of Code 2023
# Day 09

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

class Sequence:
    def __init__(self, input_values):
        self.values = [int(val) for val in input_values.split()]
        self.differences = []
        
        at_end = False
        at_end = self.compute_differences(self.values)

        while not at_end:
            at_end = self.compute_differences(self.differences[-1])
        
        self.differences.reverse()
        for index, diff_list in enumerate(self.differences):
            if index < len(self.differences) - 1:
                next_diff = diff_list[-1] + self.differences[index + 1][-1]
                prev_diff = self.differences[index + 1][0] - diff_list[0]
                self.differences[index + 1] = [prev_diff] + self.differences[index + 1] + [next_diff]
        self.differences.reverse()

        self.next_value = self.values[-1] + self.differences[0][-1]
        self.prev_value = self.values[0] - self.differences[0][0]

    def compute_differences(self, input_data):
        diffs = []
        for i in range(len(input_data) - 1):
            diffs.append(input_data[i+1] - input_data[i])
        
        if not all(val == 0 for val in diffs):
            self.differences.append(diffs)
        else:
            self.differences.append([0] + diffs + [0])
            return True


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    sequences = []
    for line in puzzle_input:
        sequences.append(Sequence(line))
    
    for sequence in sequences:
        answer += sequence.next_value

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    for sequence in sequences:
        answer += sequence.prev_value

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
