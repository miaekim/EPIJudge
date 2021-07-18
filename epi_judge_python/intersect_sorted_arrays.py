from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    idx_A, idx_B = 0, 0
    len_A, len_B = len(A), len(B)

    result = []
    while idx_A < len_A and idx_B < len_B:
        if A[idx_A] < B[idx_B]:
            idx_A += 1
        elif B[idx_B] < A[idx_A]:
            idx_B += 1
        else:
            value = A[idx_A]
            result.append(value)
            while idx_A < len_A and A[idx_A] == value:
                idx_A += 1
            while idx_B < len_B and B[idx_B] == value:
                idx_B += 1
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
