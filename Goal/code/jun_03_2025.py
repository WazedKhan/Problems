# Solution Step: Braining Storming and Approach
# ------------------------------------------------
# Problem: Find the length of the longest substring without repeating characters.
#
# Braining Storming:
# - We need to scan the string and keep track of the longest substring with unique characters.
# - If we see a repeated character, we need to move the start of the substring forward.
# - We can use a sliding window approach with two pointers.
# - A set can help us track the unique characters in the current window.
#
# Approach (Pseudocode):
# 1. Initialize a set to store unique characters.
# 2. Initialize two pointers (left_pointer and right_pointer).
# 3. Iterate right_pointer over the string:
#    a. If s[right_pointer] is not in the set, add it.
#    b. If s[right_pointer] is in the set, remove s[left_pointer] from the set and move left_pointer forward.
#    c. Update the result with the maximum window size.
# 4. Return the result.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        char_set = set()
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[left_pointer])
                left_pointer += 1

            char_set.add(s[r])

            res = max(res, len(char_set))

        return res

s = "abcabcbb"
solution = Solution().lengthOfLongestSubstring(s)
print("Result: ", solution)