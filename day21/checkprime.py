import math

def factor(num):
    sum = 1
    print("Factor: 1")
    for x in range(2,num+1):
        if num % x == 0:
            print(f"Factor: {x}")
            sum += x
    print(f"Sum = {sum}")

factor(4843319)
factor(65899)

