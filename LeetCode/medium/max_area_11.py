from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, res = 0, len(height) - 1, 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
