from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_values: dict = {}
        for index, value in enumerate(nums):
            needed_value = target - value
            if needed_value in visited_values:
                return [visited_values[needed_value], index]
            visited_values[value] = index
        return []


nums = [2, 7, 11, 15]
target = 9
solution = Solution().twoSum(nums=nums, target=target)
print(solution)
