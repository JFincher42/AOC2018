'''
AoC 2018 Day 20
'''
import numpy as np

# CONSTANTS
NORTH = 1
WEST  = 2
SOUTH = 4
EAST  = 8

def part1():
    global map
    # Input File
    # filename = "./day20/input.txt"

    # Sample Input
    # filename = "./day20/sample1.txt"
    # filename = "./day20/sample2.txt"
    # filename = "./day20/sample3.txt"
    # filename = "./day20/sample4.txt"
    filename = "./day20/sample5.txt"

    # Setup a global numpy array to track our position
    # We encode open doors in bytes
    # -           1: North
    # - 2: West              8: East
    # -           4: South
    #
    # We assume all doors marked zero are closed
    map = np.zeros([10,10], dtype=np.int64)
    
    # Start in the middle
    # We can add items as necessary to grow the array
    # Add to the NORTH: map = np.insert(map,           0 , [0], 0)  
    # Add to the SOUTH: map = np.insert(map, map.shape[0], [0], 0)
    # Add to the EAST:  map = np.insert(map, map.shape[1], [0], 1)
    # Add to the WEST:  map = np.insert(map,           0 , [0], 1)
    cx, cy = (5, 5)

    # Read the file
    with open(filename, "r") as infile:
        # Read until the starting char is seen
        ch = infile.read(1)
        while ch != '^':
            ch = infile.read(1)

        # Now read until the final char is seen
        ch = infile.read(1)
        # OK, now we do a recursive descent parser
        # There are four types of characters we can see
        # - The letters E, N, W, or S, indicating a directions from the current location
        # - An open parentheses, indicating the start of a set of branches
        # - A closed parentheses, indicating the end of a set of branches
        # - A vertical bar (|), indicating the end of a branch, and the start of another

        parse(ch, infile, cx, cy)

    # We're done, let's clean all the extra zero rows/cols the map
    # Adjust CX/CY as appropriate as well
    while (np.all(map[0] == 0)):
        map = np.delete(map,0,0)
        cy -= 1
    while (np.all(map[:,0] == 0)):
        map = np.delete(map,0,1)
        cx -= 1
    while (np.all(map[-1] == 0)):
        map = np.delete(map,-1,0)
    while (np.all(map[:,-1] == 0)):
        map = np.delete(map,-1,1)

    # and then print it to check
    print(map)
    print(f"CX = {cx}, CY = {cy}")
            
def parse(ch, infile, cx, cy):
    global map
    # ch is the current character
    # infile is where to get the next character
    # cx, cy is the current position on the map

    # Save the current position - we will need it if we hit a branch
    save_cx, save_cy = (cx, cy)

    while ch != "$":
        # What character are we looking at?
        # Close paren - we're done recursing
        if ch == ")":
            return

        # One of our directions
        elif ch == "N":
            # Add a north door
            map[cy, cx] |= NORTH

            # Can we move north? If not, add a row above us
            if cy == 0:
                map = np.insert(map, 0, [0], 0)
                cy += 1
                save_cy += 1
            cy -= 1
            # Now add a south door here
            map[cy, cx] |= SOUTH

        elif ch == "S":
            # Add a south door
            map[cy, cx] |= SOUTH

            # Can we move south? If not, add a row below us
            if cy == map.shape[0]:
                map = np.insert(map, map.shape[0], [0], 0)
            cy += 1
            # Now add a north door here
            map[cy, cx] |= NORTH

        elif ch == "W":
            # Add a west door
            map[cy,cx] |= WEST

            # Can we move west? If not, add a column to the left
            if cx == 0:
                map = np.insert(map, 0, [0], 1)
                cx += 1
                save_cx += 1
            cx -= 1
            # Now add an east door here
            map[cy, cx] |= EAST

        elif ch == "E":
            # Add an east door
            map[cy, cx] |= EAST

            # Can we move east? If not, add a row to the right
            if cx == map.shape[1]:
                map = np.insert(map, map.shape[1], [0], 1)
            cx += 1
            # Now add a west door here
            map[cy, cx] |= WEST

        # An open paren - we recurse through this
        elif ch == "(":
            ch = infile.read(1)
            parse(ch, infile, cx, cy)

        # A branch char - we recurse, but from our saved position
        elif ch == "|":
            # Reset CX/CY to the saved values
            cx, cy = save_cx, save_cy
            # parse(ch, infile, save_cx, save_cy)

        # Something else - just return
        else:
            return
    
        # Get the next char
        ch = infile.read(1)

if __name__ == "__main__":
    part1()