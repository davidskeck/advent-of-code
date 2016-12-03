instructions_string = """LLLRLLULLDDLDUDRDDURLDDRDLRDDRUULRULLLDLUURUUUDLUUDLRUDLDUDURRLDRRRUULUURLUDRURULRLRLRRUULRUUUDRRDDRLLLDDLLUDDDLLRLLULULRRURRRLDRLDLLRURDULLDULRUURLRUDRURLRRDLLDDURLDDLUDLRLUURDRDRDDUURDDLDDDRUDULDLRDRDDURDLUDDDRUDLUDLULULRUURLRUUUDDRLDULLLUDLULDUUDLDLRRLLLRLDUDRUULDLDRDLRRDLDLULUUDRRUDDDRDLRLDLRDUDRULDRDURRUULLUDURURUUDRDRLRRDRRDRDDDDLLRURULDURDLUDLUULDDLLLDULUUUULDUDRDURLURDLDDLDDUULRLUUDLDRUDRURURRDDLURURDRLRLUUUURLLRR
UUUUURRRURLLRRDRLLDUUUUDDDRLRRDRUULDUURURDRLLRRRDRLLUDURUDLDURURRLUDLLLDRDUDRDRLDRUDUDDUULLUULLDUDUDDRDUUUDLULUDUULLUUULURRUDUULDUDDRDURRLDDURLRDLULDDRUDUDRDULLRLRLLUUDDURLUUDLRUUDDLLRUURDUDLLDRURLDURDLRDUUDLRLLRLRURRUDRRLRDRURRRUULLUDLDURDLDDDUUDRUUUDULLLRDRRDRLURDDRUUUDRRUUDLUDDDRRRRRLRLDLLDDLRDURRURLLLULURULLULRLLDDLDRLDULLDLDDDRLUDDDUDUDRRLRDLLDULULRLRURDLUDDLRUDRLUURRURDURDRRDRULUDURRLULUURDRLDLRUDLUDRURLUDUUULRRLRRRULRRRLRLRLULULDRUUDLRLLRLLLURUUDLUDLRURUDRRLDLLULUDRUDRLLLRLLDLLDUDRRURRLDLUUUURDDDUURLLRRDRUUURRRDRUDLLULDLLDLUDRRDLLDDLDURLLDLLDLLLDR
LRDULUUUDLRUUUDURUUULLURDRURDRRDDDLRLRUULDLRRUDDLLUURLDRLLRUULLUDLUDUDRDRDLUUDULLLLRDDUDRRRURLRDDLRLDRLULLLRUUULURDDLLLLRURUUDDDLDUDDDDLLLURLUUUURLRUDRRLLLUUULRDUURDLRDDDUDLLRDULURURUULUDLLRRURDLUULUUDULLUDUUDURLRULRLLDLUULLRRUDDULRULDURRLRRLULLLRRDLLDDLDUDDDUDLRUURUDUUUDDLRRDLRUDRLLRDRDLURRLUDUULDRRUDRRUDLLLLRURRRRRUULULLLRDRDUDRDDURDLDDUURRURLDRRUDLRLLRRURULUUDDDLLLRDRLULLDLDDULDLUUDRURULLDLLLLDRLRRLURLRULRDLLULUDRDR
RURRRUDLURRURLURDDRULLDRDRDRRULRRDLDDLDUUURUULLRRDRLDRRDRULLURRRULLLDULDDDDLULRUULRURUDURDUDRLRULLLRDURDDUDDRDLURRURUURDLDDDDDURURRURLLLDDLDRRDUDDLLLDRRLDDUUULDLLDRUURUDDRRLDUULRRDDUDRUULRLDLRLRUURLLDRDLDRLURULDLULDRULURLLRRLLDDDURLRUURUULULRLLLULUDULUUULDRURUDDDUUDDRDUDUDRDLLLRDULRLDLRRDRRLRDLDDULULRLRUUDDUDRRLUDRDUUUDRLLLRRLRUDRRLRUUDDLDURLDRRRUDRRDUDDLRDDLULLDLURLUUDLUDLUDLDRRLRRRULDRLRDUURLUULRDURUDUUDDURDDLRRRLUUUDURULRURLDRURULDDUDDLUDLDLURDDRRDDUDUUURLDLRDDLDULDULDDDLDRDDLUURDULLUDRRRULRLDDLRDRLRURLULLLDULLUUDURLDDULRRDDUULDRLDLULRRDULUDUUURUURDDDRULRLRDLRRURR
UDDDRLDRDULDRLRDUDDLDLLDDLUUURDDDLUDRDUDLDURLUURUDUULUUULDUURLULLRLUDLLURUUUULRLRLLLRRLULLDRUULURRLLUDUDURULLLRRRRLRUULLRDRDRRDDLUDRRUULUDRUULRDLRDRRLRRDRRRLULRULUURRRULLRRRURUDUURRLLDDDUDDULUULRURUDUDUDRLDLUULUDDLLLLDRLLRLDULLLRLLDLUUDURDLLRURUUDDDDLLUDDRLUUDUDRDRLLURURLURRDLDDDULUURURURRLUUDUDLDLDDULLURUDLRLDLRLDLDUDULURDUDRLURRRULLDDDRDRURDDLDLULUDRUULDLULRDUUURLULDRRULLUDLDRLRDDUDURRRURRLRDUULURUUDLULDLRUUULUDRDRRUDUDULLDDRLRDLURDLRLUURDRUDRDRUDLULRUDDRDLLLRLURRURRLDDDUDDLRDRRRULLUUDULURDLDRDDDLDURRLRRDLLDDLULULRRDUDUUDUULRDRRDURDDDDUUDDLUDDUULDRDDULLUUUURRRUUURRULDRRDURRLULLDU"""

instructions = instructions_string.split('\n')


def main():
    keypad = [[(i * 3) + (j + 1) for i in range(3)] for j in range(3)]

    current_key = [1, 1]

    def find_next_key(direction):
        if direction == "U":
            if current_key[1] == 0:
                pass
            else:
                current_key[1] -= 1
        elif direction == "R":
            if current_key[0] == 2:
                pass
            else:
                current_key[0] += 1
        elif direction == "D":
            if current_key[1] == 2:
                pass
            else:
                current_key[1] += 1
        elif direction == "L":
            if current_key[0] == 0:
                pass
            else:
                current_key[0] -= 1

    print("Bathroom keycode is: ")

    for instruction in instructions:
        for direction in instruction:
            find_next_key(direction)
        print(keypad[current_key[0]][current_key[1]])


def part2():
    keypad = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 2, 3, 4, 0, 0],
        [0, 5, 6, 7, 8, 9, 0],
        [0, 0, 'A', 'B', 'C', 0, 0],
        [0, 0, 0, 'D', 0, 0, 0]
    ]

    current_key = [2, 1]

    def find_next_key(direction):
        if direction == "U":
            if current_key[0] == 0:
                pass
            elif keypad[(current_key[0] - 1)][current_key[1]] == 0:
                pass
            else:
                current_key[0] -= 1
        elif direction == "R":
            if current_key[1] == 6:
                pass
            elif keypad[current_key[0]][(current_key[1] + 1)] == 0:
                pass
            else:
                current_key[1] += 1
        elif direction == "D":
            if current_key[0] == 4:
                pass
            elif keypad[(current_key[0] + 1)][current_key[1]] == 0:
                pass
            else:
                current_key[0] += 1
        elif direction == "L":
            if current_key[1] == 0:
                pass
            elif keypad[current_key[0]][(current_key[1] - 1)] == 0:
                pass
            else:
                current_key[1] -= 1

    print("Bathroom keycode is: ")

    for instruction in instructions:
        for direction in instruction:
            find_next_key(direction)
        print(keypad[current_key[0]][current_key[1]])


main()
part2()
