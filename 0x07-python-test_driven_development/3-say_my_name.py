#!/usr/bin/python3
""" make a function called say my name that
    have 2 parameters first name and last name
    and then format a string my name is
    followed by first name and last name
    last name can be empty (optinal)
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints a string using first name and last name

    Args:
        first_name (str): The first name
        last_name (str): The last name

    Raises:
        TypeError: If any of the args are not strings

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = (first_name.strip() + " " + last_name.strip())
    print("My name is", name)
