from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counter = 0
        num_len = len(nums)
        for i in range(num_len):
            for j in range(i, num_len):
                if nums[i] - i != nums[j] - j:
                    counter += 1

        return counter


nums = [1, 2, 3, 4, 5]
result = Solution().countBadPairs(nums)
print(f"Result: {result}")
