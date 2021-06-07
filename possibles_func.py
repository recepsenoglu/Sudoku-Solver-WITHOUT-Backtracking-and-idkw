from eliminate_func import *
from write import write

def possible_values(location):
    explored = horizontal_Explore(location) + vertical_Explore(location) + square_Explore(location)
    possible_values = []
    for i in range(1, 10):
        if i not in explored:
            possible_values.append(i)

    if len(possible_values) == 1:
        write(location, possible_values[0])
    else:
        possibilities[str(location)] = possible_values

