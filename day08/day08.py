'''
Day 8, AoC 2018
'''

import node

def build_tree(nodeinfo, index):
    num_children = nodeinfo[index]
    index += 1
    num_metadata = nodeinfo[index]
    index += 1
    new_node = node.Node(num_children, num_metadata)

    if num_children > 0:
        for child_count in range(num_children):
            new_node.children.append(None)
            new_node.children[child_count], index = build_tree(nodeinfo, index)

    if num_metadata > 0:
        for metadata_count in range(num_metadata):
            new_node.metadata.append(nodeinfo[index])
            index += 1
    
    return new_node, index

def part1():
    # Starting point

    # Open the file and read each line
    filename = "./day08/input.txt"
    # filename = "./day08/sample.txt"

    # Read the file line by line
    with open(filename, "r") as infile:
        nodeinfo = [int(x) for x in infile.readline().split()]
    
    head, index = build_tree(nodeinfo, 0)

    print(f"Part 1: Metadata sum = {head.sum_metadata()}")
    print(f"Part 2: Child metadata sum = {head.sum_childmetadata()}")

if __name__ == "__main__":
    part1()