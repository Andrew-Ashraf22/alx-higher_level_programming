#!/usr/bin/python3
""" make a rectangle class"""


class Rectangle:
    """ a rectangle class"""
    def __init__(self, width=0, height=0):
        """make a new rectangle.

        Args:
            width (int): The width
            height (int): The height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rect"""
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter of rect"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Return the printable rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""

        strr = []
        for _ in range(self.height):
            strr += "#" * self.width + "\n"
        return strr.rstrip()
