'''
Day 10, AoC 2018
'''
import numpy as np

def part1():
    serial = 9110

    fuelcells = np.empty((300,300), dtype=np.int64)

    # Setup the fuel cells
    for x in range(300):
        for y in range(300):
            rackid = (x + 11)
            power = (rackid * (y+1)) + serial       # Add 1 to x and y since we're 0-based
            power = int((power*rackid)/100)%10      # Get hundreds digit
            fuelcells[x,y] = power - 5

    # Now we find the maximum power
    maxpower = 0
    maxpower_x = 0
    maxpower_y = 0
    for x in range(297):
        for y in range(297):
            power = sum(sum(fuelcells[x:x+3, y:y+3]))
            if power > maxpower:
                maxpower = power
                maxpower_x = x + 1
                maxpower_y = y + 1
    
    print(f"Max Power: {maxpower}, X:{maxpower_x}, Y:{maxpower_y}")

    # Now we find the maximum power, any size
    maxpower = 0
    maxpower_x = 0
    maxpower_y = 0
    maxsize = 1
    for x in range(300):
        for y in range(300):
            largest_square = min(300-x, 300-y)
            for size in range(largest_square+1):
                if size > 0:
                    power = sum(sum(fuelcells[x:x+size, y:y+size]))
                    if power > maxpower:
                        maxpower = power
                        maxpower_x = x + 1
                        maxpower_y = y + 1
                        maxsize = size
                        print(f"Max Power: {maxpower}, X:{maxpower_x}, Y:{maxpower_y}, Size:{maxsize}")

    print(f"Max Power: {maxpower}, X:{maxpower_x}, Y:{maxpower_y}, Size:{maxsize}")


if __name__ == "__main__":
    part1()