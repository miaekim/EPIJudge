from typing import List

from test_framework import generic_test, test_utils
import heapq

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    candidate = [(-A[0], 0)]
    heapq.heapify(candidate)
    n = len(A)
    largest = []
    largest_size = 0
    while largest_size < k:
        data, idx = heapq.heappop(candidate)
        largest.append(-data)
        largest_size += 1
        first = 2*idx + 1
        second = 2*idx + 2
        if first < n:
            heapq.heappush(candidate, (-A[first], first))
        if second < n:
            heapq.heappush(candidate, (-A[second], second))
        
    return largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
