#!/usr/bin/python3
"""making a square class"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        """make a square
        Args:
            size (int): size of square
        """
        self.__size = 0
        self.size = size

    def area(self):
        """Return the area of a square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """return size"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def __eq__(self, other):
        """the equal to op"""
        return self.area() == other.area()

    def __ne__(self, other):
        """the not equal to op"""
        return self.area() != other.area()

    def __le__(self, other):
        """the less than or equal op"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """ the greater than op"""
        return self.area() > other.area()

    def __ge__(self, other):
        """ the greater than or equal op"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """the less than op"""
        return self.area() < other.area()
