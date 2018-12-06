'''
Point class for day 6 AoC
'''

class Day6Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.closepoints = 0
        self.infinite = False

    def dist(self, x, y):
        '''
        Calculate Manhattan distance to given coordinates
        '''
        return abs(self.x - x) + abs(self.y - y)