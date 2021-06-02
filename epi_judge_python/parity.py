from test_framework import generic_test


def parity(x: int) -> int:
    _parity = x & 1
    while x:
        x = x >> 1
        _parity = (x ^ _parity) & 1
    return _parity


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
