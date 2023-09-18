#!/usr/bin/python3
"""make a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width
            height (int): The height
            x (int): The x coordinate
            y (int): The y coordinate
            id (int): The id
        Raises:
            TypeError: If  width or height or x or y is not int
            ValueError: If width or height or x or y <= 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, wid):
        if type(wid) != int:
            raise TypeError("width must be an integer")
        if wid <= 0:
            raise ValueError("width must be > 0")
        self.__width = wid

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, hei):
        if type(hei) != int:
            raise TypeError("height must be an integer")
        if hei <= 0:
            raise ValueError("height must be > 0")
        self.__height = hei

    @property
    def x(self):
        """get the x"""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """get the y"""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Return the area"""
        return self.width * self.height

    def display(self):
        """print a rectangle using #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for _ in range(self.y):
            print("")

        for i in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def __str__(self):
        """return a string reps of the rect"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """return the dict reps of a rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "width": self.width,
            "height": self.height
        }

    def update(self, *args, **kwargs):
        """update the attr

            Args:
                *args (int): the new values to update
                **kwargs (dict): new values to update
        """
        if args:
            siz = len(args)
            if siz >= 1:
                self.id = args[0]
            if siz >= 2:
                self.width = args[1]
            if siz >= 3:
                self.height = args[2]
            if siz >= 4:
                self.x = args[3]
            if siz >= 5:
                self.y = args[4]
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
