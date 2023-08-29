#!/usr/bin/python3
"""making a square class"""


class Square:
    """a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """make a square
        Args:
            size (int): size of square
        """
        self.__size = 0
        self.__position = (0, 0)
        self.size = size
        self.position = position

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

    def my_print(self):
        """ prints the square"""
        i = self.size
        for x in range(i):
            for y in range(i):
                print("#", end="")
            print()
        if i == 0:
            print()

    @property
    def position(self):
        """return the  position"""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and
        isinstance(i, int) for i in value and
        i < 0 for i in value and
        len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
