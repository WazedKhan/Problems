# Link: https://leetcode.com/problems/roman-to-integer/description/
# Title: 13. Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> str:
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        for index, roman_digit in enumerate(s):
            current_value = roman_values.get(roman_digit)
            if index < len(s) - 1 and current_value < roman_values.get(s[index + 1]):
                result -= current_value
            else:
                result += current_value
        return result
