from matrix import *


def print_out(liste):
    for x in range(1, 10):
        for i in liste:
            if x % 3 == 0:
                print("  " + i + " " + " | ")
def show(the_matrix):
    print(the_matrix)
    column = 0
    square = 0
    liste = list()
    while column < 9 and square < 9:
        for line in range(0,3):
            liste.append(line)
        square += 1
        if square % 3 == 1:
            column += 1
            liste.clear()
            print_out(liste)
            square -= 1
        if column % 3 == 1:
            square += 1

