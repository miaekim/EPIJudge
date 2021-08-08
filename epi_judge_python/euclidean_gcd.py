from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return x + y
    if x == 1 or y == 1:
        return 1
    x, y = min(x, y), max(x, y)
    return gcd(x, y % x)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
