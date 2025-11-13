# test file for LeetCode medium problems

import pytest

# 03: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=hash-table


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),  # longest substring is "abc" with length 3
        ("bbbbb", 1),  # longest substring is "b" with length 1
        ("pwwkew", 3),  # longest substring is "wke" with length 3
        ("", 0),  # empty string, longest substring is 0
        ("abcdef", 6),  # entire string is the longest substring, length 6
        ("aab", 2),  # longest substring is "ab", length 2
        ("dvdf", 3),  # longest substring is "vdf", length 3
        (" ", 1),  # single space character, length 1
    ],
)
def test_length_of_longest_substring(s: str, expected: int):
    from ..LeetCode.medium.longest_substring_without_repeat import Solution

    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected


# 05: Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=hash-table

# 07: Reverse Integer
# https://leetcode.com/problems/reverse-integer/?envType=problem-list-v2&envId=hash-table

# 08: String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/?envType=problem-list-v2&envId=hash-table

# 09: Palindrome Number
# https://leetcode.com/problems/palindrome-number/?envType=problem-list-v2&envId=hash-table

# 10: Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/?envType=problem-list-v2&envId=hash-table

# 11: Container With Most Water
# https://leetcode.com/problems/container-with-most-water/?envType=problem-list-v2&envId=hash-table

# 12: Integer to Roman
# https://leetcode.com/problems/integer-to-roman/?envType=problem-list-v2&envId=hash-table
