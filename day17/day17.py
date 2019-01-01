'''
Day 17  - AoC 2018
'''

def make_ground(max_x, max_y, clay_veins):
    ground = [["."] * max_x for i in range(max_y+1)]
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
    # filename = "./day17/input.txt"

    # Sample Input
    filename = "./day17/sample.txt"

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

    # The initial water source is always in the same place
    # There may be more than one stream, however, so track them all here
    water_heads = [[500, 0]]
    ground[500,0] = "~"

    # Just a counter
    round = 0

    # Keep going as long as one head of water isn't past the bottom yet
    head_min_x, head_min_y = find_min(water_heads)
    while head_min_y <= max_y:
        # We track each head of water and look to see what it will hit
        # - If it's sand, we move the head down to it
        # - If it's clay, we stop and check some assumptions

        for current_head in water_heads:
            cx, cy = current_head
            if ground[cy+1][cx] == ".":
                current_head[1] += 1
                # Draw the new water
                ground[cy+1][cx] = "~"

            elif ground[cy+1][cx] == "#":
                # One of two things happened:
                # - We hit the bottom of a basin
                # - We hit the top of a wall
                # We check by looking left and right, then down
                # If we're on the top of a wall, one or both will be sand
                if ground[cy+2][cx-1] == "." or ground[cy+2][cx+1] == ".":
                    # Here, we move our water head, and a new water head
                    current_head[0] = cx-1
                    current_head[1] = cy
                    water_heads.append([cx+1, cy])
                    # Draw the new water
                    ground[cy][cx-1] = "~"
                    ground[cy][cx+1] = "~"
                
                else:
                    # We're on the bottom of a basin
                    # We fill it bottom to top

                    # First, check for the basin width left and right
                    lx, rx = cx, cx
                    while ground[cy][lx-1] == ".":
                        lx -= 1
                    while ground[cy][rx+1] == ".":
                        rx += 1

                    # There are three cases we need to worry about
                    # - We have a clear basin to fill
                    # - We have a wall in the way
                    #   In both cases, we check each line for left/right extent
                    #   And reset lx/rx as necessary
                    # - We reach the top of the basin
                    #   We find this by checking lx/rx == "." on the current line
                    #   When we do, we move the current head to the open end
                    #   If there's another open end, we create a new head there as well

                    ground[cy][lx:rx+1] = "~"*(rx-lx+1)
                        

                    
        
        # When we hit clay, we are in a basin, so we find and mark those sides.
        #
        # Three things can happen on every line:
        # - We find the basin walls to the left and right
        #   We fill that line and move the head up
        #
        # - We find clay only on one side (we pass the basin wall)
        #   We move the head to the open side (one past the wall)
        #   We fill between the head and the clay
        #
        # - We find clay on neither side (we pass the basin wall on both sides)
        #   We create a new head on one side, and move the current head to the other
        #   We fill between the two new heads.
        #
        

        # Now we find out if we're further down than the other heads



    print(f"X Extents: {min_x} to {max_x}, Y Extents: {min_y} to {max_y}")

if __name__ == "__main__":
    part1()