# source: https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_values = {}

        for index, value in enumerate(nums):
            # lets get the required value that need to to meet the target
            required_value = target - value
            # now lets check if required value is in our visited_value dict
            if required_value in visited_values:
                # if we found the required value in visited values then we can say we have our indexes
                # as required_value + value == target
                return [index, visited_values[required_value]]
            else:
                # if required value is not in visited values then we append it in visited values as we visiting it
                visited_values[value] = index
        # no target not value didn't match return empty index list
        return []
