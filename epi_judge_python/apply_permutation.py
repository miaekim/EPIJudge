from typing import List

from test_framework import generic_test

# abcd
# 2103
# cba3

# A[2] = c
# A[1] = b

def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.
    for i in range(len(perm)):
        while i != perm[i]:
            p = perm[i]
            A[i] , A[p] = A[p], A[i]
            perm[i], perm[p] = perm[p], perm[i]


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
