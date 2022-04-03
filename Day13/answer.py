import numpy as np
import itertools

def parse_input(filename):
    folds = []
    points = []
    largest_x = 0
    largest_y = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('fold'):
                coord = line.split('fold along ')[-1]
                bearing, num = coord.split('=')
                folds.append((bearing, int(num)))
            elif line == '':
                continue
            else:
                x, y = line.split(',')
                x = int(x)
                y = int(y)
                points.append((x, y))
                largest_x = max(largest_x, x)
                largest_y = max(largest_y, y)

    grid = np.zeros((largest_y + 1, largest_x + 1)).astype('bool')
    for x, y in points:
        grid[y, x] = True 

    return grid, folds 

def fold(grid, fold):
    bearing, num = fold 

    H, W = grid.shape

    def map_func(x, y):
        if bearing == 'x':
            if x <= num:
                to_x = x 
            else:
                to_x = num - (x - num - 1) - 1
            to_y = y 
        else: # bearing == 'y'
            if y <= num:
                to_y = y 
            else:
                to_y = num - (y - num - 1) - 1
            to_x = x 

        return to_x, to_y 

    for x, y in itertools.product(range(W), range(H)):
        to_x, to_y = map_func(x, y)
        grid[to_y, to_x] = grid[to_y, to_x] or grid[y, x]

    if bearing == 'x':
        return grid[:, :num] 
    else: # bearing == 'y'
        return grid[:num, :]

if __name__ == "__main__":
    FILE = 'Day13/input.txt'
    grid, folds = parse_input(FILE)

    # part 1
    new_grid = fold(grid, folds[0])
    print(new_grid.flatten().sum())

    # part 2
    grid, folds = parse_input(FILE)
    for f in folds:
        grid = fold(grid, f)

    for row in grid:
        result = ['#' if c else '.' for c in row]
        print(''.join(result))
