# from re_leet_code.container_with_most_water_two_pointer import Solution as Proven
from typing import List


class Solution:
    def max_area(self, height: List[list]) -> int:
        max_area = 0
        left_p = 0
        right_p = len(height) - 1
        while left_p < right_p:
            area = (right_p - left_p) * min(height[left_p], height[right_p])
            max_area = max(area, max_area)

            if left_p < right_p:
                left_p += 1
            else:
                right_p -= 1
        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # Output should be 49
height = [1,1] # Output should be 49
# proven_solution = Proven().maxArea(height)
solution = Solution().max_area(height)

print(f"recap: {solution}")
