# Advent of Code 2022
# Day 11

import time
import copy
import math

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

class Monkey:
    def __init__(self, monkey_text):
        self.this_id = int(monkey_text[0].strip(':').split()[-1])
        self.worry_levels = []
        worry_string = monkey_text[1].split(':')[-1]
        for level in worry_string.split(','):
            self.worry_levels.append(int(level))
        self.operation = monkey_text[2].split("=")[-1]
        test = monkey_text[3:]
        self.divisible_by = int(test[0].split()[-1])
        self.if_true_monkey = int(test[1].split()[-1])
        self.if_false_monkey = int(test[2].split()[-1])
        self.items_to_throw = []
        self.number_of_inspections = 0

    def inspect(self, part_one=False):
        for index, level in enumerate(self.worry_levels):
            old = level
            operation = self.operation.strip()[3:]
            self.worry_levels[index] = eval(f"{old} {operation}", locals())
            if part_one:
                self.worry_levels[index] //= 3
            self.number_of_inspections += 1

    def run_test(self):
        for item in self.worry_levels:
            if item % self.divisible_by == 0:
                self.items_to_throw.append((self.if_true_monkey, item))
            else:
                self.items_to_throw.append((self.if_false_monkey, item))
        self.worry_levels = []

    def clear_thrown_items(self):
        self.items_to_throw = []

    def accept_throw_item(self, item):
        self.worry_levels.append(item)



def main(input_file):
    with open(input_file) as puzzle_data:
        puzzle_input = [line for line in puzzle_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    monkeys_dict = {}
    monkey_text = []
    least_common_multiple = 1

    for line in puzzle_input:
        monkey_text.append(line)
        if "false" in line:
            monkey = Monkey(monkey_text)
            monkeys_dict[monkey.this_id] = monkey
            monkey_text = []

    monkeys = copy.deepcopy(monkeys_dict)

    for i in range(20):
        for monkey in monkeys.values():
            monkey.inspect(part_one=True)
            monkey.run_test()
            items_to_throw = monkey.items_to_throw
            for item_data in items_to_throw:
                monkey_id, item = item_data
                monkeys[monkey_id].accept_throw_item(item)
            monkey.clear_thrown_items()

    monkey_activity = [monkey.number_of_inspections for monkey in monkeys.values()]

    answer = math.prod(sorted(monkey_activity)[-2:])

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    monkeys = copy.deepcopy(monkeys_dict)

    for monkey in monkeys.values():
        least_common_multiple *= monkey.divisible_by

    for i in range(10000):
        for monkey in monkeys.values():
            monkey.inspect()
            monkey.run_test()
            items_to_throw = monkey.items_to_throw
            for item_data in items_to_throw:
                monkey_id, item = item_data
                item %= least_common_multiple
                monkeys[monkey_id].accept_throw_item(item)
            monkey.clear_thrown_items()

    monkey_activity = [monkey.number_of_inspections for monkey in monkeys.values()]

    answer = math.prod(sorted(monkey_activity)[-2:])
    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for file in input_files:
        start_time = time.time()
        main(file)
        print(f"{file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
