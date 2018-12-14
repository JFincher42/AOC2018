'''
Day 10, AoC 2018
'''

%matplotlib inline

import time
import matplotlib.pyplot as plt
filename = "/home/jon/git/AoC2018/day10/input.txt"

# Answer is FNRGPBHR
def part(1):
    # Sample Input data
    # filename = "./day10/sample.txt"

    # Read the file line by line
    point_x = []
    point_y = []

    velocity_x = []
    velocity_y = []

    with open(filename, "r") as infile:
        for line in infile:
            point_x.append(int(line[10:16]))
            point_y.append(int(line[18:24]))

            velocity_x.append(int(line[36:38]))
            velocity_y.append(int(line[40:42]))

    iterations=0
    while True:
        if iterations > 10500 and iterations < 10600:
            print(f"Iteration: {iterations}")
            plt.scatter(point_x, point_y)
            plt.show()
        for i in range(len(point_x)):
            point_x[i] += velocity_x[i]
            point_y[i] += velocity_y[i]
        iterations += 1

if __name__ == "__main__":
    part1()