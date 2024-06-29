class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        s = s.lower()
        return new_str.strip() == new_str[::-1]


solution = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(solution)
