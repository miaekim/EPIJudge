from typing import List
import functools
from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    @functools.lru_cache(None)
    def max_recursive(start, end):
        nonlocal coins
        if start > end:
            return 0

        select_start = coins[start] + min(
            max_recursive(start + 2, end),
            max_recursive(start + 1, end -1)
        )
        select_end = coins[end] + min(
            max_recursive(start + 1, end - 1),
            max_recursive(start, end -2)
        )
        return max(select_start, select_end)
    return max_recursive(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
