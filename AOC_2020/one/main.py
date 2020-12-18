def main():
    input_data = None
    with open("input.txt") as input:
        input_data = input.readlines()
    
    input_data = input_data[:-1]
    
    solution_found_p1 = False
    solution_found_p2 = False
    for first in input_data:
        if solution_found_p1 and solution_found_p2:
            break
        first = first.strip()
        for second in input_data[1:]:
            second = second.strip()
            if not solution_found_p1 and (int(first) + int(second) == 2020):
                print("Two expenses that equal 2020: ({} * {}) = {}".format(first, second, int(first) * int(second)))
                solution_found_p1 = True
            for third in input_data[2:]:
                third = third.strip()
                if not solution_found_p2 and (int(first) + int(second) + int(third) == 2020):
                    print("Three expenses that equal 2020 (p2): ({} * {} * {}) = {}".format(first, second, third, int(first) * int(second) * int(third)))
                    solution_found_p2 = True
                

if __name__ == "__main__":
    main()

