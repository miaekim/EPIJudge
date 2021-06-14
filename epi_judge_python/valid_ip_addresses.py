from typing import List

from test_framework import generic_test

def get_valid_ip_address(s: str) -> List[str]:
    def is_valid_part(s: str):
        return len(s) == 1 or (s[0] != '0' and int(s) < 256)
        
    def get_partial_ip_address(prefix: str, s: str, dot_count: int):
        if dot_count == 1:
            if is_valid_part(s):
                return [f"{prefix}.{s}"]
            else:
                return []

        ip_addresses = []
        n = len(s)
        dot_idx = 1
        while dot_idx < n:
            if is_valid_part(s[:dot_idx]):
                new_prefix = f"{prefix}.{s[:dot_idx]}" if prefix != "" else f"{s[:dot_idx]}"
                ip_addresses += get_partial_ip_address(new_prefix, s[dot_idx:], dot_count - 1)
                dot_idx += 1
            else:
                break
        return ip_addresses

    return get_partial_ip_address("", s, 4)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
