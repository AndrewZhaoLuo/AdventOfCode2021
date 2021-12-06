with open('Day2/input.txt', 'r') as f:
    raw_data = f.readlines()


def process_input(input_str):
    cmd, amt = input_str.strip().split(' ')
    amt = int(amt)
    if cmd == 'forward':
        return (amt, 0)
    elif cmd == 'down':
        return (0, amt)
    elif cmd == 'up':
        return (0, -amt)

def part1():
    pos = [0, 0]
    for d in raw_data:
        delta = process_input(d)
        pos[0] += delta[0]
        pos[1] += delta[1]

    print(pos[0] * pos[1])

def process_input2(input_str, cur_aim):
    cmd, amt = input_str.strip().split(' ')
    amt = int(amt)
    if cmd == 'forward':
        return (amt, amt * cur_aim, 0)
    elif cmd == 'down':
        return (0, 0, amt)
    elif cmd == 'up':
        return (0, 0, -amt)

def part2():
    # horizontal, depth, aim
    pos = [0, 0, 0]
    for d in raw_data:
        delta = process_input2(d, pos[2])
        pos[0] += delta[0]
        pos[1] += delta[1]
        pos[2] += delta[2]

    print(pos[0] * pos[1])

part1()
part2()