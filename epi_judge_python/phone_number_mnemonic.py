from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    number_to_chars = {
        '0': ['0'],
        '1': ['1'],
        '2': ['A','B','C'],
        '3': ['D','E','F'],
        '4': ['G','H','I'],
        '5': ['J','K','L'],
        '6': ['M','N','O'],
        '7': ['P','Q','R', 'S'],
        '8': ['T','U','V'],
        '9': ['W','X','Y','Z']
    }
    temps = []
    results: List[str] = [""]

    for number in phone_number: # n
        chars = number_to_chars[number]
        for result in results: # n
            for char in chars: # 4
                temps.append(result + char)
        results = temps
        temps =[]

    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
