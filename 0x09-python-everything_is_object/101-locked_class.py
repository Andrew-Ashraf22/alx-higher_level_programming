#!/usr/bin/python3
"""make  a locked class"""


class LockedClass:
    """
    cant be instaniated unless for attr called first_name
    """
    __slots__ = ["first_name"]
