from possibles_func import possible_values
from marginal_func import marginal
from results import *

count = 0
first_run = True
while True:
    isDone = True
    count += 1

    for square in range(0,9):
        for column in range(0,3):
            for line in range(0,3):
                if our_matrix[square][column][line] == 0:
                    isDone = False
                    location = [square, column, line]
                    if not first_run:
                        possible_values(location)
                        marginal(location)
                    else:
                        possible_values(location)
    first_run = False
    if isDone:
        for i in our_matrix:
            print(i)
        print("\n", count, "döngüde tamamlandı.")
        break