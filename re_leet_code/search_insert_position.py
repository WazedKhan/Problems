from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while right > left:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        if len(nums) - 1 >= left and nums[left] < target:
            return left + 1
        else:
            return left
