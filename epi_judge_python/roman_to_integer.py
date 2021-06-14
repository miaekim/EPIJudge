from test_framework import generic_test

T = {'': 0, 'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
E = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
def roman_to_integer(s: str) -> int:
    prev = s[0]
    result = T[prev]
    for _s in s[1:]:
        if prev + _s in E:
            result += (E[prev+_s] - T[prev])
            prev = ''
        else:
            prev = _s 
            result += T[prev]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
