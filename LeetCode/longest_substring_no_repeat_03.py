# 3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_set = set()
        left_pointer = 0
        result = 0

        for i in range(len(s)):
            while s[i] in window_set:
                window_set.remove(s[left_pointer])
                left_pointer += 1
            window_set.add(s[i])
            result = max(result, i - left_pointer + 1)

        return result
