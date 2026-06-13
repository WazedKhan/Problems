from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = dict()
        for index, num in enumerate(nums):
            rq = target - num
            if rq in bucket:
                return [bucket[rq], index]
            bucket[num] = index
        return []

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        bucket = dict()
        for ch in s:
            bucket[ch] = bucket.get(ch, 0) + 1

        for ch in t:
            if ch in bucket:
                bucket[ch] -= 1
                if bucket[ch] == 0:
                    bucket.pop(ch)

        if bucket:
            return False

        return True


Solution().isAnagram(s="anagram", t="nagaram")
