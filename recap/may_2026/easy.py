from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Understanding Problem:
        - there will be exactly one pair of valid indices exits
        - same element of the array/list cant be used twice
        - indices/result can be return in any order

        Brute Force (O(n²)):
        - For each element, check every other element to see if they sum to target.
        - Works, but slow for large inputs.

        Optimized Approach using a Hash Map (O(n)):
        - For each number, calculate its complement: complement = target - value.
          e.g. target=9, value=2 → complement=7 (2 needs a partner of 7).
        - Store each number's complement in a hash map: { complement: index }.
        - For every new number, check if it exists as a complement in the hash map.
          If yes, a previous number was waiting for exactly this value — return both indices.
        - This way we find the answer in a single pass.
        """

        # Tracks complements we're waiting for: { complement_value: index_of_number_that_needs_it }
        hash_map = {}

        for index, value in enumerate(nums):
            complement = target - value

            # Check if the current value is a complement some earlier number was waiting for
            if value in hash_map:
                return [hash_map[value], index]

            # Otherwise, register this number's complement for future lookup
            hash_map[complement] = index

        return []  # No solution found (guaranteed not to happen per problem constraints)
