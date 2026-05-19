from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2:List[int]) -> int:
        point_one = 0
        point_two = 0

        while len(nums1) > point_one and len(nums2) > point_two:
            if nums2[point_two] == nums1[point_one]:
                return nums1[point_one]
            elif nums1[point_one] < nums2[point_two]:
                point_one += 1
            else:
                point_two += 1

        return -1
