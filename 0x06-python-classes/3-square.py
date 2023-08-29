#!/usr/bin/python3
"""making a square class"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        """make a square
        Args:
            size (int): size of square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Return the area of a square"""
        return (self.__size * self.__size)
