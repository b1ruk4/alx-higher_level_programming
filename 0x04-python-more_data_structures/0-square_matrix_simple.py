#!/usr/bin/python3
def square_matrix_matrix_simple(matrix=[]):
    for x in matrix:
        return [list(map(lambda i: i * i, x)), matrix]
