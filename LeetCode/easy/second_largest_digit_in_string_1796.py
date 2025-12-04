class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        for char in s:
            if char.isdigit():
                d = int(char)
                if d > first:
                    second = first
                    first = d
                if first > d > second:
                    second = d
        return second
