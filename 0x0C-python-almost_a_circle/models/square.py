#!/usr/bin/python3
"""make a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """make a new square

        Args:
            size (int): The size
            x (int): The x coordinate
            y (int): The y coordinate
            id (int): The id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size"""
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Update the attr

        Args:
            *args (ints): the updated attr
            **kwargs (dict): the updated attr
        """
        if args:
            size = len(args)
            if size >= 1:
                self.id = args[0]
            if size >= 2:
                self.size = args[1]
            if size >= 3:
                self.x = args[2]
            if size >= 4:
                self.y = args[3]
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """return the dict reps of a square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """return the string reps of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
