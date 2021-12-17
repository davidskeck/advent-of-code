# Advent of Code 2021
# Day 14

import os
from collections import Counter


def apply_rule(start, rule):
    pattern, insert = rule.split("->")
    pattern_index = start.find(pattern.strip())
    result = []
    while pattern_index != -1:
        result.append((insert.strip(), pattern_index))
        pattern_index = start.find(pattern.strip(), pattern_index + 1)

    return result


def main():
    with open(f"input{os.sep}day14.txt") as puzzle_data:
        puzzle_input = puzzle_data.readlines()

    start = ""
    rules = []
    for index, rule in enumerate(puzzle_input):
        rule = rule.strip()
        if len(rule) > 0:
            if index == 0:
                start = rule
            else:
                rules.append(rule)
    
    steps = 40 
    polymer = start
    for step in range(steps):
        modifications = []
        for rule in rules:
            result = apply_rule(polymer, rule)
            if result:
                modifications.extend(result)
        
        modifications.sort(key=lambda y: y[1])
        index_diff = 0
        for mod in modifications:
            insert, index = mod
            index = index + 1 + index_diff
            polymer = polymer[:index] + insert + polymer[index:]
            index_diff += len(insert)

    poly_counter = Counter(polymer)
    most_common = poly_counter.most_common()[0]
    least_common = poly_counter.most_common()[-1]

    print(f"Part One: {most_common[1] - least_common[1]}")
    
#    print(f"Part Two: {}")


if __name__ == "__main__":
    main()

