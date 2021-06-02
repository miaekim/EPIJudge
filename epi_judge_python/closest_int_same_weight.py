from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    least_one = x & ~(x - 1)
    least_zero =  ~x & ~(~x - 1)
    big = max(least_one, least_zero)
    x ^= (big | big >> 1)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
