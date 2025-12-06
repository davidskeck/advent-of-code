# Advent of Code 2025
# Day 06

import time

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
    
    problems = []
    operations = []
    for idx, line in enumerate(puzzle_input):
        if idx < len(puzzle_input) - 1:
            problem_slice = line.split()
            if idx == 0:
                for curr_slice in problem_slice:
                    problems.append([curr_slice])
            else:
                for idx, curr_slice in enumerate(problem_slice):
                    problems[idx] += [curr_slice]
        else:
            operations = line.split()
    
    problems = list(zip(operations, problems))

    for problem in problems:
        operation, values = problem
        calculation = operation.join(values)
        answer += eval(calculation)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    problems = []
    operations = reversed(puzzle_input[-1].split())
    
    curr_problem = []
    puzzle_width = len(puzzle_input[0])
    for i in reversed(range(puzzle_width)):
        curr_num = ""
        for j in range(len(puzzle_input) - 1):
            curr_char = puzzle_input[j][i]
            curr_num += curr_char
        if curr_num.strip() != "" or i == 0:
            curr_problem.append(curr_num)
            if i == 0:
                problems.append(curr_problem)
        else:
            problems.append(curr_problem)
            curr_problem = []
    
    problems = list(zip(operations, problems))

    for problem in problems:
        operation, values = problem
        calculation = operation.join(values)
        answer += eval(calculation)

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
