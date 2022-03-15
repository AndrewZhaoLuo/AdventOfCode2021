def parse_input(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        line = lines[0].split(',')
        locations = [int(n) for n in line]
        return sorted(locations)

if __name__ == "__main__":
    locations = parse_input("Day7/input.txt")
    cur_fuel_cost = 0
    for n in locations[1:]:
        cur_fuel_cost += n - locations[0]
    min_fuel_cost = cur_fuel_cost

    print(locations)
    print(f"Align locations locations[0] = {locations[0]}: {cur_fuel_cost}")
    for i in range(len(locations) - 1):
        # Calculate fuel diff moving from 
        # aligning on locations[i] --> locations[i + 1]
        prev_location = locations[i]
        new_location = locations[i + 1]

        distance = new_location - prev_location
        cnt_degraded = i + 1
        cnt_improved = len(locations) - cnt_degraded
        cur_fuel_cost = cur_fuel_cost + distance * cnt_degraded - distance * cnt_improved
        min_fuel_cost = min(min_fuel_cost, cur_fuel_cost)

        print(f"Align locations locations[{i + 1}] = {locations[i + 1]}: {cur_fuel_cost}")

    print(min_fuel_cost)