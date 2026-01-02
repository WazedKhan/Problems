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


@pytest.mark.parametrize(
    "s, expected",
    [
        ("dfa12321afd", 2),  # normal case → digits: {1,2,3}
        ("abc1111", -1),  # only one unique digit
        ("abc", -1),  # no digits
        ("ck077", 0),  # digits: {0,7} → second highest = 0
        ("sjhtz8344", 4),  # digits: {3,4,8} → second = 4
        ("aaaa9998", 8),  # digits: {8,9} → second = 8
        ("0", -1),  # only one digit
        ("9876543210", 8),  # all digits → second = 8
        ("2abc3d4e5f6", 5),  # scattered digits → second = 5
        ("99", -1),  # duplicates only
        ("a1b2c3d4e5", 4),  # increasing digits
        ("5a5b5c5d5", -1),  # one unique digit seen multiple times
        ("z1y0x9w", 1),  # digits: {0,1,9} → second = 1
    ],
)
def test_second_highest(s, expected):
    from LeetCode.easy.second_largest_digit_in_string_1796 import Solution

    solution = Solution()
    assert solution.secondHighest(s) == expected


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["flower", "flow", "flight"], "fl"),  # common prefix is "fl"
        (["dog", "racecar", "car"], ""),  # no common prefix
        (["a", "a", "a"], "a"),  # all same single character
        (["ab", "a"], "a"),  # common prefix is "a"
        ([], ""),  # empty list
        (["single"], "single"),  # single string in the list
        (["prefix", "pre", "pretest"], "pre"),  # common prefix is "pre"
    ],
)
def test_longest_common_prefix(strs, expected):
    from LeetCode.easy.longest_common_prefix_14 import Solution

    solution = Solution()
    assert solution.longestCommonPrefix(strs) == expected

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02
# 961. N-Repeated Element in Size 2N Array


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 3], 3),  # Example 1
        ([2, 1, 2, 5, 3, 2], 2),  # Example 2
        ([5, 1, 5, 2, 5, 3, 5, 4], 5),  # Example 3
        ([1, 1], 1),  # Minimum size array
        ([4, 4, 4, 4], 4),  # All elements are the same
        ([1, 2, 3, 4, 5, 5], 5),  # Repeated element at the end
        ([6, 7, 8, 9, 6, 6], 6),  # Repeated element at the beginning
        ([10, 20, 10, 30, 10, 40], 10),  # Non-consecutive repeats
        ([100, 200, 300, 100, 400, 100], 100),  # Larger numbers
        ([0, 0, 0, 0], 0),  # All zeros
    ],
)
def test_repeated_n_times(nums, expected):
    from LeetCode.easy.n_repeated_element_961 import Solution

    solution = Solution()
    assert solution.repeatedNTimes(nums) == expected
