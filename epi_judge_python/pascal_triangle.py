from typing import List

from test_framework import generic_test


pascal = [[1]]
def generate_pascal_triangle(n: int) -> List[List[int]]:
    
    if len(pascal) >= n:
        return pascal[:n]

    for row in range(len(pascal), n):
        prev = pascal[row - 1]
        curr = [1]
        for col in range(n - 2):
            curr.append(prev[col] + prev[col + 1])
        curr.append(1)
        pascal.append(curr)
    return pascal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
