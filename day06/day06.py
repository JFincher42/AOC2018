'''
Day 6, AoC 2018
'''

import day6point

def part1():
    # Starting point
    points = []

    # Open the file and read each line
    filename = "./day06/day06input.txt"
    # filename = "./day06/sample.txt"

    # Read the file line by line
    # Track the maximum x and y coordinates so we know when we can stop
    max_x, max_y = 0,0
    with open(filename, "r") as infile:
        for line in infile:
            xcoord, ycoord = line.split(",")
            points.append(day6point.Day6Point(int(xcoord), int(ycoord)))
            max_x = max(int(xcoord), max_x)
            max_y = max(int(ycoord), max_y)

    # max_x += 1
    # max_y += 1

    # Brute Force!
    # Scan the entire field, calculating the distance to each point.
    # Whoever is closer gets one added to their closestpoints field
    # If two or more are closer, no one wins the point
    #
    # While we're here, check the edges as well (x,y = 0, x=max_x+1, y=max_y+1)
    # Whoever is closest to an edge has an infinite area, and we can ignore them for the
    # final result

    for x in range(max_x+1):
        for y in range(max_y+1):
            # Should this be considered an infinite point
            infinite = (x==0 or y==0 or x==max_x or y==max_y)
            # The largest Manhattan distance is the opposite corner
            closest = max_x * max_y
            closest_point = None

            for point in points:
                distance = point.dist(x, y)
                # If this point is the closest, mark it
                if distance < closest:
                    closest = distance
                    closest_point = point
            
            # Are we right on a point? We can skip that
            # if closest == 0:
                # break

            # Now scan again looking for another closest point
            shared = False
            for point in points:
                # Skip the current closest point
                shared = shared or ((point is not closest_point) and (closest == point.dist(x, y)))
            
            if not shared:
                closest_point.closepoints += 1
                closest_point.infinite = closest_point.infinite or infinite
    
    # Now we can scan the list of points for the largest area that's not infinite
    largest_area = 0
    for point in points:
        if not point.infinite:
            largest_area = max(largest_area, point.closepoints)

    print(f"Part 1: Largest non-infinite area = {largest_area}")

    ## Part 2

    region_size = 0
    for x in range(max_x+1):
        for y in range(max_y+1):
            # Figure the total distance to each point
            distance = 0
            for point in points:
                distance += point.dist(x,y)
            if distance < 10000:
                region_size += 1

    print(f"Part 2: Region of points with 10K of all points = {region_size}")

if __name__ == "__main__":
    part1()
    part2()