from collections import defaultdict

with open('Day3/input.txt', 'r') as f:
    raw_data = f.readlines()

def part1():
    # cnt_ones[i] is the cnt of ones in the ith position
    # 0th index is MSB or left most bit
    cnt_ones = [0] * len(raw_data[0].strip())

    for line in raw_data:
        line = line.strip()
        for i, c in enumerate(line):
            cnt_ones[i] += c == '1'

    gamma_rate = [int(cnt_ones[i] > len(raw_data) // 2) for i in range(len(cnt_ones))]
    epsilon_rate = [1 - n for n in gamma_rate]

    gamma_val = int(''.join([str(c) for c in gamma_rate]), 2)
    epsilon_val = int(''.join([str(c) for c in epsilon_rate]), 2)

    print(gamma_val * epsilon_val)

def part2():
    data_oxygen = set([d.strip() for d in raw_data])
    data_co2 = set([d.strip() for d in raw_data])
    for i in range(len(raw_data[0].strip())):
        # cnt for current position
        cnt_one_oxygen = 0
        for d in (data_oxygen):
            cnt_one_oxygen += d[i] == '1'

        cnt_one_co2 = 0
        for d in (data_co2):
            cnt_one_co2 += d[i] == '1'

        oxygen_target = '1' if cnt_one_oxygen >= len(data_oxygen) / 2 else '0'
        co2_target = '0' if cnt_one_co2 >= len(data_co2) / 2 else '1'

        for d in list(data_oxygen):
            if d[i] != oxygen_target and len(data_oxygen) > 1:
                data_oxygen.remove(d)
        for d in list(data_co2):
            if d[i] != co2_target and len(data_co2) > 1:
                data_co2.remove(d)

    oxygen_rating = list(data_oxygen)[0]
    co2_rating = list(data_co2)[0]

    oxygen_rating = int(''.join([str(c) for c in oxygen_rating]), 2)
    co2_rating = int(''.join([str(c) for c in co2_rating]), 2)

    print(oxygen_rating * co2_rating)

part1()
part2()