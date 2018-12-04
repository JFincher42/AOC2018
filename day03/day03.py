'''
Day 3, AoC 2018
'''
import Rect

def part1():
    # Starting point
    rect_list = []

    # Open the file
    filename = "./day03/day03input.txt"
    #filename = "./day03/sample.txt"
    with open(filename, "r") as infile:
        for line in infile:

            # Each line looks like this:
            #  - Starts with hash (#), followed by a number and a space
            #  - Then left corner, comma, top corner, followed by a colon
            #  - Then the width, an 'x', and the height
            
            # Get the ID
            current_char = 1            # Bypass the leading hash
            while not line[current_char].isspace():
                current_char += 1
            id = int(line[1:current_char])
            # Skip all the cruft (whitespace and the @)
            while line[current_char].isspace() or line[current_char]=='@':
                current_char += 1
            start = current_char

            # Get the left coordinate
            while line[current_char] != ',':
                current_char += 1
            left = int(line[start:current_char])
            start, current_char = current_char+1, current_char+1

            # Get the top coordinate
            while line[current_char] != ':':
                current_char += 1
            top = int(line[start:current_char])
            start, current_char = current_char+1, current_char+1

            # Get the width
            while line[current_char] != 'x':
                current_char += 1
            width = int(line[start:current_char])
            start, current_char = current_char+1, current_char+1

            # Get the height
            height = int(line[start:])

            #print(f"{id} is ({left}, {top}, {width}, {height}).")
            rect_list.append(Rect.Rect(left, top, width, height))
    
    overlap = [[0 for i in range(1000)] for j in range(1000)]
    total_overlap = 0
    for first in range(0,len(rect_list)):
        for second in range(first+1,len(rect_list)):
            new_rect = rect_list[first].overlap(rect_list[second])
            if new_rect is not None:
                for w in range(new_rect.left, new_rect.left + new_rect.width):
                    for h in range(new_rect.top, new_rect.top + new_rect.height):
                        if not overlap[w][h]:
                            total_overlap += 1
                        overlap[w][h] = 1

    check_overlap = 0
    for i in range(0,1000):
        for j in range(0,1000):
            check_overlap += overlap[i][j]
    print(f"Part 1: Overlap = {total_overlap}")
    print(f"Part 1: Check Overlap = {check_overlap}")

if __name__ == "__main__":
    part1()
    #part2()