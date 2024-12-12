# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
# 2558. Take Gifts From the Richest Pile

import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            current_max = max(gifts)
            if math.sqrt(current_max) < current_max:
                current_max_position = gifts.index(current_max)
                # remove the current max from it position
                gifts.remove(current_max)
                gifts.insert(current_max_position, math.floor(math.sqrt(current_max)))

        return sum(gifts)


# Example usage
gifts = [25, 64, 9, 4, 100]
k = 4
solution = Solution().pickGifts(gifts, k)
print(solution)
