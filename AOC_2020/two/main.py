def main():
    input_data = None
    with open("input.txt") as input:
        input_data = input.readlines()
    
    input_data = input_data[:-1]
    
    solution_one_count = 0
    solution_two_count = 0
    for entry in input_data:
        entry = entry.strip()
        letterRange = entry.split()[0]
        minNum = int(letterRange.split('-')[0])
        maxNum = int(letterRange.split('-')[1])
        letter = entry.split()[1].strip(':')
        password = entry.split()[2].strip()
        if minNum <= password.count(letter) <= maxNum:
            solution_one_count += 1
        
        indexOne = minNum - 1
        indexTwo = maxNum - 1
        if (password[indexOne] == letter or password[indexTwo] == letter) and password[indexOne] != password[indexTwo]:  
            solution_two_count += 1
    
    print("Number of correct passwords (p1): {}".format(solution_one_count))
    print("Number of correct passwords (p2): {}".format(solution_two_count))


if __name__ == "__main__":
    main()

