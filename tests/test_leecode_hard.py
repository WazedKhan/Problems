import pytest


@pytest.mark.parametrize(
    "height, expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
        ([1], 0),
        ([1, 2], 0),
        ([1, 2, 3, 4, 5], 0),  # increasing
        ([5, 4, 3, 2, 1], 0),  # decreasing
        ([3, 3, 3, 3], 0),  # flat
        ([3, 0, 3], 3),
        ([5, 0, 5], 5),
        ([2, 0, 2], 2),
    ],
)
def test_trap(height, expected):
    from LeetCode.hard.trap_42 import Solution

    assert Solution().trap(height) == expected
