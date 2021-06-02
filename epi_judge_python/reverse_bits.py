from test_framework import generic_test

def reverse_bits(x: int) -> int:
    y = 0 
    i = 0
    while i < 64:
        y = y << 1 
        y |= x & 1
        x = x >> 1
        i = i + 1
    return y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
