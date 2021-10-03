import functools
from typing import List
import functools
from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    n = len(A)
    longest_length = 1
    @functools.lru_cache(None)
    def subseq_length_at(end: int) -> int:
        nonlocal A
        nonlocal longest_length
        if end == 0:
            subseq_length = 1
        else:
            subseq_length = max([
                (subseq_length_at(idx) + 1) if A[end] >= A[idx] else 1 for idx in range(end)
            ])
        longest_length = max(longest_length, subseq_length)
        return subseq_length

    for idx in range(n):
        subseq_length_at(idx)
    return longest_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
