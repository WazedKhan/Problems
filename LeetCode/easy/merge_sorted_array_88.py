# https://leetcode.com/problems/merge-sorted-array/?envType=problem-list-v2&envId=array

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1 = nums1.sort()

    def merge_optimal(self, nums1: List[int], m: int, nums2: List[int], n: int):
        i = m - 1  # Last valid element in nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # End of nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements remain in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol = Solution().merge_optimal(nums1, m, nums2, n)
print(f"Num1: {nums1}")