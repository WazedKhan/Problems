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
        return [0, 0]

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given:
        - `nums`: List of integers
        Returns:
        - Boolean indicating if there are any duplicates in the list.
        Problem:
        - Check if there are any duplicate integers in the list.
        Thought Process:
        - Use a set to track seen integers.
        Approach:
        - Iterate through the list and check if each integer has been seen before.
        Solution:
        - If an integer is found in the set, return True.
        - If the loop completes without finding duplicates, return False.
        """
        seen_integer = set()
        for num in nums:
            if num in seen_integer:
                return True
            else:
                seen_integer.add(num)
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash_map = {}
        t_hash_map = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            s_hash_map[s_char] = s_hash_map.get(s_char, 0) + 1
            t_hash_map[t_char] = t_hash_map.get(t_char, 0) + 1

        return s_hash_map == t_hash_map
