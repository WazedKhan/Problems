class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bucket = dict()

        for char in s:
            bucket[char] = bucket.get(char, 0) + 1

        for char in t:
            value = bucket.get(char)
            if value is None:
                return False
            else:
                bucket[char] -= 1

        for _, value in bucket.items():
            if value != 0:
                return False

        return True
