import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

dot_character_order = 46

def compareDepth(element1, element2):
    if ord(str(element2)) == dot_character_order:
        return True
    else:
        return ord(str(element1)) < ord(str(element2))

w, h, t1, t2, t3 = [int(i) for i in input().split()]

first_picture = []
second_picture = []
third_picture = []

asteroids_rows_before = dict()
asteroids_rows_after = dict()
asteroids_cols_before = dict()
asteroids_cols_after = dict()

for i in range(h):
    first_picture_row, second_picture_row = input().split()
    first_picture.append(first_picture_row)
    second_picture.append(second_picture_row)

    for index in range(len(first_picture_row)):
        if first_picture_row[index] != ".":
            asteroids_rows_before[first_picture_row[index]] = index
            asteroids_cols_before[first_picture_row[index]] = i
    for index in range(len(second_picture_row)):
        if second_picture_row[index] != ".":
            asteroids_rows_after[second_picture_row[index]] = index
            asteroids_cols_after[second_picture_row[index]] = i

if first_picture == second_picture:
    third_picture = first_picture
else:
    third_picture = [["."] * w for _ in range(h)]
    for key in asteroids_rows_before:

        new_x_coord = asteroids_cols_after[key]+(asteroids_cols_after[key]-asteroids_cols_before[key])
        new_y_coord = asteroids_rows_after[key]+(asteroids_rows_after[key]-asteroids_rows_before[key])

        currentKey = third_picture[int(new_x_coord)][int(new_y_coord)]
        newKey = key
        if int(new_x_coord) >= 0 and int(new_y_coord) >= 0 and compareDepth(newKey, currentKey):
            third_picture[int(new_x_coord)][int(new_y_coord)] = key 

for row in range(len(third_picture)):
    print("".join([str(element) for element in third_picture[row]]))
