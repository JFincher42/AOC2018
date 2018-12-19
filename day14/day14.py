'''
Day 13, AoC 2018
'''

def new_scores(total):
    if total > 9:
        return [int(total/10), total%10]
    else:
        return [total]

def find_sequence(sequence, recipes):
    seq_len = len(sequence)
    if len(recipes) < seq_len:
        return -1

    if recipes[-(seq_len+1):-1] == sequence:
        return len(recipes) - seq_len -1
    if recipes[-seq_len:] == sequence:
        return len(recipes) - seq_len
    return -1

def part1():
    # Input number
    practice = 793031
    practice_sequence = [7,9,3,0,3,1]

    # Sample input
    # practice = 2018
    # practice_sequence = [5,9,4,1,4]

    # Recipes
    recipes = [3, 7]

    # Where is each elf
    elves = [0, 1]

    # Loop through all the practice rounds
    # Part 1 loop
    # while len(recipes) <= practice+10:
    # Part 2 loop:
    while True:
        where_found = find_sequence(practice_sequence, recipes)
        if where_found > -1:
            break
        recipes.extend(new_scores(recipes[elves[0]] + recipes[elves[1]]))
        recipe_count = len(recipes)
        elves[0] = (elves[0] + recipes[elves[0]] + 1) % recipe_count
        elves[1] = (elves[1] + recipes[elves[1]] + 1) % recipe_count

    # Part 1:
    # Find the ten digits after the last elf
    # best_recipes = ""
    # for i in range(practice, practice+10):
    #     best_recipes += str(recipes[i])

    # print(f"Part 1: Ten best recipes are: {best_recipes}")

    # Part 2:
    print(f"Part 2: Ten best recipes appear before {where_found}.")


if __name__ == "__main__":
    part1()
