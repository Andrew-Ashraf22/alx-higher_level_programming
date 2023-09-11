#!/usr/bin/python3
"""make a MyInt class"""


class MyInt(int):
    """just like the int class but == and != revetred"""

    def __eq__(self, other):
        """== but reverted"""
        return super().__ne__(other)

    def __ne__(self, other):
        """!= but reverted"""
        return super().__eq__(other)
