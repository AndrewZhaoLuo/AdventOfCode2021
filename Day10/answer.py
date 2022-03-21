CLOSINGS = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}
SCORES_P1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
SCORES_P2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def parse_input(filename):
    chunks = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            chunks.append(line.strip())
    return chunks 

def part1(chunks):
    score = 0
    for chunk in chunks:
        stack = []
        for char in chunk:
            is_opening = char in CLOSINGS.keys()
            if is_opening:
                stack.append(char)
            else:
                expected = CLOSINGS[stack.pop()]
                if expected != char:
                    score += SCORES_P1[char]
                    break 
    return score

def get_incomplete_chunks(chunks):
    autocomplete_stack = []
    for chunk in chunks:
        is_good = True
        stack = []
        for char in chunk:
            is_opening = char in CLOSINGS.keys()
            if is_opening:
                stack.append(char)
            else:
                expected = CLOSINGS[stack.pop()]
                if expected != char:
                    is_good = False
                    break 
        if is_good:
            autocomplete_stack.append(stack)
    return autocomplete_stack

def get_score(closing_list):
    ans = 0
    for c in closing_list:
        ans *= 5
        ans += SCORES_P2[c]
    return ans 

def part2(chunks):
    autocomplete_stack = get_incomplete_chunks(chunks)
    answers = []
    for autocomplete in autocomplete_stack:
        answers.append([CLOSINGS[c] for c in autocomplete[::-1]])
    scores = [get_score(ans) for ans in answers]
    scores.sort()
    return scores[len(scores) // 2]

if __name__ == "__main__":
    chunks = parse_input('Day10/input.txt')
    print(part1(chunks)) 
    print(part2(chunks))
    