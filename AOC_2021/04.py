# Advent of Code 2021
# Day 4

import os


class BingoBoard:
    def __init__(self, board_vals):
        self.has_won = False
        self.final_score = 0
        assert(len(board_vals) == 25)
        self.bingo_card = [[] * 5] * 5
        self.bingo_marked = [[] * 5] * 5
        board_val_index = 0
        self.last_num = None
        while board_val_index < len(board_vals):
            self.bingo_card[int(board_val_index / 5)] = board_vals[board_val_index: board_val_index + 5]
            self.bingo_marked[int(board_val_index / 5)] = [False, False, False, False, False]

            board_val_index += 5
    
    def mark_number(self, number):
        self.last_num = number
        for row_index, row in enumerate(self.bingo_card):
            for column_index, column_val in enumerate(row):
                if column_val == number:
                    self.bingo_marked[row_index][column_index] = True
                    break
   
        self.check_win()

    def check_win(self):
        for row_index, row in enumerate(self.bingo_marked):
            column = []
            for walk_index in range(5):
                column.append(self.bingo_marked[walk_index][row_index])
            
            if row == [True, True, True, True, True] or column == [True, True, True, True, True]:
                self.has_won = True
                break
        
    def calculate_score(self):
        sum_unmarked = 0
        for row_index, row in enumerate(self.bingo_marked):
            for column_index, column_val in enumerate(row):
                if column_val == False:
                    sum_unmarked += int(self.bingo_card[row_index][column_index])
        
        self.final_score = sum_unmarked * int(self.last_num)
        

def main():
    with open(f"input{os.sep}day04.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().split()

    bingo_input = puzzle_input[0].split(',')
    
    puzzle_index = 0
    board_vals = []
    bingo_cards = []
    while puzzle_index < len(puzzle_input[1:]):
        board_vals.append(puzzle_input[1:][puzzle_index])
        if len(board_vals) == 25:
            bingo_cards.append(BingoBoard(board_vals))
            board_vals = []
        puzzle_index += 1
    
    first_winning_card = None
    last_winning_card = None
    winning_cards = []
    for number in bingo_input:
        for card in bingo_cards:
            card.mark_number(number)
            if card.has_won and card not in winning_cards:
                winning_cards.append(card)
                if first_winning_card == None:
                    card.calculate_score()
                    first_winning_card = card
                elif len(winning_cards) == len(bingo_cards):
                    card.calculate_score()
                    last_winning_card = card
    
    print(f"Part One: {first_winning_card.final_score}")
    print(f"Part Two: {last_winning_card.final_score}")


if __name__ == "__main__":
    main()

