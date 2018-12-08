'''
Day 7, AoC 2018
'''

import node

def part1():
    # Starting point
    steps = {}

    # Open the file and read each line
    filename = "./day07/input.txt"
    # filename = "./day07/sample.txt"

    # Read the file line by line
    # Track the maximum x and y coordinates so we know when we can stop
    with open(filename, "r") as infile:
        for line in infile:
            # Get the prereq and subsequent step names
            pre = line[5]
            sub = line[36]

            # Do we already have either of these nodes?
            # If not, create new nodes for them

            if pre not in steps:
                steps[pre] = node.Node(pre)
            if sub not in steps:
                steps[sub] = node.Node(sub)

            # Add the sub as a child of the pre
            steps[pre].add_next_step(steps[sub])
            steps[sub].prereqs += 1

    # Now we need to find the head nodes
    # Get a list of all nodes
    node_list = sorted(steps)

    # Now check each list of next_steps, and remove them from the node_list
    for step in steps:
        for next_step in steps[step].next_steps:
            if next_step.name in node_list:
                node_list.remove(next_step.name)

    # At this point, node_list has the list of next items
    # So let's loop through this list until it's empty
    # and build our output string
    output_string = ""
    while len(node_list)>0:
        # Get the next node to process
        current_node_name = node_list.pop(0)
        # If we haven't already output it
        if current_node_name not in output_string:
            # Output it
            output_string += current_node_name

            # Now find the next steps from the current node that have a single prereqs
            next_step_names = steps[current_node_name].get_next_step_names()
            for next_step_name in next_step_names:
                if steps[next_step_name].prereqs == 1:
                    node_list.append(next_step_name)
                else:
                    # Reduce the number of prereqs
                    steps[next_step_name].prereqs -= 1

            node_list.sort()
    
    # Now we can print the final string
    print(f"Part 1: Order = {output_string}")

if __name__ == "__main__":
    part1()
    # part2()