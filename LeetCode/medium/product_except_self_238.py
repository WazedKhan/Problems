from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix = [None] * nums_len
        postfix = [None] * nums_len
        output = []

        # find the prefix first
        prefix[0] = 1
        for index in range(1, nums_len):
            prefix[index] = nums[index - 1] * prefix[index - 1]

        # find the postfix
        postfix[-1] = 1
        for index in range(nums_len - 2, -1, -1):
            postfix[index] = nums[index + 1] * postfix[index + 1]

        # now find the output
        for index in range(nums_len):
            output.append(prefix[index] * postfix[index])

        return output
