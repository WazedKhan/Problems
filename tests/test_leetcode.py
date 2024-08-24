import pytest


@pytest.mark.parametrize("input_value, expected", [(19, True), (2, False)])
def test_happy_number_202(input_value, expected):
    from LeetCode.happy_number_202 import Solution

    solution = Solution().isHappy(input_value)
    assert solution == expected
