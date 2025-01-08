from typing import List


class Solution:
    def isPrefixAndSuffix(self, str_1: str, str_2: str) -> bool:
        # Check if str_1 is a prefix or suffix of str_2
        return str_2.startswith(str_1) and str_2.endswith(str_1)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if i != j and self.isPrefixAndSuffix(words[i], words[j]):
                    result += 1
        return result
