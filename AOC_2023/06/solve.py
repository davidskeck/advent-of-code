# Advent of Code 2023
# Day 06

import time

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]

class Race:
    def __init__(self, race_data):
        self.time = race_data[0]
        self.distance_record = race_data[1]

        self.possible_distances = []
        for i in range(0, self.time + 1):
            self.possible_distances.append((i * (self.time - i)))
        
        self.total_wins = 0
        for distance in self.possible_distances:
            if distance > self.distance_record:
                self.total_wins += 1


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0
    races = []
    times = []
    distances = []
    for line in puzzle_input:
        if "Time" in line:
            times = line.split(':')[-1].split()
        if "Distance" in line:
            distances = line.split(':')[-1].split()
    
    for index, time in enumerate(times):
        races.append(Race((int(time), int(distances[index]))))

    answer = 1
    for race in races:
        answer *= race.total_wins

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0
    time = int("".join(times))
    distance = int("".join(distances))
    actual_race = Race((time, distance))
    answer = actual_race.total_wins

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
