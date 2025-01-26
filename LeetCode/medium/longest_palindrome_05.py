class Solution:
    def expand_around_center(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # NOTE: We need to check for both odd-length and even-length palindromes.
            # Example: For "abac", "aba" is an odd-length palindrome, and for "cbbd", "bb" is an even-length palindrome.
            # If we only checked for even-length palindromes, single-character palindromes like "a" or "b" could be missed.

            even_palindrome = self.expand_around_center(s, i, i + 1)
            if len(even_palindrome) > len(res):
                res = even_palindrome

            odd_palindrome = self.expand_around_center(s, i, i)
            if len(odd_palindrome) > len(res):
                res = odd_palindrome

        return res
