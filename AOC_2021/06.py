# Advent of Code 2021
# Day 6

import os
from multiprocessing.pool import Pool


EXAMPLE_DAYS = 18
PART_ONE_DAYS = 80
PART_TWO_DAYS = 256

class LanternFish:
    def __init__(self, age):
        self.age = age
        self.should_create_newborn = False

    def step(self):
        if self.age == 0:
            self.age = 6
            self.should_create_newborn = True
        else: 
            self.age -= 1


def run_lanternfish_sim(population, days=PART_TWO_DAYS):
    lantern_fish = population
    
    for i in range(days):
        newborns = []
        for fish in lantern_fish:
            fish.step()
            
            if fish.should_create_newborn:
                newborns.append(LanternFish(8))
                fish.should_create_newborn = False
        lantern_fish.extend(newborns)

    return len(lantern_fish)


def main():
    pool = Pool(processes=8)
    with open(f"input{os.sep}day06.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().split(',')
    
    lantern_fish = []
    for age in puzzle_input:
        lantern_fish.append(LanternFish(int(age)))

    split_populations = []
    num_processes = 8
    minimum_slice_size = int(len(lantern_fish) / num_processes)
    for i in range(num_processes):
        if i < num_processes - 1:
            split_populations.append(lantern_fish[i * minimum_slice_size: i * minimum_slice_size + minimum_slice_size])
        else:
            split_populations.append(lantern_fish[i * minimum_slice_size:])
    for pop in split_populations:
        print(len(pop))
    results = pool.map(run_lanternfish_sim, split_populations)

    total_fish = 0
    for result in results:
        total_fish += result
    #total_fish = run_lanternfish_sim(lantern_fish, PART_TWO_DAYS)    
 
    print(f"Part One: {total_fish}")
    
#    print(f"Part Two: {}")


if __name__ == "__main__":
    main()

