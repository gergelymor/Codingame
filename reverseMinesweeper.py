import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = int(input())
h = int(input())

fields = []
mine_coords = [] 

def isValidCoordinate(i, j, matrix):
    if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]):
        if matrix[i][j] != "x":
            return True
    return False

def increaseNeighbors(coordinate, matrix):
    neighbor_indices = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0,1),
        (1,-1),
        (1,0),
        (1,1)
    ]
    for i, j in neighbor_indices:
        x = coordinate[1]+i
        y = coordinate[0]+j
        if isValidCoordinate(x, y, matrix):
            if matrix[x][y] == ".":
                matrix[x][y] = "1"
            else:
                mine_count = int(matrix[x][y])
                matrix[x][y] = mine_count + 1
    return matrix



for i in range(h):
    line = input()
    if "x" in line:
        mines_in_line = [m.start() for m in re.finditer('x', line)]
        for mine in mines_in_line:
            mine_coords.append([mine, i])
    row = list(line)
    fields.append(row)

for i in range(len(mine_coords)):
    coordinate = mine_coords[i]
    increaseNeighbors(coordinate,fields)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(len(fields)):
    new_row = "".join([str(elem) for elem in fields[i]])
    print(new_row.replace("x", "."))
