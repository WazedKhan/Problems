from typing import List

import pytest

from prep.practice.week_001 import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),  # Basic test case
        ([3, 2, 4], 6, [1, 2]),  # Another basic test
        ([3, 3], 6, [0, 1]),  # Same value twice
        ([1, 5, 7, 2], 9, [2, 3]),  # Random values
        ([1, 2, 3, 4, 5], 10, []),  # No match
        ([1, 3, 3, 4], 6, [1, 2]),  # Handles duplicate values
        ([0, 4, 3, 0], 0, [0, 3]),  # Handles zeros
    ],
)
def test_two_sum(nums: List[int], target: int, expected: List[int]):
    res = Solution().twoSum(nums, target)
    assert res == expected, f"expected {expected} but got {res}"


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),  # basic valid anagram
        ("rat", "car", False),  # different characters
        ("", "", True),  # empty strings
        ("a", "a", True),  # single character
        ("ab", "a", False),  # different lengths
        ("listen", "silent", True),  # common anagram
    ],
)
def test_valid_anagram(s, t, expected):
    result = Solution().isAnagram(s, t)
    assert result == expected, f"expected: {expected}, but got: {result}"
