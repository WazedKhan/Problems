from typing import List


class Solution:
    def chalk_replacer_brute_force(self, chalk: List[int], k: int) -> int:
        while True:
            for index, value in enumerate(chalk):
                if k <= 0 or k < value:
                    return index
                k -= value

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        left = k % total

        for index, value in enumerate(chalk):
            left -= value
            if left < 0:
                return index
