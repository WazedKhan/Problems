class Solution:
    def expand_around_center(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # Odd length palindrome (centered at i)
            palindrome_odd = self.expand_around_center(s, i, i)
            if len(palindrome_odd) > len(res):
                res = palindrome_odd

            # Even length palindrome (centered between i and i+1)
            palindrome_even = self.expand_around_center(s, i, i + 1)
            if len(palindrome_even) > len(res):
                res = palindrome_even

        return res
