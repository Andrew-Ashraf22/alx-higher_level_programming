#!/usr/bin/python3
"""make a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square class that inherit rectangle"""

    def __init__(self, size):
        """makes a new square

        Args:
            size (int): The size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[Square] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
