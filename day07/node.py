'''
Node class for Day 5 solution
'''

class Node:

    def __init__(self, name):
        self.name = name
        self.next_steps = []
        self.cost = ord(name) - ord('A') + 61
        self.prereqs = 0

    def add_next_step(self, next_step):
        if next_step not in self.next_steps:
            self.next_steps.append(next_step)
            self.next_steps.sort(key=lambda node: node.name, reverse=True)

    def get_next_step_names(self):
        next_step_names = []
        for next_step in self.next_steps:
            next_step_names.append(next_step.name)
        return next_step_names
