from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_set = set(nums1)
        result = []
        for i in nums2:
            if i in hash_set:
                result.append(i)
                hash_set.remove(i)
        return result


nums1 = [2, 2]
nums2 = [9, 4, 9, 2, 2]

solution = Solution().intersect(nums1, nums2)
print(solution)
