#!/usr/bin/python3
"Pascal's trianle function"


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    :param n: The number of rows to generate in Pascal's triangle.
    :type n: int
    :return: A list containing Pascal's triangle up to the nth row.
    :rtype: list[list[int]]
    """

    # Base cases
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    # Initialize Pascal's triangle with the first two rows
    pascal_list = [[1], [1, 1]]

    # Generate the remaining rows
    while len(pascal_list) < n:
        prev_list = pascal_list[-1]
        prev_list_len = len(prev_list)

        # Use list comprehension for the current row
        current_list = [1] + \
            [
                prev_list[i] + prev_list[i + 1]
                for i in range(prev_list_len - 1)
            ] + [1]

        # Append the current row to the triangle
        pascal_list.append(current_list)

    return pascal_list
