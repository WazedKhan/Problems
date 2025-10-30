# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/?envType=daily-question&envId=2025-10-30
# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        for idx in range(1, len(target)):
            if target[idx] > target[idx - 1]:
                res += target[idx] - target[idx - 1]
        return res
