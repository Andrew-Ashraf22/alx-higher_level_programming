#!/usr/bin/python3
"""make a functuin that divide each numberin the matrix by the given divisor"""


def matrix_divided(matrix, div):
    """divide all number inside matrix by div

    Args:
        matrix (list): contains the numbers
        div (int/float): num to divide by
    Raises:
        TypeError: if the nums are not int or float
        TypeError: if matrix is not symmetric
        ZeroDivisonError: if we div by 0

    Returns:
        the matrix with divided numbers
    """
    new = []
    if not isinstance(matrix, list) or \
            not all(isinstance(lists, list) for lists in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    hold = len(matrix)
    if hold == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    hold = len(matrix[0])
    for i in matrix:
        holder = len(i)
        if holder != hold:
            raise TypeError(
                    "Each row of the matrix must have the same size")
    for row in matrix:
        if not all(isinstance(mem, (int, float)) for mem in row):
            raise TypeError("matrix must \
                    be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        holder = [round(j / div, 2) for j in i]
        new.append(holder)

    return new
