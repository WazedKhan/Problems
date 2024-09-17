# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import defaultdict
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hash_map = defaultdict(int)
        result = list()

        full_sentence = s1.split(" ") + s2.split(" ")
        for word in full_sentence:
            hash_map[word] += 1

        for key, value in hash_map.items():
            if value == 1:
                result.append(key)

        return result


s1 = "this apple is sweet"
s2 = "this apple is sour"

solution = Solution().uncommonFromSentences(s1, s2)
print(solution)
