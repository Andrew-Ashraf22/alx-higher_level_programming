#!/usr/bin/python3
"""make a function that checks if obj is inherting from class"""


def is_kind_of_class(obj, a_class):
    """see if the object is inherting from class

    Args:
        obj (any): The obj
        a_class (type): The class
    Returns:
        true if obj is type of class
    """
    return isinstance(obj, a_class)
