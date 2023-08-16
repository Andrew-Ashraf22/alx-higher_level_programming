#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    lsum = 0
    for i in uniq:
        lsum += i
    return lsum
