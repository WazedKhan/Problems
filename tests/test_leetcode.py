import random
import time
from typing import List

import pytest  # type: ignore

# large input imports
from ..inputs.simple_bank_system_2043 import large_input


@pytest.mark.parametrize("input_value, expected", [(19, True), (2, False)])
def test_happy_number_202(input_value, expected):
    from LeetCode.happy_number_202 import Solution

    solution = Solution().isHappy(input_value)
    assert solution == expected


# challenge


@pytest.mark.parametrize(
    "chalk, k, expected",
    [
        ([5, 1, 5], 22, 0),
        ([3, 4, 1, 2], 25, 1),
        ([1, 2, 3], 6, 0),
        ([7, 5, 3, 1], 20, 0),
    ],
)
def test_chalk_replacer(chalk, k, expected):
    from LeetCode.replace_the_chalk import Solution

    solution = Solution()
    assert solution.chalk_replacer_brute_force(chalk, k) == expected
    assert solution.chalkReplacer(chalk, k) == expected


@pytest.mark.parametrize("string_val, repeat, expected", [("leetcode", 2, 6), ("iiii", 1, 36)])
def test_sum_of_digit_1945(string_val, repeat, expected):
    from LeetCode.sum_of_string_digit_1945 import Solution

    solution = Solution().getLucky(string_val, repeat)
    assert solution == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3], 2, 1),  # target 2 should be inserted at index 1
        ([1, 3, 5, 6], 5, 2),  # target 5 exists at index 2
        ([1, 3, 5, 6], 2, 1),  # target 2 should be inserted at index 1
        ([1, 3, 5, 6], 7, 4),  # target 7 should be inserted at index 4
        ([1, 3, 5, 6], 0, 0),  # target 0 should be inserted at index 0
        ([1], 0, 0),  # target 0 should be inserted at index 0 in a single-element list
    ],
)
def test_search_insert(nums: List[int], target: int, expected: int):
    from LeetCode.search_insert_position import Solution

    solution = Solution()
    assert solution.search_insert(nums, target) == expected


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
    from ..LeetCode.longest_substring_no_repeat_03 import Solution

    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        (
            "this apple is sweet",
            "this apple is sour",
            ["sweet", "sour"],
        ),  # uncommon words are "sweet" and "sour"
        ("apple apple", "banana", ["banana"]),  # "banana" is the only uncommon word
        ("apple", "apple", []),  # no uncommon words, both sentences have "apple"
        (
            "the quick",
            "brown fox",
            ["the", "quick", "brown", "fox"],
        ),  # all words are uncommon
        ("", "fox", ["fox"]),  # one sentence is empty, uncommon is "fox"
        ("hello world", "", ["hello", "world"]),  # second sentence is empty
        ("a b c", "a b", ["c"]),  # "c" is the only uncommon word
    ],
)
def test_uncommon_from_sentences(s1: str, s2: str, expected: List[str]):
    from LeetCode.uncommon_words_in_two_sen_884 import Solution

    solution = Solution()
    assert sorted(solution.uncommonFromSentences(s1, s2)) == sorted(expected)


# Test suite for Solution class
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("babad", ["bab", "aba"]),  # The longest palindrome can be "bab" or "aba"
        ("cbbd", "bb"),  # The longest palindrome is "bb"
        ("a", "a"),  # Single character is a palindrome itself
        ("ac", "a"),  # Longest palindrome is either "a" or "c"
        ("", ""),  # Empty string should return an empty string
        ("racecar", "racecar"),  # Entire string is a palindrome
        ("noon", "noon"),  # Entire string is a palindrome
        ("abcdef", "a"),  # No palindrome longer than 1 character
    ],
)
def test_longest_palindrome(input_string, expected_output):
    from LeetCode.medium.longest_palindrome_05 import Solution

    solution = Solution()
    result = solution.longestPalindrome(input_string)

    if isinstance(expected_output, list):
        assert result in expected_output  # Handle cases with multiple valid palindromes
    else:
        assert result == expected_output


@pytest.mark.parametrize(
    "input_value, expected",
    [
        (121, True),  # Positive palindrome number
        (-121, False),  # Negative number, not a palindrome
        (10, False),  # Not a palindrome
        (0, True),  # Single-digit number, always a palindrome
        (12321, True),  # Odd-length palindrome
        (12345, False),  # Non-palindrome
        (1221, True),  # Even-length palindrome
        (-101, False),  # Negative number, not a palindrome
    ],
)
def test_is_palindrome(input_value, expected):
    from LeetCode.is_palindrome import Solution

    solution = Solution()
    assert solution.isPalindrome(input_value) == expected


@pytest.mark.parametrize(
    "roman, expected",
    [
        ("I", 1),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MMXXIV", 2024),
        ("MCMXCIV", 1994),
        ("III", 3),
        ("LVIII", 58),
        ("CCCLXXXIX", 389),
    ],
)
def test_roman_to_int(roman, expected):
    from LeetCode.roman_to_int import Solution

    solution = Solution()
    assert solution.romanToInt(roman) == expected


@pytest.mark.parametrize("gift, k, expected", [([25, 64, 9, 4, 100], 4, 29), ([1, 1, 1, 1], 4, 4)])
def test_gift_from_richest_pile(gift, k, expected):
    from LeetCode.gift_from_richest_pile import Solution

    solution = Solution()
    assert solution.pickGifts(gift, k) == expected


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
    from LeetCode.two_sum_01 import Solution

    # source: https://leetcode.com/problems/two-sum/

    solution = Solution()
    result = solution.twoSum(nums, target)

    # Ensure result is correct, accounting for possible order mismatch
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize(
    "words, expected",
    [
        (["a", "aba", "ababa", "aa"], 4),
        (["pa", "papa", "ma", "mama"], 2),
        (["abab", "ab"], 0),
        (["a", "abb"], 0),
    ],
)
def test_countPrefixSuffixPairs(words: List[str], expected: int):
    from LeetCode.count_prefix_suffix_3042 import Solution

    solution = Solution()
    result = solution.countPrefixSuffixPairs(words)
    assert result == expected, f"For input {words}, expected {expected} but got {result}"


@pytest.mark.parametrize(
    "x, expected",
    [
        (123, 321),  # Basic positive number
        (-123, -321),  # Basic negative number
        (120, 21),  # Ends with zero
        (0, 0),  # Single-digit zero
        (1, 1),  # Single positive digit
        (-1, -1),  # Single negative digit
        (1534236469, 0),  # Overflow positive case
        (-2147483648, 0),  # Overflow negative case
        (1000000003, 0),  # Close to overflow
    ],
)
def test_reverse_integer(x: int, expected: int):
    from LeetCode.medium.reverse_integer_7 import Solution

    solution = Solution()
    result = solution.reverse(x)
    assert result == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),  # Single pair
        ("()[]{}", True),  # Multiple valid pairs
        ("(]", False),  # Mismatched parentheses
        ("([)]", False),  # Nested but invalid
        ("{[]}", True),  # Properly nested
        ("", True),  # Empty string
        ("(", False),  # Single opening parenthesis
        (")", False),  # Single closing parenthesis
        ("(((((((((())))))))))", True),  # Deeply nested
        ("(((((((((()))", False),  # Deeply nested but incomplete
    ],
)
def test_is_valid_parentheses(s: str, expected: bool):
    from LeetCode.valid_parentheses_20 import Solution

    solution = Solution()
    result = solution.isValid(s)
    assert result == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ],
)
def test_length_of_last_word_58(s: str, expected: int):
    from LeetCode.easy.length_of_last_word_58 import Solution

    solution = Solution()
    assert solution.lengthOfLastWord(s) == expected


# @pytest.mark.parametrize(
#     "nums, val, expected_nums, expected_k",
#     [
#         ([3, 2, 2, 3], 3, [2, 2], 2),
#         ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4], 5),
#         ([1], 1, [], 0),
#         ([1, 2, 3], 4, [1, 2, 3], 3),
#         ([4, 4, 4, 4], 4, [], 0),
#         ([2, 2, 2, 3, 3], 3, [2, 2, 2], 3),
#     ],
# )
# def test_remove_element(nums, val, expected_nums, expected_k):
#     from LeetCode.easy.remove_element_027 import Solution

#     solution = Solution()
#     original = nums[:]
#     k = solution.remove_element_brute_force(nums, val)  # ignore

#     assert k == expected_k
#     assert sorted(nums[:k]) == sorted(
#         expected_nums
#     ), f"Failed for input: {original} with val: {val}"

#     k = solution.removeElement(nums, val)

#     assert k == expected_k
#     assert sorted(nums[:k]) == sorted(
#         expected_nums
#     ), f"Failed for input: {original} with val: {val}"


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 6], 5, 2),  # Target exists in the list
        ([1, 3, 5, 6], 2, 1),  # Target should be inserted at index 1
        ([1, 3, 5, 6], 7, 4),  # Target should be inserted at the end
        ([1, 3, 5, 6], 0, 0),  # Target should be inserted at the beginning
        ([1], 0, 0),  # Single element list
    ],
)
def test_search_insert_position(nums: List[int], target: int, expected: int):
    from LeetCode.easy.search_insert_position_035 import Solution

    solution = Solution()
    result = solution.searchInsert(nums, target)
    assert result == expected, f"Expected {expected}, but got {result} for nums: {nums} and target: {target}"

    result = solution.searchInsert_binary_search(nums, target)
    assert result == expected, f"Expected {expected}, but got {result} for nums: {nums} and target: {target}"


@pytest.mark.parametrize(
    "low, high, expected",
    [
        (1, 100, 9),  # Example: 11, 22, 33, ..., 99 (symmetric 2-digit numbers)
        (1200, 1230, 4),  # Example from the problem description
        (10, 99, 9),  # All 2-digit symmetric numbers
        (100, 999, 0),  # All 3-digit numbers: none are symmetric (odd length)
        (1000, 9999, 615),  # All 4-digit symmetric numbers
    ],
)
def test_count_symmetric_integers(low, high, expected):
    from LeetCode.easy.count_symmetric_integers_2843 import Solution

    sol = Solution()
    assert sol.countSymmetricIntegers(low, high) == expected, sol.countSymmetricIntegers(low, high)


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([1, 2, 3], [1, 2, 4]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([0], [1]),
        ([1, 0], [1, 1]),
        ([2, 9], [3, 0]),
        ([5, 5], [5, 6]),
        ([9, 8, 9], [9, 9, 0]),
    ],
)
def test_plus_one_66(digits: List[int], expected: List[int]):
    from LeetCode.easy.plus_one_66 import Solution

    solution = Solution()
    data = digits.copy()
    result = solution.plusOne(data)
    assert result == expected, f"For input {digits}, expected {expected} but got {result}"


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 11], 2, [11]),
        ([4, -2], 1, [4, -2]),
        ([7, 2, 4], 2, [7, 4]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
        ([5, 4, 3, 2, 1], 3, [5, 4, 3]),
        ([2, 2, 2, 2], 2, [2, 2, 2]),
        ([2, 1, 3], 3, [3]),
    ],
)
def test_maxSlidingWindow(nums, k, expected):
    from Goal.code.week_02 import Solution

    assert Solution().maxSlidingWindow(nums, k) == expected


@pytest.mark.parametrize(
    "s, expected",
    [("3902", True), ("34789", False)],
)
def test_hasSameDigits(s, expected):
    from LeetCode.easy.has_same_digits_3461 import Solution

    assert Solution().hasSameDigits(s) == expected


@pytest.mark.parametrize(
    "operations, inputs, expected",
    [
        (
            ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"],
            [
                [[10, 100, 20, 50, 30]],
                [3, 10],
                [5, 1, 20],
                [5, 20],
                [3, 4, 15],
                [10, 50],
            ],
            [None, True, True, True, False, False],
        ),
        (
            ["Bank", "deposit", "withdraw", "transfer"],
            [[[100, 50]], [1, 50], [2, 20], [1, 2, 100]],
            [None, True, True, True],
        ),
        (
            ["Bank", "withdraw", "deposit"],
            [[[30, 10, 50]], [1, 40], [2, 5]],
            [None, False, True],
        ),
        *large_input,
    ],
)
def test_bank_operations(operations, inputs, expected):
    """
    Execute a sequence of Bank operations and assert the observed results match the expected outcomes.
    
    Parameters:
        operations (List[str]): Ordered operation names; the first operation may be "Bank" to construct the Bank instance. Other valid names are "withdraw", "deposit", and "transfer".
        inputs (List[tuple]): Arguments for each corresponding operation in `operations`. For "Bank" provide the constructor arguments; for other operations provide the method arguments.
        expected (List[Optional[bool]]): Expected results for each operation in order (use `None` for the Bank constructor).
    
    The function raises an AssertionError if the actual results collected from performing the operations do not equal `expected`.
    """
    from LeetCode.medium.simple_bank_system_2043 import Bank

    bank = None
    results = []

    for op, inp in zip(operations, inputs):
        if op == "Bank":
            bank = Bank(*inp)
            results.append(None)
        elif op == "withdraw":
            results.append(bank.withdraw(*inp))
        elif op == "deposit":
            results.append(bank.deposit(*inp))
        elif op == "transfer":
            results.append(bank.transfer(*inp))

    assert results == expected


@pytest.mark.performance
def test_bank_performance():
    from LeetCode.medium.simple_bank_system_2043 import Bank

    n = 100_000
    bank = Bank([1000] * n)  # 100k accounts, each with balance 1000
    operations = 200_000

    start = time.perf_counter()

    for _ in range(operations):
        op_type = random.choice(["deposit", "withdraw", "transfer"])
        a1 = random.randint(1, n)
        money = random.randint(1, 100)

        if op_type == "deposit":
            bank.deposit(a1, money)
        elif op_type == "withdraw":
            bank.withdraw(a1, money)
        else:  # transfer
            a2 = random.randint(1, n)
            bank.transfer(a1, a2, money)

    end = time.perf_counter()
    print(f"\nTotal time for {operations} ops on {n} accounts: {end - start:.3f}s")