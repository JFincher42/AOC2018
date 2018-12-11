'''
Day 10, AoC 2018
'''

import node
# import pygame
import numpy as np
from matplotlib import pyplot as plt

def part1():
    # Input data
    filename = "./day10/input.txt"

    # Sample Input data
    # filename = "./day10/sample.txt"

    nodes = []

    # Read the file line by line
    # Track the maximum x and y coordinates so we know when we can stop
    with open(filename, "r") as infile:
        for line in infile:
            pos_x = int(line[10:16])
            pos_y = int(line[18:24])

            vel_x = int(line[36:38])
            vel_y = int(line[40:42])
            nodes.append(node.Node(pos_x, pos_y, vel_x, vel_y))

    low_x, low_y, high_x, high_y = 0,0,0,0
    for current_node in nodes:
        if current_node.position[0] < low_x:
            low_x = current_node.position[0]
        if current_node.position[0] > high_x:
            high_x = current_node.position[0]

        if current_node.position[1] < low_y:
            low_y = current_node.position[1]
        if current_node.position[1] > high_y:
            high_y = current_node.position[1]

    # Setup the drawing surface to be big enough to handle all the points
    surface_x = abs(low_x) + abs(high_x) + 1
    surface_y = abs(low_y) + abs(high_y) + 1

    pixel_array = np.zeros((surface_x, surface_y), dtype=np.int8)

    # Setup pygame
    # pygame.init()

    # Setup a window to draw the pixels
    # w = pygame.display.set_mode([surface_x, surface_y], pygame.RESIZABLE)
    # w.fill([0,0,0])

    # Setup a pixel array to draw the pixels
    # pixels = pygame.PixelArray(w)

    while True:
        for current_node in nodes:
            surf_x = current_node.position[0] - low_x
            surf_y = current_node.position[1] - low_y
            pixel_array[surf_x, surf_y] = 1
            
        plt.title("Part 1") 
        plt.xlabel("x") 
        plt.ylabel("y") 
        plt.plot(pixel_array,".k")
        plt.show()
        input("Hit Enter to move...")
        
        for current_node in nodes:
            surf_x = current_node.position[0] - low_x
            surf_y = current_node.position[1] - low_y
            pixel_array[surf_x, surf_y] = 0 

            current_node.move_node()

if __name__ == "__main__":
    part1()