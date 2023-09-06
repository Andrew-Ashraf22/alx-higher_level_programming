#!/usr/bin/python3
""" make a function that add 2 integers or floats
    the function will check if the number gived
    are not floats or integers and raise an error
    if any of the number is float its converted to int
"""


def add_integer(a, b=98):
    """ add 2 integers or floats
    Raises:
        TypeError: If  a or b is not an integer or a float"""
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
