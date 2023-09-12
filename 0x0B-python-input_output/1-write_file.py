#!/usr/bin/python3
"""make a function that writes to a file"""


def write_file(filename="", text=""):
    """
        writes to a a file the given text

        Args:
            filename (file): the file
            text (str): the content
        Returns:
            number of chars read
    """
    with open(filename, "w", encoding="utf-8") as _file:
        return _file.write(text)
