'''
Day 1, AoC 2018
'''

def part1():
    # Starting point
    frequency = 0

    # Open the file
    filename = "./day01/day01input.txt"
    with open(filename, "r") as infile:

        # Get each line of the file...
        # ...convert it to an int...
        # ...and add it to the frequency
        for line in infile:
            frequency += int(line)

    # Now print the final frequency
    print(f"Part 1: Frequency = {frequency}")

def part2():
    # Starting point
    frequency = 0
    frequency_list = []

    # Open the file
    filename = "./day01/day01input.txt"
    #filename = "./day01/sample.txt"
    with open(filename, "r") as infile:

        duplicated = False
        # While we don't have a duplicate yet
        while not duplicated:
            # Go to the beginning of the file
            infile.seek(0)

            # Get each line of the file...
            # ...and add it to the frequency
            for line in infile:
                # ...convert it to an int and add it to the frequency
                frequency += int(line)

                # If it's not a duplicate, add it to the list
                if frequency not in frequency_list:
                    frequency_list.append(frequency)
                else:
                    duplicated = True
                    break

    # Now print the final frequency
    print(f"Part 2: Repeated Frequency = {frequency}")

if __name__ == "__main__":
    part1()
    part2()