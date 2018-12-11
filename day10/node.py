'''
Node structure for Day 10 of AoC
'''

class Node:

    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.position = [pos_x, pos_y]
        self.velocity = [vel_x, vel_y]

    def move_node(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        