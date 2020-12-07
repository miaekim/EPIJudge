from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    if citations is None:
        return 0

    n = len(citations)

    if n == 0:
        return 0
        
    arr = sorted(citations)

    h = min(arr[-1], n)
    while h >= 1:
        res = arr[n - h]
        # print("h: ", h ,"res: ", res, "\n")
        if res >= h:
            return h
        else:
            h = h -1 

        
    return h


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
