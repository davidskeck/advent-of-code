# Advent of Code 2022
# Day 2


input_file = "input.txt"
#input_file = "example.txt"

play_dict = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def main():
    with open(input_file) as puzzle_data:
        puzzle_input = puzzle_data.read().split('\n')

    total_score = 0
    for round in puzzle_input:
        round = round.split()
        if len(round) > 0:
            opponent, selected = tuple(round)
            total_score += play_dict[selected]
            if play_dict[selected] == play_dict[opponent]:
                total_score += 3
            elif selected == "X" and opponent == "C":
                total_score += 6
            elif selected == "Y" and opponent == "A":
                total_score += 6
            elif selected == "Z" and opponent == "B":
                total_score += 6

    print(f"Total score is: {total_score}")

    total_score = 0
    for round in puzzle_input:
        round = round.split()
        if len(round) > 0:
            opponent, desired_outcome = tuple(round)

            if desired_outcome == "Y":
                total_score += 3
                selected = opponent
            elif desired_outcome == "Z":
                total_score += 6
                if opponent == "A":
                    selected = "B"
                elif opponent == "B":
                    selected = "C"
                elif opponent == "C":
                    selected = "A"
            else:
                if opponent == "A":
                    selected = "C"
                elif opponent == "B":
                    selected = "A"
                elif opponent == "C":
                    selected = "B"

            total_score += play_dict[selected]

    print(f"Total score is: {total_score}")


if __name__ == "__main__":
    main()
