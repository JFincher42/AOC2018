'''
AoC 2018 Day 20
'''
import numpy as np
import sys

# CONSTANTS
NORTH   = 1
WEST    = 2
SOUTH   = 4
EAST    = 8
VISITED = 16

def part1():
    # The map is a global so everyone can access it easily
    global map

    # As we go along, we may need to add rows or columns to the map
    global add_rows, add_cols

    # Input File
    filename = "./day20/input.txt"

    # Sample Input
    # filename = "./day20/sample1.txt"
    # filename = "./day20/sample2.txt"
    # filename = "./day20/sample3.txt"
    # filename = "./day20/sample4.txt"
    # filename = "./day20/sample5.txt"

    # Setup a global numpy array to track our position
    # We encode open doors in bytes
    # -           1: North
    # - 2: West              8: East
    # -           4: South
    #
    # We assume all doors marked zero are closed
    map = np.zeros([100,100], dtype=np.int64)
    
    # Start in the middle
    # We can add items as necessary to grow the array
    # Add to the NORTH: map = np.insert(map,           0 , [0], 0)  
    # Add to the SOUTH: map = np.insert(map, map.shape[0], [0], 0)
    # Add to the EAST:  map = np.insert(map, map.shape[1], [0], 1)
    # Add to the WEST:  map = np.insert(map,           0 , [0], 1)
    cx, cy = 48, 48
    add_rows, add_cols = 0, 0

    # Read the file
    with open(filename, "r") as infile:
        # Read until the starting char is seen
        ch = infile.read(1)
        while ch != '^':
            ch = infile.read(1)

        # Now read the char past the beginning character
        ch = infile.read(1)

        # We are basically implementing a recursive descent parser
        # There are four types of characters we can see
        # - The letters E, N, W, or S, indicating a direction from the current location
        # - An open parentheses, indicating the start of a set of branches
        # - A closed parentheses, indicating the end of a set of branches
        #   This is only a valid character after an opening paren
        # - A vertical bar (|), indicating the end of a branch, and the start of another
        # 
        # We assume the input is correct, so we're not doing any error checking

        parse(ch, infile, cx, cy)

    # Let's clean all the extra zero rows/cols the map
    # Adjust CX/CY as appropriate as well
    # First clear out any extra rows/cols from the beginning
    while (np.all(map[0] == 0)):
        map = np.delete(map,0,0)
        add_rows -= 1
    while (np.all(map[:,0] == 0)):
        map = np.delete(map,0,1)
        add_cols -= 1
    while (np.all(map[-1] == 0)):
        map = np.delete(map,-1,0)
    while (np.all(map[:,-1] == 0)):
        map = np.delete(map,-1,1)

    # If we added rows and columns, we need to increment cx and cy to account for them
    cx += add_cols
    cy += add_rows

    # and then print it to check
    # print(map)
    # print(f"Width = {len(map[0])}")
    # print(f"CX = {cx}, CY = {cy}")

    # Now we find the longest path
    find_longest(cx, cy, 0)

    # Flatten map, find the largest number
    print(f"Longest path is {np.amax(map) >> 8}")

def part2():
    global map

    flattened_map = np.sort(map, axis=None)
    top_paths = flattened_map[np.where(flattened_map > (1000<<8))]
    print(f"Part 2: 1000 door paths: {len(top_paths)}")

def find_unvisited_neighbors(cx, cy):
    '''
    Finds all the neighbors of the given coordinate which have not been visited
    Returns a list of tuples of map coordinates of the unvisited neighbors
    If there are none, the returned list has zero elements.
    '''

    global map

    neighbors = []
    if map[cy, cx] & NORTH and not map[cy-1, cx] & VISITED:
        neighbors.append((cx, cy-1))
    if map[cy, cx] & SOUTH and not map[cy+1, cx] & VISITED:
        neighbors.append((cx, cy+1))

    if map[cy, cx] & EAST and not map[cy, cx+1] & VISITED:
        neighbors.append((cx+1, cy))
    if map[cy, cx] & WEST and not map[cy, cx-1] & VISITED:
        neighbors.append((cx-1, cy))

    return neighbors


def find_longest(cx, cy, path_len):
    '''
    Traverses the entire map and notesd how many steps it takes to get everywhere
    Uses a variation of a longest path algorithm for acyclic digraphs, since our map 
    is basically a digraph.

    Uses iteration if there is a single path, and recursion to handle multiple paths
    If there are no more paths, we return
    '''

    global map
    # Starting at cx, cy we do the following:
    # - Mark the current node as visited, and set the path_len
    # - Find all the unvisited nodes adjacent to us
    # - If there are none, we are done
    # - If there is only one, move to that one and loop
    # - If there is more than one, recursively scan each

    looping = True
    while looping:
        map[cy, cx] |= VISITED
        map[cy, cx] = (map[cy, cx] & 255) | (path_len << 8)
        neighbors = find_unvisited_neighbors(cx, cy)
        if len(neighbors) == 0:
            looping = False
    
        elif len(neighbors) == 1:
            cx, cy = neighbors[0]
            path_len += 1

        else:
            for neighbor in neighbors:
                cx, cy = neighbor
                find_longest(cx, cy, path_len+1)
            #looping = False

def parse(ch, infile, cx, cy):
    global map
    global add_rows, add_cols
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
                map = np.insert(map, 0, 0, 0)
                # And adjust all our y-coordinates to reflect a new row
                cy += 1
                save_cy += 1
                add_rows += 1
            # Move north
            cy -= 1
            # And add a south door here
            map[cy, cx] |= SOUTH

        elif ch == "S":
            # Add a south door
            map[cy, cx] |= SOUTH

            # Can we move south? If not, add a row below us
            if cy == map.shape[0]-1:
                map = np.insert(map, map.shape[0], 0, 0)
            cy += 1
            # Now add a north door here
            map[cy, cx] |= NORTH

        elif ch == "W":
            # Add a west door
            map[cy,cx] |= WEST

            # Can we move west? If not, add a column to the left
            if cx == 0:
                map = np.insert(map, 0, 0, 1)
                cx += 1
                save_cx += 1
                add_cols += 1
            cx -= 1
            # Now add an east door here
            map[cy, cx] |= EAST

        elif ch == "E":
            # Add an east door
            map[cy, cx] |= EAST

            # Can we move east? If not, add a row to the right
            if cx == map.shape[1]-1:
                map = np.insert(map, map.shape[1], 0, 1)
            cx += 1
            # Now add a west door here
            map[cy, cx] |= WEST

        # An open paren - we recurse through this
        elif ch == "(":
            # Read the char past the open paren, and recurse
            ch = infile.read(1)
            parse(ch, infile, cx, cy)

        # A branch char, so continue from our saved position
        elif ch == "|":
            # Reset CX/CY to the saved values
            cx, cy = (save_cx, save_cy)

        # Something else - just return
        else:
            return
    
        # Get the next char
        ch = infile.read(1)

if __name__ == "__main__":
    part1()
    part2()