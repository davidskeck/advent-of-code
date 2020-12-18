def main():
    input_data = []
    with open("example.txt") as input:
        for line in input:
            input_data.append(line.strip())
    
    unique_count = 0
    unique_chars = []
    for line in input_data:
        if line != '':
            for char in line:
                if char not in unique_chars:
                    unique_chars.append(char)
        else:
            unique_count += len(unique_chars)
            unique_chars = []

    print("Total unique characters in all groups (p1): {}".format(unique_count))

if __name__ == "__main__":
    main()

