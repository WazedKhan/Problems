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

        s_bucket = dict()
        t_bucket = dict()

        for i in s:
            s_bucket[i] = s_bucket.get(i, 0) + 1

        for i in t:
            t_bucket[i] = t_bucket.get(i, 0) + 1

        return s_bucket == t_bucket
