'''
AoC 2018 Day 18
'''

import copy

def part1():
    # Input File
    filename = "./day18/input.txt"

    # Sample Input
    # filename = "./day18/sample.txt"

    ground1 = []
    # Read the file
    with open(filename, "r") as infile:
        for line in infile:
            ground_line = [char for char in line.strip()]
            ground1.append(ground_line)

    ground2 = copy.deepcopy(ground1)

    # Ground1 and Ground2 are the objects
    # ground and new_ground are references
    # We flip them at end of each loop, using flip to tell us which way
    ground = ground1
    new_ground = ground2
    flip = True

    tick = 0
    while tick <= 10:
        # if tick%100000 == 0:
        #     print(f"Tick: {tick}")
        #     print_ground(ground)
        # print(f"Tick: {tick}")
        # print_ground(ground)
        # input()

        for y in range(len(new_ground)):
            for x in range(len(new_ground[y])):
                if new_ground[y][x] == ".":
                    if check_open(new_ground, (x,y)):
                        ground[y][x] = "|"
                    else:
                        ground[y][x] = "."

                elif new_ground[y][x] == "|":
                    if check_trees(new_ground, (x,y)):
                        ground[y][x] = "#"
                    else:
                        ground[y][x] = "|"

                elif new_ground[y][x] == "#":
                    if not check_lumber(new_ground, (x,y)):
                        ground[y][x] = "."
                    else:
                        ground[y][x] = "#"
        tick += 1
        if flip:
            ground = ground2
            new_ground = ground1
        else:
            ground = ground1
            new_ground = ground2
        flip = not flip

    # if flip:
    #     ground = ground2
    #     new_ground = ground1
    # else:
    #     ground = ground1
    #     new_ground = ground2

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