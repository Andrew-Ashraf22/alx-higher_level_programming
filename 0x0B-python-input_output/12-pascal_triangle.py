#!/usr/bin/python3
"""make a psacal triangle"""


def pascal_triangle(n):
    """return the pascal triangle of n"""
    if n <= 0:
        return []

    tri = []
    for i in range(n):
        r = [1] * (i + 1)
        if i >= 2:
            pr = tri[i - 1]
            for j in range(1, i):
                r[j] = pr[j - 1] + pr[j]
        tri.append(r)

    return tri
