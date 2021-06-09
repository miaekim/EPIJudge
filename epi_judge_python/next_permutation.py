from typing import List

from test_framework import generic_test

def next_perm(perm:List[int]) -> List[int]:
    for idx in range(len(perm) - 1, 0 - 1, -1):
        if perm[idx] > perm[0]:
            return [perm[idx]] + sorted(perm[0:idx] + perm[idx +1:])

def next_permutation(perm: List[int]) -> List[int]:
    n = len(perm)
    if n <= 1:
        return []

    for idx in range(len(perm) - 2, 0 - 1, -1):
        if perm[idx] < perm[idx + 1]:
            return perm[0:idx] + next_perm(perm[idx:])
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
