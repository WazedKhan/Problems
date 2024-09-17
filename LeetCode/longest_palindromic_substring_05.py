# 5. Longest Palindromic Substring
class Solution:
    def is_palindrome(self, word: str) -> bool:
        return word == word[::-1]

    def longestPalindrome(self, s: str) -> str:
        pass
