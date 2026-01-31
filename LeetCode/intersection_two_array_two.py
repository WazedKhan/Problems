from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        result = []
        for item in nums2:
            if counter[item] > 0:
                result.append(item)
                counter[item] -= 1
        return result


nums1 = [2, 2]
nums2 = [9, 4, 9, 2, 2]

solution = Solution().intersect(nums1, nums2)
print(solution)
