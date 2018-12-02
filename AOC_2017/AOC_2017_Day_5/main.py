def main():
    puzzle_input = open("puzzle_input.txt")
    puzzle_input_list = []

    for data in puzzle_input:
        puzzle_input_list.append(int(data))

    puzzle_input.close()

    # Part One
    number_of_jumps = 0
    current_index = 0
    part_one_puzzle_input = puzzle_input_list[:]  # Use [:] to make a copy
    while True:
        try:
            index_value = part_one_puzzle_input[current_index]
            part_one_puzzle_input[current_index] += 1
            current_index += index_value
            number_of_jumps += 1
            if current_index > len(part_one_puzzle_input):
                raise IndexError
        except IndexError:
            print("You took {} jumps.".format(number_of_jumps))
            break

    # Part Two
    number_of_jumps = 0
    current_index = 0
    part_two_puzzle_input = puzzle_input_list[:]  # Use [:] to make a copy
    while True:
        try:
            index_value = part_two_puzzle_input[current_index]
            if index_value >= 3:
                part_two_puzzle_input[current_index] -= 1
            else:
                part_two_puzzle_input[current_index] += 1

            current_index += index_value
            number_of_jumps += 1
            if current_index > len(part_two_puzzle_input):
                raise IndexError
        except IndexError:
            print("You took {} jumps.".format(number_of_jumps))
            break


main()
