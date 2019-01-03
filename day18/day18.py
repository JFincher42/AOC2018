'''
AoC 2018 Day 18
'''

import copy

def part1():
    # Input File
    filename = "./day18/input.txt"

    # Sample Input
    # filename = "./day18/sample.txt"

    ground = []
    # Read the file
    with open(filename, "r") as infile:
        for line in infile:
            ground_line = [char for char in line.strip()]
            ground.append(ground_line)

    tick = 0
    while tick < 10:
        # print(f"Tick: {tick}")
        # print_ground(ground)
        # input()

        new_ground = copy.deepcopy(ground)
        for y in range(len(new_ground)):
            for x in range(len(new_ground[y])):
                if new_ground[y][x] == "." and check_open(new_ground, (x,y)):
                    ground[y][x] = "|"
                if new_ground[y][x] == "|" and check_trees(new_ground, (x,y)):
                    ground[y][x] = "#"
                if new_ground[y][x] == "#" and not check_lumber(new_ground, (x,y)):
                    ground[y][x] = "."
        tick += 1

    trees = 0
    lumberyards = 0
    for ground_line in ground:
        trees += [x for x in ground_line].count("|")
        lumberyards += [x for x in ground_line].count("#")
    
    print(f"Part 1: Trees={trees}, lumberyards={lumberyards}, resource value={lumberyards*trees}")

def print_ground(ground):
    for ground_line in ground:
        print(''.join(str(e) for e in ground_line))

def check_trees(ground, source):
    cx, cy = source
    lx, rx = get_lohi(cx, len(ground))
    uy, dy = get_lohi(cy, len(ground))

    lumberyards = 0
    for y in range(uy, dy+1):
        lumberyards += ground[y][lx:rx+1].count("#")
    return lumberyards>=3

def check_open(ground, source):
    cx, cy = source
    lx, rx = get_lohi(cx, len(ground))
    uy, dy = get_lohi(cy, len(ground))

    trees = 0
    for y in range(uy, dy+1):
        trees += ground[y][lx:rx+1].count("|")
    return trees>=3

def check_lumber(ground, source):
    cx, cy = source
    lx, rx = get_lohi(cx, len(ground))
    uy, dy = get_lohi(cy, len(ground))

    trees = 0
    lumber = -1
    for y in range(uy, dy+1):
        trees += ground[y][lx:rx+1].count("|")
        lumber += ground[y][lx:rx+1].count("#")
    return trees>=1 and lumber>=1


def get_lohi(num, maximum):
    low = max(0, num-1)
    high = min(maximum-1, num+1)
    return (low, high)

if __name__ == "__main__":
    part1()