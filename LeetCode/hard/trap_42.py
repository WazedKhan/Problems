from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        h_len = len(height)
        max_left = [None] * h_len
        max_right = [None] * h_len

        max_left[0] = 0
        for i in range(1, h_len):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        max_right[-1] = 0
        for i in range(h_len - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        res = 0
        for i in range(h_len):
            trapped = min(max_left[i], max_right[i]) - height[i]
            res += max(0, trapped)
        return res
