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

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix, postfix = [None] * nums_len, [None] * nums_len
        output = []

        prefix[0] = 1
        for prdx in range(1, nums_len):
            prefix[prdx] = prefix[prdx - 1] * nums[prdx - 1]

        postfix[-1] = 1
        for podx in range(nums_len - 2, -1, -1):
            postfix[podx] = postfix[podx + 1] * nums[podx + 1]

        for idx in range(nums_len):
            output.append(prefix[idx] * postfix[idx])

        return output
