# Advent of Code 2021
# Day 10

import os


def main():
    with open(f"input{os.sep}day10.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().split()
    
    char_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']
    
    illegal_chars = []
    incomplete_openers = []
    for line in puzzle_input:
        pending_openers = []
        line_corrupt = False
        for index, char in enumerate(line):
            if char in openers:
                pending_openers.append(char)
            elif char in closers:
                if pending_openers[-1] == openers[closers.index(char)]:
                    pending_openers.pop()
                else:
                    illegal_chars.append(char)
                    break

            if index == len(line) - 1:
                incomplete_openers.append(pending_openers)

    p1_score = 0
    for char in illegal_chars:
        p1_score += char_scores[char]
    
    print(f"Part One: {p1_score}")
    
    auto_complete_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
        
    completion_strings = []
    for opener_set in incomplete_openers:
        repair_string = ""
        for char in reversed(opener_set):
            repair_string += closers[openers.index(char)]

        completion_strings.append(repair_string)
    
    completion_scores = []
    for completion in completion_strings:
        score = 0
        for char in completion:
            score *= 5
            score += auto_complete_scores[char]
        completion_scores.append(score)

    completion_scores.sort()
    print(f"Part Two: {completion_scores[int(len(completion_scores) / 2)]}")


if __name__ == "__main__":
    main()

