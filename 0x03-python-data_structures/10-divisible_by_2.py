#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i in len(my_list):
        if my_list[i] % 2 == 0:
            new[i] = True
        else:
            new[i] = False
    return new
