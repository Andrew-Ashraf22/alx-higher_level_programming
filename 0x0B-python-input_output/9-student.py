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

    def to_json(self):
        """Get a dict reps of a student"""
        return self.__dict__
