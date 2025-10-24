from typing import List

class Solution:
    def hasSameDigitsSimulation(self, s: str) -> bool:
        while len(s) != 2:
            result = ""
            for index in range(len(s)-1):
                sum = (int(s[index]) + int(s[index+1])) % 10
                result += str(sum)

            s = result
        return s[0] == s[1]

    def hasSameDigits(self, s: str) ->List[int]:
        digits = [int(char) for char in s]
        n = len(digits)
        if n == 2:
            return digits[0] == digits[1]

        r = n - 2
        coeffs = [1]

        for k in range(r):
            coeffs.append(coeffs[-1] * (r - k)//(k+1))

        coeffs = [c % 10 for c in coeffs]

        left_sum = 0
        right_sum = 0

        for index, value in enumerate(coeffs):
            left_sum += value * digits[index]
            right_sum += value * digits[index + 1]

        left = left_sum % 10
        right = right_sum % 10

        return left == right
