#!/usr/bin/python3
"""make a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file

    Args:
        filename (file): The file
        search_string (str): string to search for
        new_string (str): string to add
    """
    with open(filename, 'r+') as _file:
        lines = _file.readlines()
        _file.seek(0)
        for line in lines:
            _file.write(line)
            if search_string in line:
                _file.write(new_string)
        _file.truncate()
