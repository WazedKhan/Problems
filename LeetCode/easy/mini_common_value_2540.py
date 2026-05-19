from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2:List[int]) -> int:
        unique = set(nums1)
        result = -1
        nums2 = set(nums2)
        for i in unique:
            if i in nums2:
                if result == -1:
                    result = i
                else:
                    result = min(result, i)
        return result