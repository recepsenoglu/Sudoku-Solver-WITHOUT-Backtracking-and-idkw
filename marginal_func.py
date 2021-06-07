from explore_funcs import *
from write import write

def marginal(location):
    square_Location = square_Explore(location, "location")
    vertical_Location = vertical_Explore(location, "location")
    horizontal_Location = horizontal_Explore(location, "location")

    for y in [square_Location,vertical_Location,horizontal_Location]:
        square = location[0]
        column = location[1]
        line = location[2]
        if our_matrix[square][column][line] == 0:
            current_block_possibles = possibilities[str([square, column, line])]
            for each in current_block_possibles:
                exist = False
                for x in y:
                    try:
                        if x != [square, column, line] and each in possibilities[str(x)]:
                            exist = True
                    except:
                        continue
                if not exist:
                    write(location, each)









