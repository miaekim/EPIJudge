import collections
from test_framework import generic_test

from collections import Counter
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    magazine_dic = collections.Counter(magazine_text)
    letter_dic = collections.Counter(letter_text)
    
    for k, v in letter_dic.items():
        if k not in magazine_dic:
            return False
        if magazine_dic[k] < v:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
