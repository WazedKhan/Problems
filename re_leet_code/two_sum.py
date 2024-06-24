from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, value in enumerate(nums):
            require_value = target - value
            if require_value in hash_map:
                return [index, hash_map[require_value]]
            else:
                hash_map[value] = index


nums = [2, 7, 11, 15]
target = 9
solution = Solution().twoSum(nums=nums, target=target)
print(solution)
