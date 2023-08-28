#!/usr/bin/python3
def safe_print_integer(value):
    try:
        i = int(value)
        print("{:d}".format(i))
        print()
        return True
    except (TypeError, ValueError):
        return False
