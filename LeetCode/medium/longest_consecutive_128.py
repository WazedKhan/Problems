from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:
                current = 0
                while (num + current) in num_set:
                    current += 1
                longest = max(longest, current)

        return longest
