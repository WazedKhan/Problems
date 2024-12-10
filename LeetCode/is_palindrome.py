# Problem Link: https://leetcode.com/problems/palindrome-number/
# Title: 9-Palindrome Number


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determines whether an integer is a palindrome without converting it to a string.

        Approach:
        - If the number is negative, return False immediately.
        - Reverse the integer mathematically by:
            1. Extracting the last digit using modulo (`x % 10`).
            2. Building the reversed number by multiplying the current reversed value by 10 and adding the last digit.
            3. Removing the last digit from the original number using integer division (`x // 10`).
        - Compare the reversed number with the original number.

        Parameters:
        x (int): The input integer to check for palindrome property.

        Returns:
        bool: True if the input integer is a palindrome, False otherwise.
        """
        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        # Store the original number for comparison later
        original = x
        reversed_num = 0

        # Reverse the number mathematically
        while x > 0:
            # Extract the last digit and add it to the reversed number
            reversed_num = reversed_num * 10 + x % 10
            # Remove the last digit from the original number
            x //= 10

        # Check if the original number matches the reversed number
        return original == reversed_num
