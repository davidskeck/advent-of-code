# Advent of Code 2021
# Day 3

import os


def main():
    with open(f"input{os.sep}day03.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().split()
    
    ones_accumulator = len(puzzle_input[0]) * [0]    
    for value in puzzle_input:
        for index, number in enumerate(value):
             if int(number) == 1:
                ones_accumulator[index] += 1
    
    gamma_rate_binary = ""
    epsilon_rate_binary = ""
    half_size_input = len(puzzle_input) / 2
    for index, value in enumerate(ones_accumulator):
        if value > half_size_input:
            gamma_rate_binary += "1"
            epsilon_rate_binary  += "0"
        elif value < half_size_input:
            gamma_rate_binary  += "0"
            epsilon_rate_binary  += "1"
        else:
            print(f"Error: Values occur at same rate for index {index}.")
    gamma_rate = int(gamma_rate_binary, 2)
    epsilon_rate = int(epsilon_rate_binary, 2)

    print(f"Part One: {gamma_rate * epsilon_rate}")
    
    o2_result = 0
    co2_result = 0  
    o2_result_set = puzzle_input
    co2_result_set = puzzle_input
    for index in range(len(o2_result_set[0])):
        o2_accumulator = 0 
        co2_accumulator = 0
 
        for value in o2_result_set:
            if int(value[index]) == 1:
                o2_accumulator += 1
        
        for value in co2_result_set:
            if int(value[index]) == 1:
                co2_accumulator += 1

        if o2_accumulator >= len(o2_result_set) / 2:
            o2_bit = 1
        else:
            o2_bit = 0
        
        if co2_accumulator >= len(co2_result_set) / 2:
            co2_bit = 0
        else:
            co2_bit = 1
        
        temp_o2_set = []
        temp_co2_set = []
        for value in o2_result_set:
            if int(value[index]) == o2_bit:
                temp_o2_set.append(value)
        
        for value in co2_result_set:
            if int(value[index]) == co2_bit:
                temp_co2_set.append(value)
        
        o2_result_set = temp_o2_set
        co2_result_set = temp_co2_set

        if len(o2_result_set) == 1 and o2_result == 0:
            o2_result = int(o2_result_set[0], 2)
        
        if len(co2_result_set) == 1 and co2_result == 0:
            co2_result = int(co2_result_set[0], 2)
 
    print(f"Part Two: {o2_result * co2_result}")


if __name__ == "__main__":
    main()

