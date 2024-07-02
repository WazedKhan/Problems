from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        pointer_one = 0
        pointer_two = 0
        result = []

        while pointer_one < len(nums1) and pointer_two < len(nums2):

            if nums1[pointer_one] < nums2[pointer_two]:
                pointer_two += 1

            elif nums1[pointer_two] > nums2[pointer_one]:
                pointer_one += 1

            else:
                result.append(nums1[pointer_one])
                pointer_two += 1
                pointer_one += 1

        return result


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

solution = Solution().intersect(nums1, nums2)
print(solution)
