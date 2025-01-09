import pytest


@pytest.mark.parametrize(
    "words, pref, expected",
    [
        (["pay","attention","practice","attend"], "at", 2),
        (["leetcode","win","loops","success"], "code", 0),
    ],
)
def test_count_given_prefix_2185(words, pref, expected):
    from LeetCode.easy.count_given_prefix_2185 import Solution

    solution = Solution()
    assert solution.prefixCount(words, pref) == expected