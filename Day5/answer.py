from tracemalloc import start
from typing import *

class Line:
    def __init__(self, start_point: Tuple[int, int], end_point: Tuple[int, int]):
        self.start_point = start_point
        self.end_point = end_point

    def is_simple_line(self):
        """Whether a line is horizontal or vertical"""
        return self.start_point[0] == self.end_point[0] or self.start_point[1] == self.end_point[1]

    def get_points_hit(self):      
        dx = self.end_point[0] - self.start_point[0]
        dy = self.end_point[1] - self.start_point[1]

        cur_x = self.start_point[0]
        cur_y = self.start_point[1]
        yield (cur_x, cur_y)
        while dx != 0 or dy != 0:
            if dx > 0:
                cur_x += 1
                dx -= 1
            elif dx < 0:
                cur_x -= 1
                dx += 1

            if dy > 0:
                cur_y += 1
                dy -= 1
            elif dy < 0:
                cur_y -= 1
                dy += 1

            yield (cur_x, cur_y)

    def __str__(self):
        return str(self.start_point) + " -> " + str(self.end_point)

def parse_input(file_name):
    segments = []
    largest_x = 0
    largest_y = 0
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split('->')
            start_point = line[0].strip().split(',')
            start_point = (int(start_point[0]), int(start_point[1]))
            end_point = line[1].strip().split(',')
            end_point = (int(end_point[0]), int(end_point[1]))

            largest_x = max(largest_x, start_point[0], end_point[0])
            largest_y = max(largest_y, start_point[1], end_point[1])
            segments.append(Line(start_point, end_point))

    return segments, largest_x, largest_y

if __name__ == "__main__":
    # Brute force for now
    segments, largest_x, largest_y = parse_input('Day5/input.txt')

    print("largest x:", largest_x)
    print("largest y:", largest_y)

    grid = [[0 for _ in range(largest_x + 1)] for _ in range(largest_y + 1)]

    for segment in segments:
        # part 1:
        # if not segment.is_simple_line():
        #     continue 

        # print(segment)
        for x, y in segment.get_points_hit():
        #     print((x, y))
            grid[y][x] += 1
        # print()

    cnt = 0
    for row in grid:
        for n in row:
            if n > 1:
                cnt += 1

    print(cnt)

