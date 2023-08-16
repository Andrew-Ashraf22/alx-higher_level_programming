#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _keys = list(a_dictionary.keys())
    _keys.sort()
    for i in _keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
