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
        self.in_someones_range = False

    def calc_in_range(self, cave):
        self.in_range.clear()
        if cave[self.y - 1][self.x] == ".":
            self.in_range.append([self.x, self.y - 1])
        if cave[self.y][self.x - 1] == ".":
            self.in_range.append([self.x - 1, self.y])
        if cave[self.y][self.x + 1] == ".":
            self.in_range.append([self.x + 1, self.y])
        if cave[self.y + 1][self.x] == ".":
            self.in_range.append([self.x, self.y + 1])

        # Is someone else in range
        if self.actor_type == "G":
            enemy_type = "E"
        else:
            enemy_type = "G"
        
        self.in_someones_range = (cave[self.y - 1][self.x] == enemy_type or 
                                  cave[self.y][self.x - 1] == enemy_type or 
                                  cave[self.y][self.x + 1] == enemy_type or 
                                  cave[self.y + 1][self.x] == enemy_type)
        
    
    def calc_damage(self, damage, cave):
        self.HP -= 3
        if self.HP <= 0:
            self.HP = 0
            self.actor_type = "."
            self.in_range.clear()
            cave[self.y][self.x] = "."
