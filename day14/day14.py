'''
Day 13, AoC 2018
'''

def new_scores(total):
    if total > 9:
        return [int(total/10), total%10]
    else:
        return [total]

def part1():
    # Input number
    practice = 793031

    # Sample input
    # practice = 2018

    # Recipes
    recipes = [3, 7]

    # Where is each elf
    elves = [0, 1]

    # Loop through all the practice rounds
    # for i in range(practice):
    while len(recipes) <= practice+10:
        recipes.extend(new_scores(recipes[elves[0]] + recipes[elves[1]]))
        recipe_count = len(recipes)
        elves[0] = (elves[0] + recipes[elves[0]] + 1) % recipe_count
        elves[1] = (elves[1] + recipes[elves[1]] + 1) % recipe_count

    # Find the ten digits after the last elf
    best_recipes = ""
    for i in range(practice, practice+10):
        best_recipes += str(recipes[i])

    print(f"Part 1: Ten best recipes are: {best_recipes}")

if __name__ == "__main__":
    part1()
