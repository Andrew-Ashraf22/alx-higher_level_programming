#!/usr/bin/python3
"""make a class my list that inherit from list"""


class MyList(list):
    """sort list"""

    def print_sorted(self):
        """Print a list in order"""
        print(sorted(self))
