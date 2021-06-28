from typing import List

from test_framework import generic_test
import heapq

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    if not A:
        return A
    n = len(A)
    if n <= 1:
        return A
    sorted_array = []
    start, end, increasing = 0, 0, True
    for i in range(0, n - 1):
        if increasing and A[i] > A[i + 1] or not increasing and A[i] < A[i + 1]:
            if increasing:
                sorted_array.append(A[start:i])
            else:
                if start == 0:
                    sorted_array.append(A[i-1::-1])
                else:
                    sorted_array.append(A[i-1:start-1:-1])
            increasing = not increasing
            start = i
    if start < n - 1:
        if increasing:
            sorted_array.append(A[start:])
        else:
            if start == 0:
                sorted_array.append(A[::-1])
            else:
                sorted_array.append(A[n-1:start-1:-1])

    # print(sorted_array)
    return list(heapq.merge(*sorted_array))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
