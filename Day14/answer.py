from collections import defaultdict
from tracemalloc import start


def parse_input(filename):
    polymerizations = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        start_chain = lines[0].strip()
        lines = lines[2:]
        for line in lines:
            line = line.strip()
            pair, result = line.split('->')
            pair = pair.strip()
            result = result.strip()
            polymerizations[pair] = result

    return start_chain, polymerizations

def apply_polymerizations(chain, polys):
    result = []

    for i in range(len(chain) - 1):
        cur_c = chain[i]
        result.append(cur_c)
        pair = chain[i:i+2]
        if pair in polys:
            result.append(polys[pair])
        
    result.append(chain[-1])
    return ''.join(result)

def part1(start_chain, polys):
    chain = start_chain
    for _ in range(10):
        chain = apply_polymerizations(chain, polys)
    counts = defaultdict(int)
    for c in chain:
        counts[c] += 1

    results = list(counts.items())
    results.sort(key=lambda x: x[1])
    return results[-1][1] - results[0][1]

def apply_one_step_eff(pair_counts, polys):
    new_pair_counts = defaultdict(int)

    # A more efficient algo
    for pair, count in pair_counts.items():
        if pair in polys:
            new_pair1 = pair[0] + polys[pair]
            new_pair2 = polys[pair] + pair[1]
            new_pair_counts[new_pair1] += count 
            new_pair_counts[new_pair2] += count 
        else:
            new_pair_counts[pair] += count 
    return new_pair_counts

def get_pair_counts(chain):
    pair_counts = defaultdict(int)
    for i in range(len(chain) - 1):
        pair_counts[chain[i:i+2]] += 1
    return pair_counts

def part2(start_chain, polys):
    pair_counts = get_pair_counts(start_chain)
    for _ in range(40):
        pair_counts = apply_one_step_eff(pair_counts, polys)

    # Each pair is counted twice
    counts = defaultdict(int)
    for pair, count in pair_counts.items():
        counts[pair[0]] += count 
        counts[pair[1]] += count

    # Except for the first and last item in chain
    counts[start_chain[0]] += 1
    counts[start_chain[-1]] += 1

    for c in counts:
        counts[c] /= 2

    results = list(counts.items())
    results.sort(key=lambda x: x[1])
    return results[-1][1] - results[0][1]

if __name__ == "__main__":
    FILE = 'Day14/example_input.txt'
    chain, polys = parse_input(FILE)
    print(part1(chain, polys))
    print(part2(chain, polys))
