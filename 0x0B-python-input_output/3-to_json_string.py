#!/usr/bin/python3
"""make a function that returns the json reps of an object"""
import json


def to_json_string(my_obj):
    """Return the JSON reps of a object"""
    return json.dumps(my_obj)
