# LeetCode 14: Longest common prefix
# https://leetcode.com/problems/longest-common-prefix/
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]


        first_word: str = strs[0]
        res: str = ""
        for index in range(len(first_word)):
            for word in strs:
                if index == len(word) or first_word[index] != word[index]:
                    return res
            res += word[index]
        return res

