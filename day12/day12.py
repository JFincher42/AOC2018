'''
Day 12, AoC 2018
'''
def count_plants(state, zero):
    count = 0
    for pot in range(len(state)):
        if state[pot] == "#":
            count += (pot - zero)
    return count

def part1():
    # Input File
    filename = "./day12/input.txt"

    # Sample Input
    # filename = "./day12/sample.txt"

    # Read the file line by line
    with open(filename, "r") as infile:
        current_state = "..." + infile.readline()[15:].strip() + "....."
        plant_rules = []
        empty_rules = []
        for line in infile:
            if len(line) > 0:
                if line[-2:-1] == "#":
                    plant_rules.append(line[0:5])
                else:
                    empty_rules.append(line[0:5])
    
    generation = 0
    zero_pot = 3
    plant_count = 0
    while generation < 20:
        print(f" Generation {generation}: State: {current_state}")
        next_state = current_state[0:2]
        current = 2
        while current < len(current_state):
            if current_state[current-2:current+3] in plant_rules:
                next_state += "#"
            elif current_state[current-2:current+3] in empty_rules:
                next_state += "."
            else:
                next_state += "."
            current += 1
        generation += 1
        current_state = next_state

        if current_state[2] == "#":
            current_state = "." + current_state
            zero_pot += 1
        if current_state[-3] == "#":
            current_state = current_state + ".."
    
    print(f" Generation {generation}: State: {current_state}")
    plant_count = count_plants(current_state, zero_pot)

    print(f"Part 1: Final count: {plant_count}")

if __name__ == "__main__":
    part1()