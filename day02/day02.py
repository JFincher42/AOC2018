'''
Day 2, AoC 2018
'''

def part1():
    # Starting point
    letter2 = 0
    letter3 = 0

    # Open the file
    filename = "./day02/day02input.txt"
    with open(filename, "r") as infile:

        # Get each line of the file...
        for line in infile:
            # Blank out the dictionary, and set our flags to False
            line_dict = {}
            has2 = False
            has3 = False

            # For every character in the line, add it to the dictionary
            # If it's already there, increase it's count
            for char in line:
                if char in line_dict:
                    line_dict[char] += 1
                else:
                    line_dict[char] = 1

            # Now walk the dictionary, looking for double and triple occurences
            for key in line_dict:
                if line_dict[key] == 2:
                    has2 = True
                elif line_dict[key] == 3:
                    has3 = True

            if has2:
                letter2 += 1
            if has3:
                letter3 += 1

    # Now print the final checksum
    print(f"Part 1: Checksum = {letter2*letter3}")

def part2():

    line_list = []
    filename = "./day02/day02input.txt"
    with open(filename, "r") as infile:

        # Get each line of the file and put it in a list
        line_list = infile.read().splitlines()
    
    foundit = False
    current_line = 0
    found_line = 0
    while not foundit:
        for next_line in range(current_line+1,len(line_list)):
            diffs = 0
            foundit = False
            for letters in range(len(line_list[current_line])):
                if line_list[current_line][letters] != line_list[next_line][letters]:
                    diffs += 1
                if diffs > 1:
                    break
            if diffs == 1:
                foundit = True
                found_line = next_line
                break
        current_line += 1

    print(f"Part 2: Line 1: {line_list[current_line-1]}")
    print(f"Part 2: Line 2: {line_list[found_line]}")

if __name__ == "__main__":
    part1()
    part2()