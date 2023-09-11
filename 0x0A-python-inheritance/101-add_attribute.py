#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, name, val):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object
        name (str): The name
        val (any): The value
    Raises:
        TypeError: If attr cant be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, val)
