from typing import List

from test_framework import generic_test, test_utils


def permutations(nums: List[int]) -> List[List[int]]:
    def perm(nums: List[int], n: int) -> List[List[int]]:
        if n == 1:
            return [nums]
        
        result = []
        nums_set = set(nums)
        for num in nums:
            small_nums = nums_set - set([num])
            small_perms = perm(list(small_nums), n -1)
            for small_perm in small_perms: 
                result.append([num] + small_perm)
        return result
    return perm(nums, len(nums))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
