from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given:
        - `nums`: List of integers
        - `target`: Integer target sum
        Returns:
        - List of two indices such that nums[index1] + nums[index2] == target
        Problem:
        - Find two indices in the list such that the sum of the elements at those indices equals the target.
        Thought Process:
        - Take the fist element and check difference with the target available in the hash_map.
        - If the difference is found in the hash_map, return the indices.
        - If not found, add the current number and its index to the hash_map.
        Approach:
        - Use a hash_map to store the numbers and their indices as we iterate through the list.
        Solution:
        - Iterate through the list, calculate the difference between the target and the current number.
        - Check if the difference exists in the hash_map.
        - If it exists, return the indices of the current number and the number from the hash_map.
        """
        hash_map = {}
        for index in range(len(nums)):
            temp = target-nums[index]
            if temp in hash_map:
                return [hash_map[temp], index]
            else:
                hash_map[nums[index]] = index