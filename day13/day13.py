'''
Day 13, AoC 2018
'''

def find_collision(cars):
    for i in range(len(cars)-1):
        for j in range(i+1,len(cars)):
            # Ignore previous crashes
            if cars[i][3] != "*" and cars[j][3] != "*":
                if cars[i][0] == cars[j][0] and cars[i][1] == cars[j][1]:
                    cars[i][3] = "*"
                    cars[j][3] = "*"
                    return [cars[i][0],cars[i][1]]
    return []

def check_last_car(cars):
    remaining_cars = len(cars) - sum([1 for car in cars if car[3] == "*"])
    if remaining_cars == 1:
        for i in range(len(cars)):
            if cars[i][3] != "*":
                return i
    else:
        return -1

def part1():
    # Input File
    filename = "./day13/input.txt"

    # Sample Input
    # filename = "./day13/sample.txt"

    # Initial state
    maze = []
    cars = []

    # Read the file line by line
    with open(filename, "r") as infile:
        maze = [line for line in infile]

    # Find all the cars in the maze, and replace them with their proper lines
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] in "^v<>":
                # Each car has:
                # - an x, y position, 
                # - a turn preference (0=left, 1=straight, 2=right)
                # - a current direction
                cars.append([x,y,0,maze[y][x]])

                # Replace the car with a proper line
                if maze[y][x] == "^" or maze[y][x] == "v":
                    maze[y] = maze[y][0:x] + "|" + maze[y][x+1:]
                if maze[y][x] == ">" or maze[y][x] == "<":
                    maze[y] = maze[y][0:x] + "-" + maze[y][x+1:]

    # Let's start the fun!
    collision = False
    tick = 0
    while not collision:

        # Start each tick by sorting the cars from left to right, then top to bottom
        cars.sort(key=lambda tup:tup[0])
        cars.sort(key=lambda tup:tup[1])

        # Process each car in turn
        for car in cars:
            # Get the car data
            x, y, turn, direction = car
            
            # Which way are we headed? Get the next place to move
            current_step = maze[y][x]
            
            # First, skip any cars in a collision already
            if direction == "*":
                pass

            # UP
            elif direction == "^":
                # First, which way do we move?
                # If it's straight, keep going
                if current_step == "|":
                    y -= 1

                # If we're turning, turn and head that direction
                elif current_step == "/":
                    direction = ">"
                    x += 1
                elif current_step == "\\":
                    direction = "<"
                    x -= 1
                
                # It's an intersection, figure out the turn
                elif current_step == "+":
                    if turn == 0:
                        direction = "<"
                        x -= 1
                    elif turn == 1:
                        y -= 1
                    else:
                        direction = ">"
                        x += 1
                    turn = (turn + 1) % 3

                # Something's gone horribly wrong
                else:
                    raise Exception("We're off the range!")

            # DOWN
            elif direction == "v":
                # First, which way do we move?
                # If it's straight, keep going
                if current_step == "|":
                    y += 1

                # If we're turning, turn and head that direction
                elif current_step == "/":
                    direction = "<"
                    x -= 1
                elif current_step == "\\":
                    direction = ">"
                    x += 1
                
                # It's an intersection, figure out the turn
                elif current_step == "+":
                    if turn == 0:
                        direction = ">"
                        x += 1
                    elif turn == 1:
                        y += 1
                    else:
                        direction = "<"
                        x -= 1
                    turn = (turn + 1) % 3

                # Something's gone horribly wrong
                else:
                    raise Exception("We're off the range!")

            # LEFT
            elif direction == "<":
                # First, which way do we move?
                # If it's straight, keep going
                if current_step == "-":
                    x -= 1

                # If we're turning, turn and head that direction
                elif current_step == "/":
                    direction = "v"
                    y += 1
                elif current_step == "\\":
                    direction = "^"
                    y -= 1
                
                # It's an intersection, figure out the turn
                elif current_step == "+":
                    if turn == 0:
                        direction = "v"
                        y += 1
                    elif turn == 1:
                        x -= 1
                    else:
                        direction = "^"
                        y -= 1
                    turn = (turn + 1) % 3

                # Something's gone horribly wrong
                else:
                    raise Exception("We're off the range!")

            # RIGHT
            else:
                # First, which way do we move?
                # If it's straight, keep going
                if current_step == "-":
                    x += 1

                # If we're turning, turn and head that direction
                elif current_step == "/":
                    direction = "^"
                    y -= 1
                elif current_step == "\\":
                    direction = "v"
                    y += 1
                
                # It's an intersection, figure out the turn
                elif current_step == "+":
                    if turn == 0:
                        direction = "^"
                        y -= 1
                    elif turn == 1:
                        x += 1
                    else:
                        direction = "v"
                        y += 1
                    turn = (turn + 1) % 3

                # Something's gone horribly wrong
                else:
                    raise Exception("We're off the range!")            
            
            # Now save the car state
            # print(f"Tick {tick}: Car at ({x}, {y}), turn {turn}, direction '{direction}'")
            car[0] = x
            car[1] = y
            car[2] = turn
            car[3] = direction
            
            # Now check for a collision
            collision_location = find_collision(cars)
            # collision = (len(collision_location)>0)
            # if collision:
            #     break
        
        # Check for only one car left
        last_car = check_last_car(cars)
        if last_car == -1:
            tick += 1
        else:
            print(f"Part 2: Last car at ({cars[last_car][0]}, {cars[last_car][1]})")
            break

    print(f"Part 1: First collision at ({collision_location[0]}, {collision_location[1]}), tick {tick}")

if __name__ == "__main__":
    part1()