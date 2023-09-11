#!/usr/bin/python3
"""make a function that checks if obj inherit from class"""


def inherits_from(obj, a_class):
    """see if obj is inherting from class

    Args:
        obj (any): The obj
        a_class (type): The class
    Returns:
        true if obj is inheriting from class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
