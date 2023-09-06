#!/usr/bin/python3
"""
    makes a function that prints a square
    the given input is the size of the square
    the size must be an integer and greater
    than or equal to 0 otherwise raise exception
"""


def print_square(size):
    """
    prints the square of size

    Args:
        size (int): size of square

    Raises:
        TypeError: If size not an integer or less than 0
        ValueError: If size is less than 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
