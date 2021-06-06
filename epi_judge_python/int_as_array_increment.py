from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1
    i = len(A) - 1
    while i >= 0:
        carry, A[i] = (A[i] + carry) // 10, (A[i] + carry) % 10
        i = i - 1
    if carry > 0:
        A.insert(0, carry)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
