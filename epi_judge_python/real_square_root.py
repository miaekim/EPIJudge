from test_framework import generic_test
import sys

EIPSLION = sys.float_info.epsilon * 10
def square_root(x: float) -> float:
    reverse = False
    if x < 1:
        reverse = True
        x = 1/x
    left, right = 0, x
    while left<right:
        mid = (left + right) / 2
        if mid ** 2 < x:
            if mid == left:
                return 1/mid if reverse else mid
            left = mid + EIPSLION
        elif mid ** 2 > x:
            if mid == right:
                return 1/mid if reverse else mid
            right = mid - EIPSLION
        else:
            if reverse:
                return 1/mid
            return mid

    return 1/left if reverse else left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
