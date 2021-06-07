from matrix import *
from eliminate_func import eliminate

def write(location,number):
    our_matrix[location[0]][location[1]][location[2]] = number
    possibilities[str([location[0], location[1], location[2]])] = []
    eliminate(location)