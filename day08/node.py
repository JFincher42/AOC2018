'''
Node class for Day 8 solution
'''

class Node:

    def __init__(self, num_children, num_metadata):
        self.num_children = num_children
        self.num_metadata = num_metadata

        self.children = []
        self.metadata = []

    def sum_metadata(self):
        total = sum(self.metadata)
        if self.num_children > 0:
            for child in self.children:
                total += child.sum_metadata()
        return total

    def sum_childmetadata(self):
        total = 0
        if self.num_children > 0:
            for metadata_index in range(self.num_metadata):
                if self.metadata[metadata_index] <= self.num_children:
                    total += self.children[self.metadata[metadata_index]-1].sum_childmetadata()
        else:
            total = sum(self.metadata)

        return total
