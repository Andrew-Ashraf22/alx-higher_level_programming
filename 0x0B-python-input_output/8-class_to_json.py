#!/usr/bin/python3
"""make a function function that returns a dic of a simple
data struct"""


def class_to_json(obj):
    """Return the dict of a simple data struct"""
    json = {}
    attr = obj.__dict__
    for key, value in attr.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json[key] = value
    return json
