from test_framework import generic_test

def reverse_int(x: int) -> int:
    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10
    return result

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    return x == reverse_int(x)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
