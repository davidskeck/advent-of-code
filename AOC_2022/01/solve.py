# Advent of Code 2022
# Day 1


def main():
    with open("input.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().split('\n')  # Interestingly have to split on just the newline here... Otherwise you can't tell when one elf's calorie count ends and another starts.

    calorie_counts = []
    current_cals = 0
    for input in puzzle_input:
        if input != '':
            current_cals += int(input)
        else:
            calorie_counts.append(current_cals)
            current_cals = 0

    sorted_calories = sorted(calorie_counts)
    print(f"The most calories carried by an elf is: {sorted_calories[-1]}.")
    print(f"The sum of the calories carried by the top three elves is: {sum(sorted_calories[-3:])}.")


if __name__ == "__main__":
    main()
