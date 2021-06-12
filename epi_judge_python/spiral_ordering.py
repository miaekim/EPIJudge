from typing import List

from test_framework import generic_test
from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    n = len(square_matrix)

    ordering = []
    direction = Direction.EAST
    i, j = 0, -1
    ordering_size = 0
    iteration = 1
    while ordering_size < n*n:
        if direction == Direction.EAST:
            if j < n - iteration:
                j += 1
            else:
                direction = Direction.SOUTH
                continue
        elif direction == Direction.SOUTH:
            if i < n - iteration:
                i += 1
            else:
                direction = Direction.WEST
                continue
        elif direction == Direction.WEST:
            if j > iteration - 1:
                j -= 1
            else:
                iteration += 1
                direction = Direction.NORTH
                continue
        elif direction == Direction.NORTH:
            if i > iteration - 1:
                i -= 1
            else:
                direction = Direction.EAST
                continue
        ordering.append(square_matrix[i][j])
        ordering_size += 1

    return ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
