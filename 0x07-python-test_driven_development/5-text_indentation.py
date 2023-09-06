#!/usr/bin/python3
"""
    make a function that prints the text
    followed by 2 new lines after
    every . ? or : it sees the given
    text  must be a string or a exception
    will be raised
"""


def text_indentation(text):
    """
    prints text with 2 new lines after . ? or :

    Args:
        text (str): the text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = text.splitlines()
    marks = [".", "?", ":"]
    for i in line:
        i = i.strip()
        for c in marks:
            i = i.replace(c, f"{c}\n\n")
        print(i, end="")
