from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], target: int) -> bool:
    n = len(A)
    if n == 0:
        return False
    m = len(A[0])
    if m == 0:
        return False

    x, y = 0, m - 1
    while x < n and y >= 0:
        if A[x][y] < target:
            x += 1
        elif A[x][y] > target:
            y -= 1
        else:
            return True
    return False



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
