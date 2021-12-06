with open('Day1/input.txt', 'r') as f:
    raw_data = f.readlines()

def part1():
    data = [int(d) for d in raw_data]

    # holds # increases in measurement
    cnt = 0
    for i in range(len(data) - 1):
        cnt += data[i] < data[i + 1]

    print(cnt)

def part2():
    data = [int(d) for d in raw_data]

    data = [data[i] + data[i + 1] + data[i + 2] for i in range(len(data) - 2)]

    # holds # increases in measurement
    cnt = 0
    for i in range(len(data) - 1):
        cnt += data[i] < data[i + 1]

    print(cnt)

part1()
part2()