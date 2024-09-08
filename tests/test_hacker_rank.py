import pytest
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
