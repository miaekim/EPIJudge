from typing import List
import functools
from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    @functools.lru_cache(None)
    def max_recursive(start, end):
        nonlocal coins
        if start == end:
            return coins[start]

        return max(coins[start] + min_recursive(start + 1, end), coins[end] + min_recursive(start, end - 1))
    @functools.lru_cache(None)
    def min_recursive(start, end):
        nonlocal coins
        if start == end:
            return 0

        return min(max_recursive(start + 1, end), max_recursive(start, end - 1))
    
    return max_recursive(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
