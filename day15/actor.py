'''
Actor class

Defines goblin and elf behavior in the cave for Day 15 AOC 2018 puzzle
'''

class Actor:

    def __init__(self, pos_x, pos_y, actor_type):
        self.x = pos_x
        self.y = pos_y
        self.actor_type = actor_type
        self.in_range = []
        self.HP = 200
        self.AP = 3