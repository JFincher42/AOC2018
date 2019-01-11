'''
AoC 2018 Day 21
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

def part1():
    # Input File
    filename = "./day21/input.txt"

    # Registers and other important things
    # Part 1
    registers = [0, 0, 0, 0, 0, 0]

    ip = 0
    ip_register = 0
    program = []

    # The dictionary of instructions
    instruction_set = { "addr":addr, "addi":addi, "mulr":mulr, "muli":muli, 
                        "banr":banr, "bani":bani, "borr":borr, "bori":bori, 
                        "setr":setr, "seti":seti, "gtir":gtir, "gtri":gtri, 
                        "gtrr":gtrr, "eqir":eqir, "eqri":eqri, "eqrr":eqrr}

    # Read the file
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile]

    # The first line is the IP register
    ip_register = int(lines[0][3:])

    # The next are the program
    for index in range(1,len(lines)):
        inst, in1, in2, out = lines[index].split()
        program.append([inst, int(in1), int(in2), int(out)])

    # Any IP >= this is off the end of the program
    last = len(program)

    # PART 2
    hashes = []

    # Now we can execute 
    while ip>=0 and ip<last:
        # Move IP to register
        registers[ip_register] = ip

        # SPECIAL FOR PART 2:
        if ip == 28:                # My comparison instruction
            if registers[2] in hashes:
                print(f"Register[2] = {registers[2]}")
                print(f"Last value = {hashes[-1]}")
                break
            else:
                hashes.append(registers[2])

        # Execute next instruction
        inst, in1, in2, out = program[ip]
        registers = instruction_set[inst](in1, in2, out, registers)
        
        # Read IP back from register
        ip = registers[ip_register]

        # Increment IP
        ip += 1

    print(f"Program done, register[0]={registers[0]}")

if __name__ == "__main__":
    part1()