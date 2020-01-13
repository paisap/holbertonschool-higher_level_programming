#!/usr/bin/python3
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
    """


def matrix_divided(matrix, div):
    """Example of add on the matrix_divided method.
            this functions divided a matrix with div
        """
    the_len = 0
    aux = 0
    new_matrix = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, (list)):
        raise TypeError(msg)
    new_matrix = matrix.copy()
    the_len = len(matrix[0])
    if the_len == 0:
        raise TypeError(msg)
    for i in matrix:
        if not isinstance(i, (list)):
            raise TypeError(msg)
        if the_len != len(matrix[aux]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(msg)
        aux += 1
    new_matrix = [[round(i / div, 2) for i in j]for j in matrix]
    return new_matrix
