from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    n, m =  len(t), len(s)
    idx = 0

    while idx < n:
        i = 0
        while idx + i < n and i < m and t[idx + i] == s[i]:
            i += 1
        if i == m:
            return idx 
        idx += 1 
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
