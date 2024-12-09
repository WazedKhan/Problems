import pytest
from typing import List

from HackerRank.BreakingRheRecords import breaking_records


def test_breaking_records():
    # Test case 1: Sample input
    assert breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]) == [2, 4]

    # Test case 2: No record broken
    assert breaking_records([10, 10, 10, 10, 10]) == [0, 0]

    # Test case 3: Constantly increasing scores
    assert breaking_records([1, 2, 3, 4, 5]) == [4, 0]

    # Test case 4: Constantly decreasing scores
    assert breaking_records([5, 4, 3, 2, 1]) == [0, 4]

    # Test case 5: Single game
    assert breaking_records([100]) == [0, 0]

    # Test case 6: Two games where both records are broken
    assert breaking_records([10, 20]) == [1, 0]
    assert breaking_records([10, 5]) == [0, 1]


def test_time_in_words():
    from HackerRank.time_in_words import time_in_words

    # Test exact hour
    assert time_in_words(5, 0) == "five o' clock"
    assert time_in_words(12, 0) == "twelve o' clock"

    # Test quarter past
    assert time_in_words(5, 15) == "quarter past five"
    assert time_in_words(7, 15) == "quarter past seven"

    # Test quarter to
    assert time_in_words(5, 45) == "quarter to six"
    assert time_in_words(11, 45) == "quarter to twelve"

    # Test half past
    assert time_in_words(5, 30) == "half past five"
    assert time_in_words(12, 30) == "half past twelve"

    # Test minutes past
    assert time_in_words(5, 1) == "one minute past five"
    assert time_in_words(6, 10) == "ten minutes past six"

    # Test minutes to
    assert time_in_words(5, 59) == "one minute to six"
    assert time_in_words(11, 50) == "ten minutes to twelve"


# Test the Larry's Array function
@pytest.mark.parametrize(
    "array, expected_output",
    [
        ([3, 1, 2], "YES"),  # Example from problem description
        ([1, 3, 4, 2], "YES"),  # Example from problem description
        ([1, 2, 3, 5, 4], "NO"),  # Example from problem description
        ([1, 2, 3], "YES"),  # Already sorted
        ([4, 3, 2, 1], "NO"),  # Impossible to sort
        # ([2, 1, 3], "YES"),  # Rotations make it sortable
        ([1, 5, 4, 3, 2], "NO"),  # Odd number of inversions
        ([1], "YES"),  # Single element, no sorting needed
        ([2, 1], "NO"),  # Only two elements, can't perform rotations
    ],
)
def test_larrysArray(array: List[int], expected_output: str):
    from HackerRank.larrys_array import larrysArray

    assert larrysArray(array) == expected_output
