import pytest


@pytest.mark.parametrize(
    "num1,n,num2,m,expected",
    [
        # Test case 1: Normal merge
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        # Test case 2: num1 is empty except for zeroes
        ([0], 0, [1], 1, [1]),
        # Test case 3: num2 is empty, num1 should remain the same
        ([1], 1, [], 0, [1]),
        # Test case 4: All elements in num2 are smaller
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        # Test case 5: All elements in num2 are larger
        ([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3, [1, 2, 3, 4, 5, 6]),
        # Test case 6: num1 and num2 have same values
        ([2, 2, 3, 0, 0, 0], 3, [2, 2, 3], 3, [2, 2, 2, 2, 3, 3]),
        # Test case 7: One list contains all duplicates
        ([1, 1, 1, 0, 0, 0], 3, [1, 1, 1], 3, [1, 1, 1, 1, 1, 1]),
        # Test case 8: Large input where num2 fills all of num1
        ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),
        # Test case 9: Already merged
        ([1, 2, 3], 3, [], 0, [1, 2, 3]),
        # Test case 10: Mix of negative numbers
        ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3]),
    ],
)
def test_merge_sorted_array_88(num1, n, num2, m, expected):
    """
    LeetCode 88 - Merge Sorted Array

    The final sorted array should not be returned by the function,
    but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements
    denote the elements that should be merged, and the last n elements are set to 0
    and should be ignored. nums2 has a length of n.
    """
    from LeetCode.easy.merge_sorted_array_88 import Solution

    sol = Solution()

    sol.merge(num1, n, num2, m)
    assert num1 == expected


@pytest.mark.parametrize(
    "numRows, expected",
    [
        (1, [[1]]),
        (2, [[1], [1, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (
            6,
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
            ],
        ),
    ],
)
def test_generate(numRows, expected):
    from LeetCode.easy.pascals_triangle_118 import Solution

    solution = Solution()
    assert solution.generate(numRows) == expected


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),  # Prices only go down, no profit
        ([2, 7, 1, 5, 4], 5),  # Buy at 2, sell at 7
        ([1, 2], 1),  # Smallest input with a profit
        ([2, 1, 2, 1, 2], 1),  # Multiple valleys and peaks
        ([3, 3, 3, 3, 3], 0),  # All same prices
        ([1], 0),  # Only one day
    ],
)
def test_max_profit(prices, expected):
    from LeetCode.easy.best_time_buy_sell_stock_121 import Solution

    solution = Solution()
    assert solution.maxProfit(prices) == expected


# https://leetcode.com/problems/reverse-string/description/
# 344. Reverse String
@pytest.mark.parametrize(
    "s, expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["A", "b", "c", "d", "e"], ["e", "d", "c", "b", "A"]),
        (["a", "b", "c", "d", "e"], ["e", "d", "c", "b", "a"]),
        (["a", "b", "c", "d", "e", "f"], ["f", "e", "d", "c", "b", "a"]),
        (["a", "b", "c", "d", "e", "f", "g"], ["g", "f", "e", "d", "c", "b", "a"]),
        (
            ["a", "b", "c", "d", "e", "f", "g", "h"],
            ["h", "g", "f", "e", "d", "c", "b", "a"],
        ),
    ],
)
def test_reverse_string_344(s, expected):
    from LeetCode.easy.reverse_string_344 import Solution

    solution = Solution()
    solution.reverseString(s)  # should return None
    assert s == expected  # check in-place modification
