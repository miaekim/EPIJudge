from test_framework import generic_test


def snake_string(s: str) -> str:
    n = len(s)
    snake = ''
    if n <= 0:
        return snake
    for idx in range(1,n,4):
        snake += s[idx]
    for idx in range(0,n, 2):
        snake += s[idx]
    if n <= 3:
        return s[1]+s[0]+s[2:n]
    for idx in range(3,n, 4):
        snake += s[idx]
    return snake


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
