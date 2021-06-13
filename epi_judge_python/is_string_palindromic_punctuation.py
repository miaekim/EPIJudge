from test_framework import generic_test

import re
def is_palindrome(s: str) -> bool:
    def to_plain(s: str) -> str:
        return re.sub(r'[^a-zA-Z0-9]', "", s.lower().strip())
    return to_plain(s) == to_plain(s[::-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
