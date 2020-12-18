from math import ceil


charToIndex = {
    "F": 0,
    "B": 1,
    "R": 1,
    "L": 0
}

def main():
    input_data = []
    with open("input.txt") as input:
        for line in input:
            input_data.append(line.strip())
    
    input_data = input_data[:-1]
    
    seat_locations = []
    seat_ids = []
    for line in input_data:
        min_row = 0
        max_row = 127
        row = 0
        min_column = 0
        max_column = 7
        column = 0
        row_designators = line[0:7]
        column_designators = line[-3:]
        for designator in row_designators:
            index = charToIndex[designator]
            if index == 0:
                max_row -= ceil((max_row - min_row) / 2)
                row = max_row
            else:
                min_row += ceil((max_row - min_row) / 2)
                row = min_row

        for designator in column_designators:
            index = charToIndex[designator]
            if index == 0:
                max_column -= ceil((max_column - min_column) / 2)
                column = max_column
            else:
                min_column += ceil((max_column - min_column) / 2)
                column = min_column
        
        seat_locations.append((row, column))
        seat_ids.append(row * 8 + column)

    print("Highest seat id (p1): {}".format(max(seat_ids)))
    
    rows_with_empty_seats = []
    for i in range(1, 127):
        used_seats = []
        for row, column in seat_locations:
            if row == i:
                used_seats.append(column)

        if len(used_seats) < 8:
            rows_with_empty_seats.append((i, used_seats))

    for row_data in rows_with_empty_seats:
        row, seats = row_data
        if len(seats) > 0:
            seats.sort()
            seat_offset = seats[0]
            for index, seat in enumerate(seats):
                if index + seat_offset != seat:
                    print("My seat id (p2): {}".format(8 * row + index))
                    break

if __name__ == "__main__":
    main()

