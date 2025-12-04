from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}  # {key: valu}

        for val in nums:
            gg = seen.get(val)
            if gg:
                return True
            seen[val] = 1

        return False

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for idx in range(len(s)):
            s_char = s[idx]
            t_chat = t[idx]

            s_map[s_char] = s_map.get(s_char, 0) + 1
            t_map[t_chat] = t_map.get(t_chat, 0) + 1

        return s_map == t_map

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx in range(len(nums)):
            hash_map[nums[idx]] = idx

        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in hash_map and hash_map[diff] != idx:
                return [idx, hash_map[diff]]
