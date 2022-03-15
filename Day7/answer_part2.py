def parse_input(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        line = lines[0].split(',')
        locations = [int(n) for n in line]
        return sorted(locations)

def calculate_fuel_cost(rally_point, locations):
    cost = 0
    for n in locations:
        distance = abs(rally_point - n)
        cost += distance * (distance + 1) // 2
    return cost

if __name__ == "__main__":
    locations = parse_input("Day7/input.txt")

    lowest_cost = calculate_fuel_cost(0, locations)

    print(f"Rally at 0: {lowest_cost}")
    # Brute force bro!
    for rally_point in range(1, max(locations)):
        fuel_cost = calculate_fuel_cost(rally_point, locations)
        lowest_cost = min(lowest_cost, fuel_cost)
        print(f"Rally at {rally_point}: {fuel_cost}")
    print(lowest_cost)
