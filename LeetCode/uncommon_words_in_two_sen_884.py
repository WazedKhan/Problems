# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        result = list()

        full_sentence = s1.split(" ") + s2.split(" ")
        counted_words = Counter(full_sentence)
        for word in counted_words:
            if counted_words[word] == 1 and word != "":
                result.append(word)

        return result
