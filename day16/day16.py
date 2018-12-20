'''
Day 16 AOC 2018
'''

def addr(A, B, C, registers):
    registers[C] = registers[A] + registers[B]
    return registers

def addi(A, B, C, registers):
    registers[C] = registers[A] + B
    return registers

def mulr(A, B, C, registers):
    registers[C] = registers[A] * registers[B]
    return registers

def muli(A, B, C, registers):
    registers[C] = registers[A] * B
    return registers

def banr(A, B, C, registers):
    registers[C] = registers[A] & registers[B]
    return registers

def bani(A, B, C, registers):
    registers[C] = registers[A] & B
    return registers

def borr(A, B, C, registers):
    registers[C] = registers[A] | registers[B]
    return registers

def bori(A, B, C, registers):
    registers[C] = registers[A] | B
    return registers

def setr(A, B, C, registers):
    registers[C] = registers[A]
    return registers

def seti(A, B, C, registers):
    registers[C] = A
    return registers

def gtir(A, B, C, registers):
    if A > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0
    return registers

def gtri(A, B, C, registers):
    if registers[A] > B:
        registers[C] = 1
    else:
        registers[C] = 0
    return registers

def gtrr(A, B, C, registers):
    if registers[A] > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0
    return registers

def eqir(A, B, C, registers):
    if A == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0
    return registers

def eqri(A, B, C, registers):
    if registers[A] == B:
        registers[C] = 1
    else:
        registers[C] = 0
    return registers

def eqrr(A, B, C, registers):
    if registers[A] == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0
    return registers

opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
ordered_opcodes = [None]*16

def part1():
    # Input File
    filename = "./day16/input.txt"
    # filename = "./day16/input2.txt"

    # Sample Input
    # filename = "./day16/sample.txt"

    # Read the file
    with open(filename, "r") as infile:
        lines = [line for line in infile]

    # Count of triples
    triples = 0
    i = 0
    while i < len(lines):
        before_reg = [int(x) for x in lines[i][9:19].split(",")]
        instruction = [int(x) for x in lines[i+1].split(" ")]
        after_reg = [int(x) for x in lines[i+2][9:19].split(",")]
        # Skip a trailing blank line
        i += 4

        matches = []
        # Loop through the opcodes and find which ones match the output
        for opcode in opcodes:
            if after_reg == opcode(instruction[1], instruction[2], instruction[3], before_reg.copy()):
                if opcode not in ordered_opcodes:
                    matches.append(opcode)

        if len(matches) == 1:
            ordered_opcodes[instruction[0]] = matches[0]

    print(f"Part 2: Ordered count = {sum([1 for opcode in ordered_opcodes if opcode != None])}")

    # Now we can run the program
    # Starting register state
    registers = [0, 0, 0, 0]

    # Program file
    filename = "./day16/input2.txt"

    # Read the file
    with open(filename, "r") as infile:
        for line in infile:
            instruction = [int(x) for x in line.split(" ")]
            registers = ordered_opcodes[instruction[0]](instruction[1], instruction[2], instruction[3], registers)
    
    print(f"Part 2: Register[0] = {registers[0]}")

if __name__ == "__main__":
    part1()