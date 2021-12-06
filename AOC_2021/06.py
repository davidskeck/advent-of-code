# Advent of Code 2021
# Day 6

import os
from collections import Counter

EXAMPLE_DAYS = 18
PART_ONE_DAYS = 80
PART_TWO_DAYS = 256


def simulate_population(population, days):
    for i in range(days):
        new_pop = dict.fromkeys(range(9), 0)
        
        new_pop[8] = population[0]
        
        for key, val in population.items():
            if key > 0:
                new_pop[key - 1] = val
        
        new_pop[6] += population[0]

        population = new_pop
            
    return population


def main():
    with open(f"input{os.sep}day06.txt") as puzzle_data:
        puzzle_input = [int(timer) for timer in puzzle_data.read().split(',')]
    
    lantern_timers = Counter(puzzle_input)
    lantern_timers.update({6: 0, 7: 0, 8: 0, 0: 0})

    population = simulate_population(lantern_timers, PART_ONE_DAYS)
    
    total_fish = 0
    for key, val in population.items():
        total_fish += val
    
    print(f"Part Two: {total_fish}")

    population = simulate_population(population, PART_TWO_DAYS - PART_ONE_DAYS)
    
    total_fish = 0
    for key, val in population.items():
        total_fish += val
    
    print(f"Part Two: {total_fish}")


if __name__ == "__main__":
    main()

