from sklearn import neighbors


def parse_input(filename):
    grid = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            row = [int(c) for c in line.strip()]
            grid.append(row)

    return grid 

def is_valid_index(grid, x, y):
    if len(grid) == 0:
        return False 
    if len(grid[0]) == 0:
        return False 
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0])

def is_low_point(grid, x, y):
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    
    current = grid[y][x]
    for nx, ny in neighbors:
        if is_valid_index(grid, nx, ny):
            height = grid[ny][nx] 
        else:
            height = 10
        if current >= height:
            return False

    return True 
        
def part1(grid):
    danger_level_sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_low_point(grid, x, y):
                danger_level_sum += 1 + grid[y][x]
    return danger_level_sum

def part2(grid):
    # shows which basin things belongs too
    basin_grid = [
        [0 for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]

    def verify_basin_coord(nx, ny):
        if not is_valid_index(grid, nx, ny):
            return False 
        if basin_grid[ny][nx] > 0:
            return False
        if grid[ny][nx] == 9:
            return False

        return True 

    basin_sizes = []
    cur_basin_index = 1
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if not verify_basin_coord(x, y):
                continue 

            # x, y, basin_index
            search = [(x, y, cur_basin_index)]
            basin_size = 0

            while len(search) > 0:
                x, y, basin_index = search.pop()
                if not verify_basin_coord(x, y):
                    continue
                
                cur_height = grid[y][x]
                basin_grid[y][x] = basin_index
                basin_size += 1
                neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                for nx, ny in neighbors:
                    if verify_basin_coord(nx, ny):
                        search.append((nx, ny, basin_index))
            cur_basin_index += 1
            basin_sizes.append(basin_size)
    result = sorted(basin_sizes)
    return result[-1] * result[-2] * result[-3]
    
if __name__ == "__main__":
    grid = parse_input('Day9/input.txt')
    print(part1(grid))
    print(part2(grid))