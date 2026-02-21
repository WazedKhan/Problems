from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        This function takes a list of integers and returns the missing number in the list.

        The function works by calculating the expected sum of the list (n*(n+1)//2) and
        subtracting the actual sum of the list from the expected sum.

        :param nums: List[int] - A list of integers.
        :return: int - The missing number in the list.
        """
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)
