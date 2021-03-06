'''
AoC 2018 Day 19
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
    filename = "./day19/input.txt"

    # Sample Input
    # filename = "./day19/sample.txt"

    # Registers and other important things
    # Part 1
    registers = [0, 0, 0, 0, 0, 0]
    # Part 2
    # registers = [1, 0, 0, 0, 0, 0]

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

    # Now we can execute 
    while ip>=0 and ip<last:
        # Move IP to register
        registers[ip_register] = ip

        # Execute next instruction
        inst, in1, in2, out = program[ip]
        registers = instruction_set[inst](in1, in2, out, registers)
        
        # Read IP back from register
        ip = registers[ip_register]

        # Increment IP
        ip += 1

    print(f"Program done, registers[0]={registers[0]}")

def factor(num):
    sum = 1
    print("Factor: 1")
    for x in range(2,num+1):
        if num % x == 0:
            print(f"Factor: {x}")
            sum += x
    print(f"Sum = {sum}")

if __name__ == "__main__":
    factor(947)
    print()
    factor(10551347)
    #part1()