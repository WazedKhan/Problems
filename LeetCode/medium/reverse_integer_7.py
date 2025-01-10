class Solution:
    def reverse(self, x: int) -> int:
        # Handle the sign and reverse the absolute value
        sign = -1 if x < 0 else 1

        x = abs(x)
        result = 0

        while x:
            result = result * 10 + (x % 10)
            x //= 10
        result = result * sign

        # check if reversed integer overflows 32 bit
        if result < -(2**31) or result > 2**31 - 1:
            return 0

        return result


solution = Solution().reverse(-123)
print(solution)
