#!/usr/bin/python3
"""make a function that reads from file and print it to stdout"""


def read_file(filename=""):
    """
        reads content of filename and prints them

        Args:
            filename (file): the file
    """
    with open(filename, "r", encoding="utf-8") as _file:
        print(_file.read(), end="")
