#!/usr/bin/python3
"""make a function that writes to file the json reps of obj"""
import json


def save_to_json_file(my_obj, filename):
    """Write an obj to a file using json reps"""
    with open(filename, "w") as _file:
        json.dump(my_obj, _file)
