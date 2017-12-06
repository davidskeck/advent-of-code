# NOTE: Did receive some help on this puzzle
import urllib.request as urllib


def main():
    puzzle_input = 325489

    # Part One
    # I solved this without using code.
    # The lower right corner of the spiral memory is always a perfect odd square.
    # Knowing this, you can calculate the smallest value that is larger than the
    # puzzle input and then count backwards to find the final position relative
    # to the center of the spiral.

    print("It will take 552 steps.")

    # Part Two
    # Look up solution in data table at https://oeis.org/A141481/b141481.txt

    link = "https://oeis.org/A141481/b141481.txt"
    f = urllib.urlopen(link)
    pattern_list = f.read().decode('utf-8')
    pattern_list = pattern_list.split()

    for index, data in enumerate(pattern_list):
        try:
            if int(data) > puzzle_input:
                print("The first larger value is:", pattern_list[index])
                break
        except ValueError:
            pass


main()
