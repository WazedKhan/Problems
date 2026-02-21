from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = dict()
        for index, value in enumerate(nums):
            if target - value in bucket:
                return [bucket.get(target - value), index]

            bucket[value] = index
