from matrix import *

def square_Explore(location, task="value"):
    return_list = []
    location_list = []
    square = location[0]

    for x in range(0, 3):
        for i in range(0, 3):
            return_list.append(our_matrix[square][x][i])
            location_list.append([square, x, i])

    if task == "location":
        return location_list
    return return_list

def horizontal_Explore(location, task="value"):
    return_list = []
    location_list = []
    column = location[1]
    square = location[0]
    square = square - square%3

    for x in range(0, 3):
        for i in range(0, 3):
            return_list.append(our_matrix[square][column][i])
            location_list.append([square, column, i])
        square += 1

    if task == "location":
        return location_list
    return return_list

def vertical_Explore(location, task="value"):
    return_list = []
    location_list = []
    line = location[2]
    square = location[0]
    square = square % 3

    for x in range(0, 3):
        for i in range(0, 3):
            return_list.append(our_matrix[square][i][line])
            location_list.append([square, i, line])
        square += 3

    if task == "location":
        return location_list
    return return_list

