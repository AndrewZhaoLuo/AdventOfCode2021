from typing import * 

class BingoBoard:
    def __init__(self, board: List[List[int]]):
        self.board = board 
        self.rows = len(board)
        self.cols = len(board[0])
        self.won = False

        # map of bingo number to (row, col) indices
        self.row_col_map = {}
        self.row_count = [0] * self.rows
        self.col_count = [0] * self.cols 

        for r in range(self.rows):
            for c in range(self.cols):
                num = board[r][c]
                self.row_col_map[num] = (r, c)

    def add_num(self, num: int) -> bool:
        if num not in self.row_col_map:
            return False 

        row, col = self.row_col_map[num]
        self.row_count[row] += 1
        self.col_count[col] += 1

        self.won = self.row_count[row] == self.rows or self.col_count[col] == self.cols
        return self.won

    def sum_unmarked(self, numbers_called: Set[int]):
        sum_unmarked = 0
        for row in self.board:
            for n in row: 
                if n not in numbers_called:
                    sum_unmarked += n
        return sum_unmarked

def parse_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines() 
        numbers_in_order = lines[0].strip().split(',')
        numbers_in_order = [int(n) for n in numbers_in_order]
        boards = []

        NUM_LINES = 5
        cur_board = []
        for line in lines[2:]:
            if line.strip() == '':
                continue 
            line = line.strip().split()
            line = [int(n) for n in line]
            cur_board.append(line)

            if len(cur_board) == NUM_LINES:
                boards.append(BingoBoard(cur_board))
                cur_board = []

    return numbers_in_order, boards

if __name__ == "__main__":
    numbers_in_order, boards = parse_file('Day4/input.txt')
    numbers_called = set()
    for number in numbers_in_order:
        if number in numbers_called:
            continue
        numbers_called.add(number)

        for board in boards:
            if not board.won and board.add_num(number):
                print("Winner:", number, board.board)
                print("Result:", number * board.sum_unmarked(numbers_called))
                print()