import hashlib


def decrypt_door_one(puzzle_input):
    password = ""
    current_iteration = 0
    characters_found = 0

    while characters_found != 8:
        current_puzzle_input = puzzle_input + str(current_iteration)
        first_six_characters = (hashlib.md5(current_puzzle_input.encode()).hexdigest())[0: 6]
        current_iteration += 1

        if first_six_characters[0: 5] == "00000":
            characters_found += 1
            password += first_six_characters[5: 6]

    print "Door one password is: " + password


def decrypt_door_two(puzzle_input):
    password = "00000000"
    current_iteration = 0
    characters_found = 0
    invalid_positions = []

    while characters_found != 8:
        current_puzzle_input = puzzle_input + str(current_iteration)
        first_seven_characters = (hashlib.md5(current_puzzle_input.encode()).hexdigest())[0: 7]
        current_iteration += 1

        if first_seven_characters[0: 5] == "00000":
            try:
                position = int(first_seven_characters[5: 6])
            except ValueError:
                pass

            if position > 7 or position in invalid_positions:
                pass
            else:
                characters_found += 1
                password = password[:position] + first_seven_characters[6: 7] + password[position + 1:]
                invalid_positions.append(position)

    print "Door two password is: " + password


def main():
    puzzle_input = "abbhdwsy"
    
    decrypt_door_one(puzzle_input)
    decrypt_door_two(puzzle_input)


main()
