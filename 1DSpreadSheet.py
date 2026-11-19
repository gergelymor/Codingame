import sys
import math

n = int(input())
cells = [[] for x in range(n)]
output = [None for x in range(n)]

def calculate(operand, arg1, arg2):
    if operand == "VALUE":
        return int(arg1)
    if operand == "ADD":
        return int(arg1)+int(arg2)
    if operand == "SUB":
        return int(arg1)-int(arg2)
    if operand == "MULT":
        return int(arg1)*int(arg2)

def referencer(arg):
    if arg == "_":
        return 0
    if str(arg).startswith("$"):
        referencedIndex = int(arg[1:])
        if output[referencedIndex] is None:
            operand, arg1, arg2 = cells[referencedIndex]
            output[referencedIndex] = calculate(operand, referencer(arg1), referencer(arg2))
        return output[referencedIndex]
    return int(arg)

for i in range(n):
    operation, arg1, arg2 = input().split()
    cells[i] = [operation, arg1, arg2]

for i in range(len(cells)):
    if output[i] is None:
        output[i] = calculate(cells[i][0], referencer(cells[i][1]), referencer(cells[i][2]))

for i in range(n):
    print(output[i])
