#!/usr/bin/python3
"""
This script defines a function to rotate a 2D matrix by 90 degrees clockwise.

Keyword arguments:
matrix -- The input 2D matrix to be rotated (list of lists)

Returns:
None. The function operates in-place and modifies the original matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given 2D matrix by 90 degrees clockwise.

    Keyword arguments:
    matrix -- The input 2D matrix to be rotated (list of lists)

    Returns:
    None. The function operates in-place and modifies the original matrix.
    """

    # 3 rotations needed for 90-degree clockwise rotation
    # for _ in range(3):
    # Reverse the matrix
    # for row in matrix:
    #     row.reverse()

    length = len(matrix) - 1
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            # Swap matrix elements at (i, j) and (j, i)
            matrix[i][j], matrix[length - 1 - j][i] = matrix[length - 1 - j][i], matrix[i][j]
