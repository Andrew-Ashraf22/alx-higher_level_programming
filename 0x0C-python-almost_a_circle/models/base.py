#!/usr/bin/python3
"""make a base class"""
import os
import json
import csv


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """make a base obj
            Args:
                id (int): the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON reps

        Args:
            list_dictionaries (list): A list of dics
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the json reps to a file

        Args:
            list_objs (list): A list of obj
        """
        name = cls.__name__ + ".json"
        j_list = []
        if list_objs is not None:
            j_list = [obj.to_dictionary() for obj in list_objs]
        with open(name, "w") as _file:
            _file.write(cls.to_json_string(j_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string reps

        Args:
            json_string (str): the json string reps
        Returns:
            python list reps of the json string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attrs

        Args:
            **dictionary (dict): a dict of attrs to set
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances

        Returns:
            a list of instantiated classes
        """
        name = cls.__name__ + ".json"
        try:
            with open(name, 'r') as _file:
                list_dicts = Base.from_json_string(_file.read())
                return [cls.create(**dicts) for dicts in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the csv reps to file

        Args:
            list_objs (list): A list of objs
        """
        name = cls.__name__ + ".csv"
        with open(name, 'w', newline='') as _file:
            writer = csv.writer(_file)
            if cls.__name__ == "Rectangle":
                names = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                names = ["id", "size", "x", "y"]
            writer.writerow(names)
            for k in list_objs:
                writer.writerow([getattr(k, i) for i in names])

    @classmethod
    def load_from_file_csv(cls):
        """returns list of classes from csv file

        Returns:
            list instanitaied classes
        """
        name = cls.__name__ + ".csv"
        try:
            with open(name, 'r') as _file:
                reader = csv.reader(_file)
                h = next(reader)
                insts = []
                for r in reader:
                    insts_dict = {k: int(val) for k, val in zip(h, r)}
                    inst = cls.create(**insts_dict)
                    insts.append(inst)
            return insts
        except IOError:
            return []
