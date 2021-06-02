from test_framework import generic_test


def divide(x: int, y: int) -> int:
    if x > y:
        i = 1
        quotient = 0
        while True:
            if (y << i) > x:
                x = x - (y << (i-1))
                quotient = 1 << (i - 1)
                break
            i = i + 1

        return divide(x, y) + quotient
    elif x == y:
        return 1
    else:
        return 0



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
