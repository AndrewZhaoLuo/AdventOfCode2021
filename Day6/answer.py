
def parse_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        line = lines[0].split(',')
        return [int(n) for n in line]

COUNTER_AFTER_ZERO = 6
COUNTER_AFTER_SPAWN = 8

def advance_one_day(counter_counts):
    zero_count = counter_counts[0]
    for i in range(len(counter_counts) - 1):
        counter_counts[i] = counter_counts[i + 1]
    
    counter_counts[COUNTER_AFTER_SPAWN] = zero_count
    counter_counts[COUNTER_AFTER_ZERO] += zero_count

if __name__ == "__main__":
    initial_counts = parse_input('Day6/input.txt')

    # map of internal timers to count of fish with those internal counters
    counter_counts = [0] * (COUNTER_AFTER_SPAWN + 1)
    for n in initial_counts:
        counter_counts[n] += 1

    target_day = 256
    for day in range(target_day):
        # print(f"Day {day}")
        # print(counter_counts)
        advance_one_day(counter_counts)
    print(sum(counter_counts))
    

