#!/usr/bin/python3
"""make a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class that inherits from basegeometry"""

    def __init__(self, width, height):
        """make a new rectangle

        Args:
            width (int): The width
            height (int): The height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
