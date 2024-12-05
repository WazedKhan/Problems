import pytest
from typing import List


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
    from re_leet_code.search_insert_position import Solution

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
    from LeetCode.longest_palindrome_05 import Solution

    solution = Solution()
    result = solution.longestPalindrome(input_string)

    if isinstance(expected_output, list):
        assert result in expected_output  # Handle cases with multiple valid palindromes
    else:
        assert result == expected_output
