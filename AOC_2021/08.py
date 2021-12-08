# Advent of Code 2021
# Day 8

import os


ONE_SEG_CNT = 2
FOUR_SEG_CNT = 4
SEVEN_SEG_CNT = 3
EIGHT_SEG_CNT = 7


def find_pattern_from_int(digit, pattern_dict):
    for key, value in pattern_dict.items():
        if value == digit:
            return key


def search_patterns_dict(input_pattern, pattern_dict):
    for key, value in pattern_dict.items():
        if set(list(input_pattern)) == set(list(key)):
            return value


def unscramble_output(note):
    patterns, output = note
    pattern_dict = {}
    for pattern in patterns:
        pattern_len = len(pattern)
        if pattern_len == ONE_SEG_CNT:
            pattern_dict[pattern] = 1
        elif pattern_len == FOUR_SEG_CNT:
            pattern_dict[pattern] = 4
        elif pattern_len == SEVEN_SEG_CNT:
            pattern_dict[pattern] = 7
        elif pattern_len == EIGHT_SEG_CNT:
            pattern_dict[pattern] = 8

    while len(pattern_dict) != 10:
        for pattern in patterns:
            if len(pattern) == 6:
                four_pattern = find_pattern_from_int(4, pattern_dict)
                one_pattern = find_pattern_from_int(1, pattern_dict)
                if four_pattern and len(set(list(pattern)) & set(list(four_pattern))) == 4:
                    pattern_dict[pattern] = 9
                elif one_pattern and len(set(list(pattern)) & set(list(one_pattern))) == 2:
                    pattern_dict[pattern] = 0

                if one_pattern and len(set(list(pattern)) & set(list(one_pattern))) == 1:
                    pattern_dict[pattern] = 6

            elif len(pattern) == 5:
                six_pattern = find_pattern_from_int(6, pattern_dict)
                five_pattern = find_pattern_from_int(5, pattern_dict)
                if five_pattern and len(set(list(pattern)) & set(list(five_pattern))) == 3:
                    pattern_dict[pattern] = 2
                elif five_pattern:
                    pattern_dict[pattern] = 3
                
                if six_pattern and len(set(list(pattern)) & set(list(six_pattern))) == 5:
                    pattern_dict[pattern] = 5
                

    output_str = ""
    for num in output:
        actual_value = search_patterns_dict(num, pattern_dict)
        if actual_value is not None:
            output_str += str(actual_value)
        else:
            print(f"Unknown value for {num} in {pattern_dict}")
    
    if len(output_str) > 0:
        return (int(output_str))


def main():
    with open(f"input{os.sep}day08.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().strip().split('\n')
    
    display_notes = []
    for line in puzzle_input:
        patterns = line.split('|')[0].split()
        outputs = line.split('|')[1].split()
        display_notes.append((patterns, outputs))

    unique_segments_count = 0
    for note in display_notes:
        for output in note[1]:
            output_len = len(output)
            if output_len == ONE_SEG_CNT or output_len == FOUR_SEG_CNT or output_len == SEVEN_SEG_CNT or output_len == EIGHT_SEG_CNT:
                unique_segments_count += 1
 
    print(f"Part One: {unique_segments_count}")
   
    total_value = 0 
    for note in display_notes:
        total_value += unscramble_output(note)
     
    print(f"Part Two: {total_value}")


if __name__ == "__main__":
    main()

