#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    ro = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    rsum = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = ro.get(char, 0)

        if value >= prev_value:
            rsum += value
        else:
            rsum -= value

        prev_value = value

    return rsum
