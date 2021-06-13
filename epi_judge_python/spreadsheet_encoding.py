from test_framework import generic_test
import functools
DIGITS = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def ss_decode_col_id(col: str) -> int:
    return functools.reduce(lambda x, y: x*26 + DIGITS.index(y), col, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
