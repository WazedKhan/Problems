# 1752. Check if Array Is Sorted and Rotated
from typing import List

class Solution:
    def find_break_point(self, nums: List[int], start=0) -> bool:
        result = 0
        if nums[-1] > nums[0]:
            result += 1

        for index in range(len(nums)-1):
            if nums[index + 1] < nums[index]:
                result += 1

        return result

    def check(self, nums: List[int]) -> bool:
        break_point = self.find_break_point(nums)
        return break_point <= 1
