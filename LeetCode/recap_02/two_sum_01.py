from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in hash_map:
                return [hash_map[complement], index]
            hash_map[value] = index


# nums = [2,7,11,15], target = 9
