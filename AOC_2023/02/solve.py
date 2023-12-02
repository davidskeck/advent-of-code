# Advent of Code 2023
# Day 02

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

part_one_constraints = {
    "red": 12,
    "green": 13,
    "blue": 14
}


class GameData:
    def __init__(self, data_str):
        self.id = int(data_str.split()[1].strip(':'))
        self.cube_grabs = []
        cube_data = [grab.strip() for grab in data_str[data_str.index(':')+1:].split(';')]
        for random_grab in cube_data:
            grabs = random_grab.split(',')
            for grab in grabs:
                grab = grab.strip().split()
                self.cube_grabs.append([grab[-1], int(grab[0])])

        self.min_cube_counts = {}
        self.satisfies_p1_contraints = True
        for grab in self.cube_grabs:
            curr_col, curr_count = tuple(grab)
            for color, count in part_one_constraints.items():
                if curr_col == color and curr_count > count:
                    self.satisfies_p1_contraints = False
        
            if curr_col in self.min_cube_counts:
                if self.min_cube_counts[curr_col] < curr_count:
                    self.min_cube_counts[curr_col] = curr_count
            else:
                self.min_cube_counts[curr_col] = curr_count
        
        self.power = 1
        for count in self.min_cube_counts.values():
            self.power *= count


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0

    game_data = []
    for game in puzzle_input:
        game_data.append(GameData(game))
    
    for game in game_data:
        if game.satisfies_p1_contraints:
            answer += game.id

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    for game in game_data:
        answer += game.power

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for puzzle_file in input_files:
        start_time = time.time()
        main(puzzle_file)
        print(f"{puzzle_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
