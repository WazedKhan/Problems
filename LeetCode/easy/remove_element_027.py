# https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array

from typing import List


class Solution:
    def remove_element_brute_force(self, nums: List[int], val: int) -> int:
        k = 0
        duplicate_counts = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
                duplicate_counts += 1
        k = len(nums) - duplicate_counts
        
        for i in range(duplicate_counts):
            nums.remove(None)
        
        return k, nums
        
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k, nums

nums = [3,2,2,3]
val = 3
k, nums = Solution().removeElement(nums, val)
print(k, nums)