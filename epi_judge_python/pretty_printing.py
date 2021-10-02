import functools
from typing import List
from test_framework import generic_test


def minimum_messiness(words: List[str], line_length: int) -> int:
    # greedy, last line
    n = len(words)
    word_lens = [len(w) for w in words]
    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            selected_length = sum(word_lens[i : j + 1]) + (j - i)
            if selected_length > line_length:
                cost[i][j] = float("inf")
            else:
                cost[i][j] = (line_length - selected_length) ** 2

    @functools.lru_cache(None)
    def line_messiness(start: int):
        nonlocal cost
        nonlocal line_length
        if start >= n:
            return 0

        return min([
           (cost[start][k] + line_messiness(k + 1)) for k in range(start, n)
        ])
    return line_messiness(0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
