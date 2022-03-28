import numpy as np 
import itertools

def parse_input(file_name):
    grid = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for row in lines:
            grid.append(
                [int(c) for c in row.strip()]
            )

    return np.array(grid) 

def valid_index(grid, row, col):
    return row >= 0 and col >= 0 and row < grid.shape[0] and col < grid.shape[1]

def get_bonus_grid(grid, flashed):
    """flashed gets mutated"""

    bonus = np.zeros_like(grid)
    any_bonus = False
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row][col] > 9 and not flashed[row][col]:
                flashed[row][col] = True

                adjacent = itertools.product((row + 1, row, row - 1), (col + 1, col, col - 1))
                for adj_row, adj_col in adjacent:
                    if adj_row == row and adj_col == col:
                        continue
                    if not valid_index(grid, adj_row, adj_col):
                        continue 
                    bonus[adj_row][adj_col] += 1
                    any_bonus = True 

    return bonus, any_bonus

def one_step(grid):
    """grid is mutated"""
    grid += 1
    flashed = np.zeros_like(grid)
    bonus, any_bonus = get_bonus_grid(grid, flashed)
    while any_bonus:
        grid += bonus 
        bonus, any_bonus = get_bonus_grid(grid, flashed)

    total_flashed = flashed.flatten().sum()
    grid *= (1 - flashed)
    return total_flashed

def part1(grid, steps):
    total_flashes = 0 
    # print('0\n', grid)
    for i in range(steps):
        total_flashes += one_step(grid)
        # print(f'{i + 1}\n{grid}')
    return total_flashes

def part2(grid):
    i = 0
    while True:
        total_flashes = one_step(grid)
        i += 1
        if total_flashes == grid.size:
            break
    return i

if __name__ == "__main__":
    FILE = "Day11/input.txt"
    grid = parse_input(FILE) 
    print(part1(grid, 100))
    grid = parse_input(FILE) 
    print(part2(grid))
