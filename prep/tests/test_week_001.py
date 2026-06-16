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


# @pytest.mark.parametrize(
#     "prices, expected",
#     [
#         ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
#         ([7, 6, 4, 3, 1], 0),  # Prices only go down, no profit
#         ([2, 7, 1, 5, 4], 5),  # Buy at 2, sell at 7
#         ([1, 2], 1),  # Smallest input with a profit
#         ([2, 1, 2, 1, 2], 1),  # Multiple valleys and peaks
#         ([3, 3, 3, 3, 3], 0),  # All same prices
#         ([1], 0),  # Only one day
#     ],
# )
# def test_max_profit(prices, expected):
#     assert Solution().maxProfit(prices) == expected


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
    result = Solution().productExceptSelf(nums)

    assert result == expected, f"Expected {expected}, but got {result}"
