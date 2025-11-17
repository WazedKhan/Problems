# https://leetcode.com/problems/reverse-string/description/
# 344. Reverse String
from typing import List


class Solution:
    def swap(self, x, y):
        return y, x

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while right > left:
            s[left], s[right] = self.swap(s[left], s[right])
            left += 1
            right -= 1
