#!/usr/bin/python3
"""make a function that appends text to file"""


def append_write(filename="", text=""):
    """Appends a string to the file

    Args:
        filename (file): the file
        text (str): The content
    Returns:
        The number of chars appended
    """
    with open(filename, "a", encoding="utf-8") as _file:
        return _file.write(text)
