#!/usr/bin/python3
"""2D matrix, rotate it 90 degrees clockwise"""


def transpose_matrix(matrix, n):
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    n = len(matrix)
    # print(n)

    # transpose matrix
    transpose_matrix(matrix, n)

    # reverse matrix
    reverse_matrix(matrix)

    return matrix
