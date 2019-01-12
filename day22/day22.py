'''
AoC 2018 Day 22
'''

import numpy as np          # For the map and numeric manipulations

# Real data
# map_depth = 8787
# target = (725, 10)      # (Y coord first)

# Sample data - answer should be 114
map_depth = 510
target = (10, 10)       # (Y coord first)

def calc_geological_index(cx, cy):
    global map_depth, target, erosion_levels, geological_levels, region_types

    xmul = 16807
    ymul = 48271

    if (cy, cx) == (0, 0):
        geological_levels[cy, cx] = 0

    elif (cy, cx) == map_depth:
        geological_levels[cy, cx] = 0

    elif cx == 0:
        geological_levels[cy, cx] = cy*ymul
    
    elif cy == 0:
        geological_levels[cy, cx] = cx*xmul

    else:
        if erosion_levels[cy-1, cx] == -1:
            calc_erosion_level(cx, cy-1)

        if erosion_levels[cy, cx-1] == -1:
            calc_erosion_level(cx-1, cy)

        geological_levels[cy, cx] = erosion_levels[cy, cx-1] * erosion_levels[cy-1, cx]

    # return geological_levels[cy, cx]

def calc_erosion_level(cx, cy):
    global map_depth, target, erosion_levels, geological_levels, region_types

    mod_val = 20183

    if geological_levels[cy, cx] == -1:
        calc_geological_index(cx, cy)

    erosion_levels[cy, cx] = (geological_levels[cy, cx] + map_depth) % mod_val
    region_types[cy, cx] = erosion_levels[cy, cx] % 3

    # return erosion_levels[cy, cx]

def part1():
    global map_depth, target, erosion_levels, geological_levels, region_types

    # Setup map based on Input Data
    cy, cx = target
    erosion_levels = np.ones([cy+1, cx+1], dtype=np.int64)
    geological_levels = np.ones([cy+1, cx+1], dtype=np.int64)
    region_types = np.ones([cy+1, cx+1], dtype=np.int64)
    erosion_levels *= -1
    geological_levels *= -1
    region_types *= -1

    # Let's populate the map between the origin and the target
    # Add the risk as we go
    risk = 0
    for map_y in range(cy+1):
        for map_x in range(cx+1):
            calc_erosion_level(map_x, map_y)
            risk += region_types[map_y, map_x]

    # Print the risk
    print(f"Part 1: Risk = {risk}")

    # Just to see it, let's print the map
    print_map()

def print_map():
    global target, region_types

    cy, cx = target
    for map_y in range(cy+1):
        line = []
        for map_x in range(cx+1):
            if map_y == 0 and map_x == 0:
                line.append("M")
            elif map_y == cy and map_x == cx:
                line.append("T")
            elif region_types[map_y, map_x] == 0:
                line.append(".")
            elif region_types[map_y, map_x] == 1:
                line.append("=")
            elif region_types[map_y, map_x] == 2:
                line.append("|")
        print("".join(line))
    print()

if __name__ == "__main__":
    part1()