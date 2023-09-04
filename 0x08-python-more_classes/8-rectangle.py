#!/usr/bin/python3
""" make a rectangle class"""


class Rectangle:
    """ a rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """make a new rectangle.

        Args:
            width (int): The width
            height (int): The height
        """
        Rectangle.number_of_instances += 1
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

        strr = ""
        for _ in range(self.height):
            strr += str(self.print_symbol) * self.width + "\n"
        return strr.rstrip()

    def __repr__(self):
        """Return string represinting rect"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints bye when a rectangle is begin deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
         """ returns the bigger rect

        Args:
            rect_1 (Rectangle): rect1
            rect_2 (Rectangle): rect2
        Raises:
            TypeError: If any of the rects are not a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
