from test_framework import generic_test

from collections import defaultdict
def can_form_palindrome(input: str) -> bool:
    #  number of odd count character should be same or less than zero
    dic = {}
    for s in input:
        if s and s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

    odd_cnt = 0
    for _, v in dic.items():
        if v % 2 == 1:
            odd_cnt += 1
        if odd_cnt > 1:
            return False
        
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
