from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, value in enumerate(nums):
            required_value = target - value
            if required_value in hash_map:
                return [hash_map[required_value], index]
            else:
                hash_map[value] = index


    def two_sum_brute(self, nums: List[int], target: int) -> List[int]:
        nums_size = len(nums)
        for position in range(nums_size):
            for index, value in enumerate(nums):
                if position < index:
                    current_sum = value + nums[position]
                    if current_sum == target:
                        return [position, index]


nums = [2, 7, 11, 15]
target = 9  # Output: [0, 1]
solution = Solution().two_sum_brute(nums, target)
print(f"Result Brute: {solution}")


nums = [2, 7, 11, 15]
target = 9  # Output: [0, 1]
solution = Solution().twoSum(nums, target)
print(f"Result Hash Map: {solution}")
