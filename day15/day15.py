"""
Day 15 AOC 2018
"""

import actor


def part1():
    # Input File
    # filename = "./day15/input.txt"

    # Sample Input
    filename = "./day15/sample1.txt"
    # filename = "./day15/sample2.txt"
    # filename = "./day15/sample3.txt"
    # filename = "./day15/sample4.txt"
    # filename = "./day15/sample5.txt"
    # filename = "./day15/sample6.txt"

    # Cave system
    cave = []

    # Read the file line by line
    with open(filename, "r") as infile:
        for line in infile:
            cave.append([ch for ch in line.rstrip()])

    # Find all the goblins and elves
    actors = []
    for y in range(len(cave)):
        for x in range(len(cave[y])):
            if cave[y][x] in "GE":
                actors.append(actor.Actor(x, y, cave[y][x]))

    # Sort everything in reading order (first by x, then by y)
    actors.sort(key=lambda char: char.x)
    actors.sort(key=lambda char: char.y)

    # Now find what is in everyone's range to start
    for char in actors:
        x = char.x
        y = char.y
        char.in_range.clear()
        if cave[y - 1][x] == ".":
            char.in_range.append([x, y - 1])
        if cave[y][x - 1] == ".":
            char.in_range.append([x - 1, y])
        if cave[y][x + 1] == ".":
            char.in_range.append([x + 1, y])
        if cave[y + 1][x] == ".":
            char.in_range.append([x, y + 1])

    # OK, let's start - starting with round 0
    round = 0

    # Get out initial count of goblins and elves
    goblins = sum([1 for char in actors if char.actor_type == "G"])
    elves = sum([1 for char in actors if char.actor_type == "E"])

    # While there is still something to do
    while goblins > 0 and elves > 0:
        # Do our thing
        pass

    # Add the HP for the everyone left
    total_hp = sum([char.HP for char in actors if char.actor_type != "."])
    print(f"Part 1: Total is {round} rounds and {total_hp} HP for {total_hp * round}.")


if __name__ == "__main__":
    part1()
