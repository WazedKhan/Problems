from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for index in range(len(nums)):
            left, right = index + 1, len(nums) - 1

            while left < right:
                three_sum = nums[index] + nums[left] + nums[right]
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
                if abs(three_sum - target) < abs(closest - target):
                    closest = three_sum
        return closest
