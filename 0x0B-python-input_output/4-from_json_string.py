#!/usr/bin/python3
"""make a function that return the python reps of json"""
import json


def from_json_string(my_str):
    """Return the python reps of a json"""
    return json.loads(my_str)
