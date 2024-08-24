class Solution:
    def isHappy(self, n: int) -> bool:
        visitor = set()
        while n not in visitor:
            visitor.add(n)
            n = self.sum_of_squares(n)
            if n == 1:
                return True
        return False

    def sum_of_squares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit**2
            output += digit
            n = n // 10
        return output


solution = Solution().isHappy(19)
print(solution)
