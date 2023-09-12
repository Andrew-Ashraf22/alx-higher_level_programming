#!/usr/bin/python3
"""make a student class"""


class Student:
    """a student class"""

    def __init__(self, first_name, last_name, age):
        """make a new student

        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dict reps of a student

            Args:
            attrs (list): The attr
        """
        if attrs is None:
            return self.__dict__

        json = {}
        for key in attrs:
            if hasattr(self, key):
                json[key] = getattr(self, key)
        return json
