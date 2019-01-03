'''
Day 17  - AoC 2018
'''

import queue
import sys

def print_ground(ground, min_x, max_x):
    print("GROUND:")
    for y in range(len(ground)):
        print(''.join(str(e) for e in ground[y][min_x-5:max_x+5]))
    print()

def make_ground(max_x, max_y, clay_veins):
    ground = [["."] * (max_x+10) for i in range(max_y+5)]
    for clay in clay_veins:
        ground[clay[1]][clay[0]] = "#"
    return ground

def find_max(coordinates):
    max_x = coordinates[0][0]
    max_y = coordinates[0][1]
    for coordinate in coordinates:
        max_x = max(max_x, coordinate[0])
        max_y = max(max_y, coordinate[1])
    return (max_x, max_y)

def find_min(coordinates):
    min_x = coordinates[0][0]
    min_y = coordinates[0][1]
    for coordinate in coordinates:
        min_x = min(min_x, coordinate[0])
        min_y = min(min_y, coordinate[1])
    return (min_x, min_y)

def parse_clay(lines):
    coordinates = []
    for line in lines:
        coordinate_strings = line.split(",")
        first_coord = int(coordinate_strings[0].split("=")[1])
        second_coord = coordinate_strings[1].split("=")[1]
        second_coord_low = int(second_coord.split("..")[0])
        second_coord_high = int(second_coord.split("..")[1])

        if coordinate_strings[0][0] == "x":
            x_coord = first_coord
            for y_coord in range(second_coord_low, second_coord_high+1):
                coordinates.append([x_coord, y_coord])

        else:
            y_coord = first_coord
            for x_coord in range(second_coord_low, second_coord_high+1):
                coordinates.append([x_coord, y_coord])


    return coordinates

def part1():
    # Input File
    filename = "./day17/input.txt"

    # Sample Input
    # filename = "./day17/sample.txt"

    # Read the file
    with open(filename, "r") as infile:
        lines = [line for line in infile]

    # Get all the clay veins, and the min/max for x and y
    clay_veins = parse_clay(lines)
    max_x, max_y = find_max(clay_veins)
    min_x, min_y = find_min(clay_veins)

    # The array doesn't need anything past the max values
    # But it does need to be filled
    ground = make_ground(max_x, max_y, clay_veins)
    ground[0][500] = "|"

    sys.setrecursionlimit(5000)

    # The initial water source is always in the same place
    fill_down(ground, (500,0), max_y)
    # print_ground(ground, min_x, max_x)

    # Now we need to count the water
    water_count = 0
    standing_water = 0
    for line in ground[min_y:max_y+1]:
        standing_water += line.count("~")
        water_count += line.count("~") + line.count("|")
                  
    print(f"Water count: {water_count}")
    print(f"Standing water: {standing_water}")

def fill_down(ground, source, max_y):
    # Get the current x and y values
    cx, cy = source

    # If we're past the bottom of the ground
    if cy >= max_y:
        return

    # If we're over sand, just fill to it
    if ground[cy+1][cx] == ".":
        ground[cy+1][cx] = "|"
        fill_down(ground, (cx, cy+1), max_y)

    # If we're over clay or standing water, and there's room to the right
    if (ground[cy+1][cx] in ["#", "~"]) and ground[cy][cx+1] == ".":
        ground[cy][cx+1] = "|"
        fill_down(ground, (cx+1, cy), max_y)

    # If we're over clay or standing water, and there's room to the left
    if (ground[cy+1][cx] in ["#", "~"]) and ground[cy][cx-1] == ".":
        ground[cy][cx-1] = "|"
        fill_down(ground, (cx-1, cy), max_y)

    # Change the | chars to ~ chars if we have walls
    if has_walls(ground, (cx, cy)):
        fill_level(ground, (cx, cy))

# Do we have both walls?
def has_walls(ground, source):
    return has_wall(ground, source, True) and has_wall(ground, source, False)

# Do we have a wall to one side?
def has_wall(ground, source, left):
    cx, cy = source
    while True:
        if ground[cy][cx] == ".":
            return False
        if ground[cy][cx] == "#":
            return True
        if left:
            cx -= 1
        else:
            cx += 1

# Fill the current level
def fill_level(ground, source):
    fill_side(ground, source, True)
    fill_side(ground, source, False)

# Fill to one side
def fill_side(ground, source, left):
    cx, cy = source
    while True:
        if ground[cy][cx] == "#":
            return
        ground[cy][cx] = "~"
        if left:
            cx -= 1
        else:
            cx += 1

if __name__ == "__main__":
    part1()