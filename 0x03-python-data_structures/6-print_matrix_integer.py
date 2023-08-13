#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for i in lists:
            if i == (lists[len(lists) - 1]):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
        print()
