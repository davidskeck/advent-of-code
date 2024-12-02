# Advent of Code 2023
# Day 19

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


STARTING_WF = "in"
REJECTED = "R"
ACCEPTED = "A"


class Rule:
    def __init__(self, data):
        self.final = False
        if ':' in data:
            self.condition = data.split(':')[0]
            self.var = self.condition[0]
            self.comparator = self.condition[1]
            self.val = int(self.condition[2:])
            self.result = data.split(':')[1]
        else:
            self.final = True
            self.result = data


class Workflow:
    def __init__(self, data):
        self.name = data.split('{')[0]
        self.rules = []

        for rule in data.split('{')[1].strip('{}').split(','):
            self.rules.append(Rule(rule))

        self.accepted = False


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    
    workflows = []
    ratings = []
    for line in puzzle_input:
        if line[0] == '{':
            ratings.append(line)
        else:
            workflows.append(Workflow(line))

    starting_workflow = None
    for workflow in workflows:
        if workflow.name == STARTING_WF:
            starting_workflow = workflow

    for rating in ratings:
        curr_workflow = starting_workflow
        steps = rating.strip('{}').split(',')
        step_values = {}
        for step in steps:
            var, val = step.split('=')
            step_values[var] = int(val)

        result_found = False
        while not result_found:
            for rule in curr_workflow.rules:
                if not rule.final:
                    curr_val = step_values[rule.var]
                    if eval(f"{curr_val}{rule.comparator}{rule.val}"):
                        if rule.result == ACCEPTED:
                            workflow.accepted = True
                            for key, val in step_values.items():
                                answer += val
                            result_found = True
                            break
                        elif rule.result == REJECTED:
                            workflow.accepted = False
                            result_found = True
                            break
                        else:
                            for workflow in workflows:
                                if workflow.name == rule.result:
                                    curr_workflow = workflow
                                    break
                            break
                else:
                    if rule.result == ACCEPTED:
                        workflow.accepted = True
                        for key, val in step_values.items():
                            answer += val
                        result_found = True
                        break
                    elif rule.result == REJECTED:
                        workflow.accepted = False
                        result_found = True
                        break
                    else:
                        for workflow in workflows:
                            if workflow.name == rule.result:
                                curr_workflow = workflow
                                break
                        break


    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
