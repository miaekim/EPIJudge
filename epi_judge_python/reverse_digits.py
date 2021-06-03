from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.

    if x < 0:
        x = str(x * -1)
        sign = "-"
    else:
        x = str(x)
        sign = ""
    
    return int(sign + x[::-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
