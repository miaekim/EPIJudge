from test_framework import generic_test

match = {
    "(": ")",
    "{": "}",
    "[": "]"
}
def is_well_formed(s: str) -> bool:
    stack = []
    for _s in s:
        if _s in match:
            stack.append(_s)
        elif not stack or match[stack.pop()] != _s:
            return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
