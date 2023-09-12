#!/usr/bin/python3
"""make a function that returns the obj from json file"""
import json


def load_from_json_file(filename):
    """create obj from json file"""
    with open(filename) as _file:
        return json.load(_file)
