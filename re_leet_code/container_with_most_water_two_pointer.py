from typing import List


class Solution:
    def get_area(self, left_pointer: int, right_pointer: int) -> int:
        # get the min height line from left and right pointer
        minimum_height = min(height[left_pointer], height[right_pointer])
        # get the distance between the two pointer
        distance = right_pointer - left_pointer
        # get area according to current position of pointers
        return distance * minimum_height

    def maxArea(self, height: List[int]) -> int:
        # Initialize variable to store the maximum water amount area
        # Initially set to 0 because there's no water in the container yet
        max_water_container_area = 0
        # declare the left and right pointer
        left_pointer = 0
        right_pointer = len(height) - 1

        # we need to keep moving pointers until they do not contain same vale
        while left_pointer < right_pointer:

            area = self.get_area(left_pointer=left_pointer, right_pointer=right_pointer)
            max_water_container_area = max(area, max_water_container_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water_container_area


# Example usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solve = Solution().maxArea(height=height)
print(solve)  # Output should be 49
