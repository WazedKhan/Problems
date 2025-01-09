from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for word in words:
            if word.startswith(pref):
                result += 1
        return result
