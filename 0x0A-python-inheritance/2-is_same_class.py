#!/usr/bin/python3
"""make a function to check if obj is instance of class"""


def is_same_class(obj, a_class):
    """ see if obj is instance of class
        Args:
            obj (any): The obj
            a_class (type): The class
        Returns:
            True if obj is instance of class false otherwise
    """
    return isinstance(obj, a_class) and type(obj) == a_class
