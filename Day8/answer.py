import itertools

CHARS = 'abcdefg'
SEGMENTS = {
    0: sorted("abcefg"),
    1: sorted("cf"),
    2: sorted("acdeg"),
    3: sorted("acdfg"),
    4: sorted('bcdf'),
    5: sorted('abdfg'),
    6: sorted('abdefg'),
    7: sorted('acf'),
    8: sorted('abcdefg'),
    9: sorted('abcdfg')
}
VALID_CODES = set(''.join(x) for x in SEGMENTS.values())
REVERSE_SEGMENTS = {
    ''.join(v): k for k, v in SEGMENTS.items()
}
def parse_input(file_name):
    results = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            before, after = line.split('|')
            before = sorted(before.strip().split(), key=lambda x: len(x))
            after = after.strip().split()
            results.append((before, after))
    return results

def part1(inputs):
    cnt = 0
    # 1, 4, 7, 8 corresponds to 
    # 2, 4, 3, 7 segments and are unique
    for before, after in inputs:
        for data in after:
            if len(data) in {2, 3, 4, 7}:
                cnt += 1
    return cnt 

PERMUTATIONS = list(itertools.permutations(CHARS))
PERMUTATION_MAP = list()
for permutation in PERMUTATIONS:
    local_map = {}
    for from_c, to_c in zip(permutation, CHARS):
        local_map[from_c] = to_c
    PERMUTATION_MAP.append(local_map)

def solve(before, after):
    # There are only 7! possible scramblings so
    # basically try them all
    for permutation in PERMUTATION_MAP: 
        all_good = True
        for code in before:
            new_code = sorted([permutation[c] for c in code])
            new_code = ''.join(new_code)
            if new_code not in VALID_CODES:
                all_good = False 
                break
        if all_good:
            break

    r = 0
    for code in after:
        code = [permutation[c] for c in code]
        code = sorted(code)
        code = ''.join(code)
        value = REVERSE_SEGMENTS[code]
        r = r * 10 + value 
    return r

def part2(inputs):
    sum = 0
    for before, after in inputs:
        sum += solve(before, after)
    return sum

if __name__ == "__main__":
    r = parse_input("Day8/input.txt")
    print(part1(r))
    print(part2(r))