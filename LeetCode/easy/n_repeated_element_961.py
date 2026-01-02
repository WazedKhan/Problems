# 961. N-Repeated Element in Size 2N Array
# Link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen_hash = {}  # this can solved with set as well

        for num in nums:
            if num in seen_hash:
                return num
            seen_hash[num] = 1
