from collections import defaultdict

START = 'start'
END = 'end'

def parse_input(filename):
    graph = defaultdict(set)
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            start, end = line.split('-')
            start = start.strip()
            end = end.strip()
            graph[start].add(end)
            graph[end].add(start)
    return graph 

def part1(graph, start=START, end=END):
    return part1_recursive(graph, start, set(), end=end) 

def is_small_cave(cave):
    return cave.islower()

# DFS
def part1_recursive(graph, node, visited, end=END):
    if node in visited:
        return 0

    if node == end:
        return 1
    
    if is_small_cave(node):
        visited.add(node)

    total_paths = 0
    neighbors = graph[node]
    for neighbor in neighbors:
        total_paths += part1_recursive(graph, neighbor, visited)

    if is_small_cave(node):
        visited.remove(node)
    return total_paths

def part2(graph, start=START, end=END):
    return part2_recursive(graph, start, set(), None, end=end) 

def part2_recursive(graph, node, visited, used_twice, end=END):
    # handle special nodes
    if node == START and START in visited:
        return 0
    if node == end:
        return 1
    
    if node in visited:
        if used_twice is not None:
            return 0
        else:
            used_twice = node

    if is_small_cave(node):
        visited.add(node)

    total_paths = 0
    neighbors = graph[node]
    for neighbor in sorted(neighbors):
        total_paths += part2_recursive(graph, neighbor, visited, used_twice)

    if is_small_cave(node):
        if used_twice != node:
            visited.remove(node)
    return total_paths


if __name__ == "__main__":
    graph = parse_input('Day12/input.txt')
    print(part1(graph))
    print(part2(graph))