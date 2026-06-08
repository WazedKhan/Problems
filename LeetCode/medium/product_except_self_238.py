from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix = [None] * nums_len
        postfix = [None] * nums_len
        output = []

        # find the prefix first
        for index in range(nums_len):
            if index == 0:
                prefix[index] = nums[index]
            elif index < nums_len:
                prefix[index] = nums[index] * prefix[index - 1]

        # find the postfix
        for index in range(nums_len, 0, -1):

            if index == nums_len:
                postfix[index - 1] = nums[index - 1]
            else:
                postfix[index - 1] = nums[index - 1] * postfix[index]

        # now find the output
        for index in range(nums_len):
            if index == 0:
                # with index 0 there aren't any prefix
                output.append(postfix[index + 1])
            elif index == nums_len - 1:
                # last element so no postfix
                output.append(prefix[index - 1])
            else:
                output.append(prefix[index - 1] * postfix[index + 1])

        return output
