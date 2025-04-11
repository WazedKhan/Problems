# https://leetcode.com/problems/count-symmetric-integers/description/?envType=daily-question&envId=2025-04-11


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        number is symmetric if the sum of its first half digits is equal to the sum of its second half digits.
        example 1:
        lets say the number is 123321, the first half is 123 and the second half is 321
        so 1 + 2 + 3 = 3 + 2 + 1 is true and its symmetric
        
        example 2:
        lets say the number is 11, the first half is 1 and the second half is 1
        so 1 = 1 is true and its symmetric
        
        NOTE: the number should be even in order to be symmetric, like 123 is not symmetric as its length is odd
        """
        
        symmetric_count = 0
        for num in range(low, high + 1):
            if self.is_symmetric(num):
                symmetric_count += 1
        return symmetric_count
        
    
    def is_symmetric(self, num: int) -> bool:
        s = str(num)
        if len(s)%2 != 0:
            return False

        mid = len(s) // 2

        # 123
        first_half = sum([int(i) for i in s[:mid]])
        # 321
        second_half = sum([int(i) for i in s[mid:]])

        return first_half == second_half
