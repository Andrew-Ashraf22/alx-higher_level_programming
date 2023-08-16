#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r = len(matrix)
    c = len(matrix[0])
    
    new = [[0 for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            new[i][j] = matrix[i][j] ** 2
    
    return new
