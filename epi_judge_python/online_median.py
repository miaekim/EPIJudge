import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    min_heap, max_heap = [], []
    heapq.heapify(max_heap)
    heapq.heapify(max_heap)

    # min_heap : has large half
    # max_heap : has small half
    median, is_even = [], True
    for seq in sequence:
        # min_heap and max_heap same size or min_heap one more
        if max_heap and -seq > max_heap[0]:
            heapq.heappush(max_heap, -seq)
        else:
            heapq.heappush(min_heap, seq)
        is_even = not is_even
        
        if len(max_heap) + 1 < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if is_even:
            med = (min_heap[0] + max_heap[0] * -1) / 2
        else:
            med = min_heap[0]
        median.append(med)
        
    return median


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
