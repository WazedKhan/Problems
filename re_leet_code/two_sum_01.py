from typing import List


# [2, 7, 11, 15], 9, [0, 1]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, value in enumerate(nums):
            require_value = target - value
            if require_value in hash_map:
                return [hash_map[require_value], index]
            hash_map[value] = index
