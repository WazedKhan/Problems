from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Understanding Problem:
        - there will be exactly one pair of valid indices exits
        - same element of the array/list cant be used twice
        - indices/result can be return in any order

        Brute Force (O(n²)):
        - For each element, check every other element to see if they sum to target.
        - Works, but slow for large inputs.

        Optimized Approach using a Hash Map (O(n)):
        - For each number, calculate its complement: complement = target - value.
          e.g. target=9, value=2 → complement=7 (2 needs a partner of 7).
        - Store each number's complement in a hash map: { complement: index }.
        - For every new number, check if it exists as a complement in the hash map.
          If yes, a previous number was waiting for exactly this value — return both indices.
        - This way we find the answer in a single pass.
        """

        # Tracks complements we're waiting for: { complement_value: index_of_number_that_needs_it }
        hash_map = {}

        for index, value in enumerate(nums):
            complement = target - value

            # Check if the current value is a complement some earlier number was waiting for
            if value in hash_map:
                return [hash_map[value], index]

            # Otherwise, register this number's complement for future lookup
            hash_map[complement] = index

        return []  # No solution found (guaranteed not to happen per problem constraints)

    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, return true if x is a palindrome, and false otherwise.
        Challenge: solve it without converting the integer to a string.

        Understanding the Problem:
        - A number is a palindrome if reversing it reads the same.
        - e.g. 123 reversed → 321 (different, not a palindrome)
            121 reversed → 121 (same, it's a palindrome!)
        - One tricky case: negative numbers. Even if the digits read the same,
        their sign makes them different — e.g. 121 and -121 are not palindromes.

        String Solution:
        - In programming we can easily convert an integer to a string and reverse it.
        - If the reversed string matches the original, it's a palindrome.
        - This takes O(n) time since we go through each digit once.

        Challenge Solution (without string conversion):
        - Edge case first: a negative number will never be a palindrome,
        so we don't need to worry about reversing negative integers.
        - We can use math instead:
            - Modulo (%) any number by 10 to extract its last digit.
            - Integer divide (//) by 10 to remove the last digit.

        - A naive approach would be:
            temp = x % 10
            result += temp
            x //= 10

        - But notice the issue with this approach for x = 121:
            Step 1: temp = 121 % 10 → 1,  result = 0 + 1 = 1,  x = 12
            Step 2: temp = 12  % 10 → 2,  result = 1 + 2 = 2,  x = 1
        The digits are just being summed, not reconstructed in reverse order!

        - The fix: before adding the new digit, shift result left by multiplying by 10.
        This preserves place value, just like how numbers are built digit by digit.

            Step 1: temp = 121 % 10 → 1,  result = 0 + 1 = 1,    x = 12
                    → more digits remain, so: result = 1 * 10 = 10
            Step 2: temp = 12  % 10 → 2,  result = 10 + 2 = 12,  x = 1
                    → more digits remain, so: result = 12 * 10 = 120
            Step 3: temp = 1   % 10 → 1,  result = 120 + 1 = 121, x = 0
                    → x == 0, stop. No over-multiplying!

        - Finally compare the reversed result with the original value.
        """

        # Negative numbers are never palindromes
        if x < 0:
            return False

        original = x
        result = 0

        while x > 0:
            digit = x % 10  # extract last digit
            result = result * 10 + digit  # shift result left and append digit
            x = x // 10  # remove last digit from x

        return original == result
