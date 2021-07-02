from test_framework import generic_test


def square_root(k: int) -> int:
    digit = len(str(k))
    if k == 0:
        return 0

    left, right = 10 ** ((digit - 1) // 2) , 10 ** ((digit + 1) // 2)
    while left < right:
        mid = (left + right) // 2
        if mid ** 2 <= k:
            if (mid + 1) ** 2 > k:
                return mid
            left = mid + 1
        else:
            right = mid - 1
    return right


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
