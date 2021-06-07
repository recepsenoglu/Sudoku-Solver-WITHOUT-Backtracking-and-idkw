from explore_funcs import *

def eliminate(location):
    locations = square_Explore(location, "location") + vertical_Explore(location, "location") + horizontal_Explore(location, "location")
    number = our_matrix[location[0]][location[1]][location[2]]

    for [square,column,line] in locations:
        try:
            values = possibilities[str([square, column, line])]
            if number in values:
               values.remove(number)
               possibilities[str([square, column, line])] = values
        except:
            continue
