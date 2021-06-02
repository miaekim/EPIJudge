from test_framework import generic_test


def swap_bits(x, i, j):
    ii = (x >> i) & 1
    jj = (x >> j) & 1

    if ii ^ jj:
        if ii == 1:
            x = x | 2**j
            x = x & ~2**i
        else:
            x = x | 2**i
            x = x & ~2**j

    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
