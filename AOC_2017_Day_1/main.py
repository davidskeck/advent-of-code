def main():
    puzzle_input = open("puzzle_input.txt")
    puzzle_input_list = []

    for line in puzzle_input:
        for number in line:
            puzzle_input_list.append(number)

    puzzle_input.close()

    # Part One
    previous_number = 0
    captcha = 0
    for index, number in enumerate(puzzle_input_list):
        if number == previous_number:
            captcha += int(number)
        if (len(puzzle_input_list) - 1) == index:
            if number == puzzle_input_list[0]:
                captcha += int(number)
        previous_number = number

    print("The first captcha is:", captcha)

    # Part Two
    captcha = 0
    halfway = len(puzzle_input_list) / 2

    for index, number in enumerate(puzzle_input_list):
        if index < halfway:
            halfway_index = int(halfway + index)
        else:
            halfway_index = int(halfway + index) - len(puzzle_input_list)

        opposite_number = puzzle_input_list[halfway_index]
        if number == opposite_number:
            captcha += int(number)

    print("The second captcha is:", captcha)


main()
