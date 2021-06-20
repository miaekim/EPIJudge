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
        else:
            if not stack:
                return False
            open = stack.pop()
            if match[open] != _s:
                return False
    if stack:
        return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
