#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    dkeys = list(new.keys())
    for i in dkeys:
        new[i] = new[i] * 2
    return new
