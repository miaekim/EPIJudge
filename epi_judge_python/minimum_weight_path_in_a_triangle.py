from typing import List
import functools
from test_framework import generic_test


# a
# b c
# d e f
# g h i j

# a + min(root_b, root_c)
def minimum_path_weight(triangle: List[List[int]]) -> int:
    if not triangle:
        return 0

    n = len(triangle)
    @functools.lru_cache(None)  
    def triange_traverse(row: int, col: int):
        nonlocal triangle
        
        if row == n - 1:
            return triangle[row][col]
        left = triange_traverse(row + 1, col)
        right = triange_traverse(row + 1, col + 1) if col <= row else float("inf")
        return  triangle[row][col] + min(left, right)

    return triange_traverse(0, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
