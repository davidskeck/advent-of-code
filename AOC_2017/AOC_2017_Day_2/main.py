def main():

    puzzle_input = open("puzzle_input.txt")
    puzzle_input_list = []

    for line in puzzle_input:
        puzzle_input_list.append(line.strip('\n').split('\t'))

    puzzle_input.close()

    # Part One
    spreadsheet_checksum = 0

    for line in puzzle_input_list:
        first_run = True

        smallest = 0
        largest = 0
        for num in line:
            if first_run:
                smallest = int(num)
                largest = int(num)
                first_run = False
            if int(num) > largest:
                largest = int(num)
            if int(num) < smallest:
                smallest = int(num)
        spreadsheet_checksum += int(largest) - int(smallest)

    print("The spreadsheet checksum is:", spreadsheet_checksum)

    # Part Two
    sum_of_divisor_results = 0

    for index, line in enumerate(puzzle_input_list):
        for num_index, num in enumerate(line):
            for iter_index, iter_num in enumerate(puzzle_input_list[index]):
                if int(num) % int(iter_num) == 0 and num_index != iter_index:
                    sum_of_divisor_results += int(int(num) / int(iter_num))
                    break

    print("The sum of each row's result is:", sum_of_divisor_results)


main()
