from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    if y < 0:
        x, y = 1/x, y * -1

    if y == 0:
        return 1

    multiplier = 1
    if y & 1 == 1:
        multiplier = x

    half = power(x, y >> 1)
    return half * half * multiplier


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
