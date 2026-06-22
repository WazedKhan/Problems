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


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),  # basic case
        ([0, 1, 2, 3], [6, 0, 0, 0]),  # one zero
        ([0, 0, 2, 3], [0, 0, 0, 0]),  # two zeros
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),  # LeetCode example
        ([2, 3], [3, 2]),  # minimum valid length
        ([1, 1, 1, 1], [1, 1, 1, 1]),  # all ones
        ([-1, -2, -3, -4], [-24, -12, -8, -6]),  # all negatives
        ([5, 2, 1], [2, 5, 10]),  # small array
    ],
)
def test_product_except_self(nums, expected):
    from LeetCode.medium.product_except_self_238 import Solution

    result = Solution().productExceptSelf(nums)

    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (
            [""],
            [[""]],
        ),
        (
            ["a"],
            [["a"]],
        ),
        (
            ["abc", "bca", "cab"],
            [["abc", "bca", "cab"]],
        ),
        (
            ["abc", "def", "ghi"],
            [["abc"], ["def"], ["ghi"]],
        ),
    ],
)
def test_group_anagram(strs, expected):
    from LeetCode.medium.group_anagrams_49 import Solution

    result = Solution().groupAnagrams(strs)

    # Order of groups and order within groups do not matter
    normalized_result = sorted([sorted(group) for group in result])
    normalized_expected = sorted([sorted(group) for group in expected])

    assert normalized_result == normalized_expected


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9], 8, [4, 5]),
        ([-5, -3, 0, 2, 4, 8], 5, [2, 6]),
        ([1, 3, 5, 7, 9], 16, [4, 5]),
    ],
)
def test_two_sum(numbers, target, expected):
    from LeetCode.medium.two_sum_two_167 import Solution

    result = Solution().twoSum(numbers, target)

    assert result == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        (
            [-1, 0, 1, 2, -1, -4],
            [[-1, -1, 2], [-1, 0, 1]],
        ),
        (
            [0, 1, 1],
            [],
        ),
        (
            [0, 0, 0],
            [[0, 0, 0]],
        ),
        (
            [0, 0, 0, 0],
            [[0, 0, 0]],
        ),
        (
            [-2, 0, 0, 2, 2],
            [[-2, 0, 2]],
        ),
        (
            [1, 2, -2, -1],
            [],
        ),
        (
            [-1, -1, -1, 2, 2],
            [[-1, -1, 2]],
        ),
        (
            [1, 2, 0, 1, 0, 0, 0, 0],
            [[0, 0, 0]],
        ),
        (
            [-100, -70, -60, 110, 120, 130, 160],
            [[-100, -60, 160], [-70, -60, 130]],
        ),
    ],
)
def test_three_sum(nums, expected):
    from LeetCode.medium.three_sum_15 import Solution

    result = Solution().threeSum(nums)

    normalized_result = sorted([sorted(triplet) for triplet in result])
    normalized_expected = sorted([sorted(triplet) for triplet in expected])

    assert normalized_result == normalized_expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([0, 0, 0], 0, 0),
        ([1, 1, 1, 0], -100, 2),
        ([1, 1, -1, -1, 3], -1, -1),
        ([-3, -2, -5, 3, -4], -1, -2),
        ([4, 0, 5, -5, 3, 3, 0, -4, -5], -2, -2),
    ],
)
def test_three_sum_closest(nums, target, expected):
    from LeetCode.medium.three_sum_closest_16 import Solution

    result = Solution().threeSumClosest(nums, target)
    assert result == expected, f"expected: {expected} but got: {result}"


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
