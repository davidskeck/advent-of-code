# Advent of Code 2023
# Day 15

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

def run_hash(data):
    current_value = 0
    for index, char in enumerate(data):
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


class Step:
    def __init__(self, data):
        self.data = data
        self.current_value = 0
        for index, char in enumerate(data):
            self.current_value += ord(char)
            self.current_value *= 17
            self.current_value %= 256
        
        self.label = self.data.split('=')[0].split('-')[0]
        self.box_id = run_hash(self.label)
        self.focal_length = None
        if "=" in self.data:
            self.focal_length = int(self.data.split('=')[1])


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line.strip() for line in input_data.read().split(',') if line != ""]

    # Part One
    answer = 0

    steps = []
    for line in puzzle_input:
        steps.append(Step(line))

    for step in steps:
        answer += step.current_value

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    box_dict = dict.fromkeys(range(256))
    for i in range(256):
        box_dict[i] = []
    for step in steps:
        curr_lenses = box_dict[step.box_id]
        if step.focal_length is None:
            updated_lenses = []
            for lens in curr_lenses:
                if step.label in lens:
                    continue
                updated_lenses.append(lens)
            box_dict[step.box_id] = updated_lenses
        else:
            updated_lens = False
            updated_lenses = []
            for lens in curr_lenses:
                if step.label in lens:
                    updated_lenses.append(f"{step.label} {step.focal_length}")
                    updated_lens = True
                    continue
                updated_lenses.append(lens)
            if updated_lens:
                box_dict[step.box_id] = updated_lenses
            else:
                curr_lenses.append(f"{step.label} {step.focal_length}")
                box_dict[step.box_id] = curr_lenses

    for box_id, lenses in box_dict.items():
        for slot, lens in enumerate(lenses):
            answer += (box_id + 1) * (slot + 1) * int(lens.split()[-1])

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
