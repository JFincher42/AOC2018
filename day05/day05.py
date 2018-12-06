'''
Day 5, AoC 2018
'''

upper = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
lower = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

def part1():
    # Starting point
    characters = []

    # Open the file and read each line
    filename = "./day05/day05input.txt"
    # filename = "./day05/sample.txt"
    with open(filename, "r") as infile:
        char = infile.read(1)
        while char != "":
            characters.append(char)
            char = infile.read(1)

    print(f"Starting string length is {len(characters)}")
    i = 0
    while i < len(characters)-1:
        current_char = characters[i]
        next_char = characters[i+1]
        if current_char in upper and next_char in lower:
            if upper.index(current_char) == lower.index(next_char):
                characters[i:i+2] = []
                i = max (0, i-1)
                #print(f"Removed '{current_char}' and '{next_char}', remaining '{''.join(characters)}'")
            else:
                i += 1
        elif current_char in lower and next_char in upper:
            if lower.index(current_char) == upper.index(next_char):
                characters[i:i+2] = []
                i = max (0, i-1)
                #print(f"Removed '{current_char}' and '{next_char}', remaining '{''.join(characters)}'")
            else:
                i += 1
        else:
            i += 1
            
    print(f"Part 1: Remaining string length: {len(characters)}")

def react_polymer(uch, lch, chars):
    while True:
        try:
            chars.remove(uch)
        except:
            break

    while True:
        try:
            chars.remove(lch)
        except:
            break

    i = 0
    while i < len(chars)-1:
        current_char = chars[i]
        next_char = chars[i+1]
        if current_char in upper and next_char in lower:
            if upper.index(current_char) == lower.index(next_char):
                chars[i:i+2] = []
                i = max (0, i-1)
                #print(f"Removed '{current_char}' and '{next_char}', remaining '{''.join(characters)}'")
            else:
                i += 1
        elif current_char in lower and next_char in upper:
            if lower.index(current_char) == upper.index(next_char):
                chars[i:i+2] = []
                i = max (0, i-1)
                #print(f"Removed '{current_char}' and '{next_char}', remaining '{''.join(characters)}'")
            else:
                i += 1
        else:
            i += 1
    return len(chars)

def part2():
    # Starting point
    characters = []

    # Open the file and read each line
    filename = "./day05/day05input.txt"
    with open(filename, "r") as infile:
        char = infile.read(1)
        while char != "":
            characters.append(char)
            char = infile.read(1)

    minlen = len(characters)
    for upper_char in upper:
        lower_char = upper_char.lower()
        print(f"Removing {upper_char} and {lower_char}")
        newlen = react_polymer(upper_char, lower_char, characters[:])
        if newlen < minlen:
            minlen = newlen
            print(f" New minlen: {minlen}")

    print(f"Part 2: Minimum length: {minlen}")

if __name__ == "__main__":
    # part1()
    part2()